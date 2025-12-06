import os
import openai
import fitz  # PyMuPDF for PDF processing
import docx
import re
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from .models import Summary
from .serializers import SummarySerializer
from dotenv import load_dotenv

# ✅ Load API key securely
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# ✅ Ensure API key is set
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API Key not found! Set OPENAI_API_KEY in your .env file.")

# ✅ Initialize OpenAI Client (New Syntax)
client = openai.OpenAI(api_key=OPENAI_API_KEY)


def chunk_text(text, max_chunk_size=4000):
    """
    Splits text into **sentence-based chunks** for better summarization.
    """
    sentences = re.split(r'(?<=[.!?])\s+', text)  # Split at sentence boundaries
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_chunk_size:
            current_chunk += sentence + " "
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


def generate_summary(input_text, max_tokens=250):
    """
    Calls OpenAI's GPT-3.5 Turbo API to generate a summary.
    """
    try:
        response = client.chat.completions.create(  # ✅ Corrected API syntax
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional AI summarizer. Keep the summary concise yet informative."},
                {"role": "user", "content": f"Summarize the following text:\n{input_text}"}
            ],
            max_tokens=max_tokens,
            temperature=0.4,  # ✅ Less randomness for better accuracy
            top_p=0.9
        )

        return response.choices[0].message.content  # ✅ Corrected response format

    except Exception as e:
        return f"Error: {str(e)}"


@api_view(['POST'])
def summarize_text(request):
    """
    API endpoint to accept text input or file upload and return an AI-generated summary using GPT-3.5 Turbo.
    """
    input_text = request.data.get("text", "")
    file = request.FILES.get("file", None)

    if not input_text and not file:
        return Response({"error": "No text or file provided"}, status=400)

    try:
        # ✅ Extract text from uploaded file
        if file:
            file_path = default_storage.save(file.name, ContentFile(file.read()))
            input_text = extract_text_from_file(file_path)

            if not input_text.strip():
                return Response({"error": "No valid text found in the uploaded document"}, status=400)

        # ✅ Split text into chunks if too large
        chunks = chunk_text(input_text, max_chunk_size=4000)
        summarized_chunks = [generate_summary(chunk) for chunk in chunks]

        # ✅ Combine summarized chunks into a full summary
        final_summary = " ".join(summarized_chunks)

        # ✅ Save to database
        summary_instance = Summary.objects.create(
            input_text=input_text,
            summary_text=final_summary
        )

        # ✅ Serialize response
        serializer = SummarySerializer(summary_instance)
        return Response(serializer.data, status=200)

    except Exception as e:
        return Response({"error": f"Summarization failed: {str(e)}"}, status=500)


def extract_text_from_file(file_path):
    """
    Extract text from uploaded `.txt`, `.pdf`, or `.docx` files.
    """
    _, ext = os.path.splitext(file_path)

    if ext == ".pdf":
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text("text") + "\n"
        return text

    elif ext == ".txt":
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    elif ext == ".docx":  # ✅ Support for Word Documents
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])  # Extracts text from each paragraph

    return ""
