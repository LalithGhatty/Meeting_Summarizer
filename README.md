
A full-stack web application that transcribes meeting audio and generates AI-powered summaries with key discussion points, decisions, and action items using OpenAI's Whisper and GPT models.

https://img.shields.io/badge/React-18.2.0-blue
https://img.shields.io/badge/FastAPI-0.104.1-green
https://img.shields.io/badge/OpenAI-Whisper%252BGPT-orange
https://img.shields.io/badge/Netlify-Deployed-brightgreen
https://img.shields.io/badge/Cyclic-Backend-success

✨ Features
🎤 Audio Upload - Support for MP3, WAV, M4A files

📝 AI Transcription - Powered by OpenAI Whisper

🤖 Smart Summarization - GPT-powered meeting summaries

🎯 Structured Output - Key points, decisions, and action items

💫 Modern UI - Built with React & Tailwind CSS

🚀 Easy Deployment - Deployed on Netlify + Cyclic

🏗️ Architecture
text
Frontend (React + Vite) → Backend (FastAPI) → OpenAI API
       ↓                          ↓
    Netlify                    Cyclic.sh
🚀 Live Demo
Frontend: https://your-app.netlify.app

Backend API: https://your-app.cyclic.app

API Documentation: https://your-app.cyclic.app/docs

📸 Screenshots
(Add screenshots of your application here)

🛠️ Technology Stack
Frontend
React 18 - UI framework

Vite - Build tool & dev server

Tailwind CSS - Styling

Fetch API - HTTP requests

Backend
FastAPI - Modern Python web framework

OpenAI API - Whisper transcription & GPT summarization

Uvicorn - ASGI server

Python-multipart - File upload handling

Deployment
Netlify - Frontend hosting

Cyclic.sh - Backend hosting

GitHub - Version control

🏃‍♂️ Quick Start
Prerequisites
Python 3.8+

Node.js 16+

OpenAI API key

Local Development
Clone the repository

bash
git clone https://github.com/yourusername/meeting-summarizer.git
cd meeting-summarizer
Backend Setup

bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp .env.example .env
# Edit .env with your OPENAI_API_KEY

# Start backend server
uvicorn main:app --reload --port 8000
Frontend Setup

bash
cd frontend

# Install dependencies
npm install

# Start frontend server
npm run dev
Access the application

Frontend: http://localhost:5173

Backend API: http://localhost:8000

API Docs: http://localhost:8000/docs

🌐 Deployment
Frontend (Netlify)
Build the project: npm run build

Drag & drop the dist folder to netlify.com/drop

Or connect GitHub repo in Netlify dashboard

Set environment variable: VITE_API_URL=your-backend-url

Backend (Cyclic.sh)
Go to cyclic.sh

Sign up with GitHub

Click "Link Your Own" and select your repository

Set environment variable: OPENAI_API_KEY=your-key

📚 API Documentation
Endpoints
Method	Endpoint	Description
POST	/summarize	Upload audio file for summarization
GET	/health	Health check endpoint
GET	/	API information
Example Request
bash
curl -X POST "https://your-app.cyclic.app/summarize" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@meeting.mp3"
Example Response
json
{
  "status": "success",
  "filename": "meeting.mp3",
  "transcript": "Full meeting transcript...",
  "summary": "1. KEY DISCUSSION POINTS:\n- Project timeline\n- Budget allocation\n\n2. DECISIONS MADE:\n- Approved Q4 budget\n\n3. ACTION ITEMS:\n- John: Update project plan"
}
🗂️ Project Structure
text
meeting-summarizer/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   ├── .env.example        # Environment template
│   └── __init__.py         # Python package
├── frontend/
│   ├── src/
│   │   ├── App.jsx         # Main React component
│   │   ├── main.jsx        # React entry point
│   │   └── App.css         # Styles
│   ├── public/
│   │   └── _redirects      # Netlify SPA configuration
│   ├── package.json        # Node dependencies
│   ├── vite.config.js      # Vite configuration
│   └── index.html          # HTML template
├── .gitignore              # Git ignore rules
└── README.md              # Project documentation
⚙️ Configuration
Environment Variables
Backend (.env)

env
OPENAI_API_KEY=sk-your-openai-api-key
Frontend (.env)

env
VITE_API_URL=http://localhost:8000
🔧 Troubleshooting
Common Issues
CORS Errors

Ensure backend CORS is configured for your frontend domain

Check environment variables are set correctly

File Upload Issues

Verify audio file format (MP3, WAV, M4A supported)

Check file size limits

OpenAI API Errors

Verify API key is valid and has sufficient credits

Check API rate limits

Netlify 404 Errors

Ensure _redirects file is in public folder

Verify SPA redirects are configured

Build Issues
bash
# If frontend build fails
cd frontend
rm -rf node_modules
npm install
npm run build

# If backend deployment fails
cd backend
pip install -r requirements.txt
🤝 Contributing
Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
OpenAI for Whisper and GPT APIs

FastAPI for the excellent web framework

Vite for the frontend tooling

Netlify for easy frontend deployment

Cyclic for reliable backend hosting

📞 Support
If you have any questions or run into issues, please open an issue on GitHub.

Built with ❤️ using FastAPI, React, and OpenAI

Transform your meetings into actionable insights! 
