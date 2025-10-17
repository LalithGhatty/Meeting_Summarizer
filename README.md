🎯 Meeting Summarizer
An AI-powered web application that transcribes and summarizes meeting audio files using OpenAI's Whisper and GPT models.
🌟 Features

🎧 Audio Transcription - Convert meeting recordings to text using OpenAI Whisper
📄 AI Summarization - Generate structured summaries with key points, decisions, and action items
🎨 Modern UI - Clean, responsive interface built with React and Tailwind CSS
⚡ Fast Processing - Efficient audio processing and AI-powered analysis
🔒 Secure - API key management and secure file handling
📱 Responsive Design - Works seamlessly on desktop and mobile devices

🚀 Live Demo

Frontend: https://meeting-summarizer-frontend.onrender.com
Backend API: https://meeting-summarizer-backend-87d3.onrender.com
API Docs: https://meeting-summarizer-backend-87d3.onrender.com/docs

🛠️ Tech Stack
Backend

FastAPI - Modern Python web framework
OpenAI API - Whisper (transcription) + GPT-4 (summarization)
Uvicorn - ASGI server
Python 3.11 - Core language

Frontend

React 18 - UI library
Vite - Build tool and dev server
Tailwind CSS - Utility-first styling
JavaScript (ES6+) - Modern JavaScript

Deployment

Render - Hosting platform for both frontend and backend
GitHub - Version control and CI/CD

📁 Project Structure
meeting-summarizer/
│
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   ├── runtime.txt          # Python version specification
│   └── __init__.py          # Package initializer
│
├── frontend/
│   ├── src/
│   │   ├── App.js           # Main React component
│   │   ├── App.css          # Component styles
│   │   ├── index.js         # React entry point
│   │   └── index.css        # Global styles (Tailwind)
│   ├── public/              # Static assets
│   ├── package.json         # Node dependencies
│   ├── vite.config.js       # Vite configuration
│   └── tailwind.config.js   # Tailwind configuration
│
└── README.md                # This file
🔧 Local Development Setup
Prerequisites

Python 3.11+
Node.js 18+
OpenAI API Key (Get one here)

Backend Setup

Clone the repository:

bashgit clone https://github.com/yourusername/meeting-summarizer.git
cd meeting-summarizer/backend

Create virtual environment:

bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

bashpip install -r requirements.txt

Set environment variables:

bash# Create .env file
echo "OPENAI_API_KEY=your_api_key_here" > .env

Run the backend:

bashuvicorn main:app --reload --port 8000
Backend will be available at http://localhost:8000
Frontend Setup

Navigate to frontend:

bashcd ../frontend

Install dependencies:

bashnpm install

Create .env file:

bashecho "VITE_API_URL=http://localhost:8000" > .env

Run the frontend:

bashnpm run dev
Frontend will be available at http://localhost:3000
🌐 Deployment
This project is deployed on Render with automatic deployments from GitHub.
Deploy Your Own Instance
Backend Deployment

Fork this repository
Sign up at Render
Create a new Web Service
Connect your GitHub repository
Configure:

Root Directory: backend
Build Command: pip install -r requirements.txt
Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT


Add environment variable:

OPENAI_API_KEY: Your OpenAI API key



Frontend Deployment

Create a new Static Site on Render
Connect the same GitHub repository
Configure:

Root Directory: frontend
Build Command: npm install && npm run build
Publish Directory: dist


Add environment variable:

VITE_API_URL: Your backend URL (e.g., https://your-backend.onrender.com)



For detailed deployment instructions, see DEPLOYMENT.md
📖 API Documentation
Endpoints
GET /
Root endpoint - returns API status
json{
  "message": "Meeting Summarizer API",
  "mode": "real"
}
GET /health
Health check endpoint
json{
  "status": "healthy",
  "mode": "real"
}
POST /summarize
Upload audio file for transcription and summarization
Request:

Content-Type: multipart/form-data
Body: Audio file (MP3, WAV, M4A, etc.)

Response:
json{
  "status": "success",
  "mode": "real",
  "filename": "meeting.mp3",
  "transcript": "Full transcription text...",
  "summary": "Structured summary with key points..."
}
Interactive API documentation available at /docs
🎨 Features in Detail
AI-Powered Transcription

Uses OpenAI's Whisper model for accurate speech-to-text
Supports multiple audio formats
Handles various audio qualities and accents

Intelligent Summarization
The AI generates structured summaries with:

Key Discussion Points - Main topics and conversations
Decisions Made - Important decisions and outcomes
Action Items - Tasks, assignees, and deadlines

User Experience

Drag-and-drop file upload
Real-time processing status
Clear error messages
Responsive design for all devices
Download/copy summary and transcript

🔒 Security & Privacy

API keys stored securely as environment variables
Temporary files deleted after processing
No permanent storage of audio files
HTTPS encryption for all communications
CORS configured for security

🐛 Troubleshooting
Backend Issues
Error: OpenAI API Key not found
bash# Set your API key
export OPENAI_API_KEY="your_key_here"
Error: Port already in use
bash# Use a different port
uvicorn main:app --port 8001
Frontend Issues
Error: Cannot connect to backend

Check if backend is running
Verify VITE_API_URL is correct
Check CORS settings in backend

Build fails
bash# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
Deployment Issues
Render service won't start

Check logs in Render dashboard
Verify environment variables are set
Ensure Python/Node versions match requirements

Cold starts taking long

Free tier services sleep after 15 minutes
First request after sleep takes 30-60 seconds
Consider upgrading to paid tier for production

🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository
Create a feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
👥 Authors

Your Name - Initial work - YourGitHub

🙏 Acknowledgments

OpenAI for Whisper and GPT APIs
FastAPI community for excellent documentation
React and Vite teams for amazing tools
Render for free hosting

📞 Support

Issues: GitHub Issues
Email: your.email@example.com
Documentation: Full Docs

🔮 Roadmap

 Multi-language support
 Speaker identification (diarization)
 Export summaries as PDF
 Integration with calendar apps
 Real-time transcription
 Team collaboration features
 Custom summary templates
 Webhook notifications

💰 Costs
Development (Free)

Local development: $0

Production (Estimated Monthly)

Render Hosting: $0 (Free tier)
OpenAI API: ~$0.006 per minute of audio

Whisper: $0.006/min
GPT-4-mini: ~$0.001-0.003/request


Estimated for 100 meetings (avg 30 min each): ~$18-25/month

Tips to Reduce Costs

Use shorter audio clips for testing
Implement caching for repeated requests
Set usage limits in OpenAI dashboard
Monitor API usage regularly


⭐ Star History
If you find this project useful, please consider giving it a star! ⭐

Built with ❤️ using OpenAI, FastAPI, and React
