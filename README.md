# AI Document Summarizer

An AI-powered web application that summarizes large documents and text into concise, easy-to-understand content using OpenAI's GPT-3.5 Turbo model.

## 🌟 Features

- **Intelligent Summarization**: Processes large documents and generates clear, concise and meaningful summaries
- **Multiple Format Support**: Handles various document types and large text inputs
- **Download Capability**: Export summaries as downloadable documents
- **RESTful API**: Clean API architecture for easy integration
- **Responsive UI**: User-friendly interface for seamless interaction

## 🛠️ Tech Stack

**Backend:**
- Python 3.x
- Django
- Django REST Framework
- OpenAI API (GPT-3.5 Turbo)

**Frontend:**
- HTML/CSS/JavaScript
- React.js

**Database:**
- SQLite (development)
- PostgreSQL (production-ready)

**Tools:**
- Git & GitHub
- Postman (API testing)
- VS Code

## 📋 Prerequisites

Before running this project, make sure you have:

- Python 3.8 or higher
- pip (Python package manager)
- OpenAI API key
- Git

## 🚀 Installation & Setup

### 1. Project Repo
cd summarizer_project


### 2. Create virtual environment

# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Set up environment variables
# .env
SECRET_KEY=your-django-secret-key-here
DEBUG=True
OPENAI_API_KEY=your-openai-api-key-here
ALLOWED_HOSTS=localhost,127.0.0.1

### 5. Run migrations
python manage.py migrate

### 7. Run the development server
python manage.py runserver

Visit: `http://127.0.0.1:8000/`

## 📁 Project Structure
summarizer_project/
├── summarizer/              # Main Django app
│   ├── migrations/          # Database migrations
│   ├── __init__.py
│   ├── admin.py            # Admin configuration
│   ├── apps.py             # App configuration
│   ├── models.py           # Database models
│   ├── serializers.py      # DRF serializers
│   ├── urls.py             # URL routing
│   └── views.py            # View logic
├── summarizer_project/      # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Django settings
│   ├── urls.py             # Root URL configuration
│   └── wsgi.py
├── .gitignore              # Git ignore file
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              # Project documentation
```

## 🔑 Getting OpenAI API Key

1. Go to: https://platform.openai.com/api-keys
2. Sign up or log in
3. Click "Create new secret key"
4. Copy the key and add it to your `.env` file

## 📡 API Endpoints

### Summarize Text

**POST** `/api/summarize/`

**Request Body:**
```json
{
  "text": "Your long text or document content here..."
}
```

**Response:**
```json
{
  "summary": "Concise summary of the input text",
  "status": "success"
}
```

## 🧪 Testing

### Test with Postman

1. Open Postman
2. Create a POST request to `http://127.0.0.1:8000/api/summarize/`
3. Set Headers: `Content-Type: application/json`
4. Add JSON body with your text
5. Send request

### Run Django tests
python manage.py test

## 🔒 Security Notes

- Never commit API keys or sensitive data
- Always use environment variables for secrets
- Keep `.env` in `.gitignore`
- Regularly rotate your API keys

## 👤 Author

**Bhagya Lakshmi Putturu**
- GitHub: [@BhagyalakshmiPutturu](https://github.com/BhagyalakshmiPutturu)
- LinkedIn: https://www.linkedin.com/in/bhagyalakshmi-putturu-fullstack/
- Email: bhagyaputturu2000@gmail.com

## 🙏 Acknowledgments

- OpenAI for providing the GPT-3.5 Turbo API
- Django community for excellent documentation


**⭐ If you found this project helpful, please give it a star!**
