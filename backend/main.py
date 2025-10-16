from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from openai import OpenAI
import os
import tempfile
import json

# ✅ Load environment variables
# ⚠️ Always use mock mode
USE_REAL_AI = False
client = None
print("⚠️ Mock mode enabled: No OpenAI API required")


# ✅ Create FastAPI app
app = FastAPI(title="Meeting Summarizer API")
frontend_url = os.getenv("FRONTEND_URL", "https://meeting-summarizer-frontend-0kdi.onrender.com")

 

# ✅ Enable CORS for all origins (since we're serving frontend from same domain)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url, "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ API Routes
@app.get("/")
async def root():
    return {"message": "Meeting Summarizer API", "mode": "real" if USE_REAL_AI else "mock"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "mode": "real" if USE_REAL_AI else "mock"}

@app.post("/summarize")
async def summarize_meeting(file: UploadFile):
    """Handles meeting audio upload → transcription → summary generation"""
    tmp_path = None
    
    try:
        # Validate file type
        if not file.content_type or not (file.content_type.startswith('audio/') or file.content_type in ['application/octet-stream']):
            raise HTTPException(status_code=400, detail="Please upload an audio file (MP3, WAV, M4A, etc.)")

        # Step 1: Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            content = await file.read()
            if len(content) == 0:
                raise HTTPException(status_code=400, detail="Uploaded file is empty")
            tmp.write(content)
            tmp_path = tmp.name

        if USE_REAL_AI and client:
            # Real AI processing
            print("🎧 Transcribing audio with Whisper...")
            with open(tmp_path, "rb") as audio_file:
                transcription = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                ).text

            print("🧠 Generating summary with GPT...")
            prompt = f"""
            Summarize the following meeting transcript into clear sections:
            
            1. KEY DISCUSSION POINTS:
            - Main topics covered
            - Important conversations
            
            2. DECISIONS MADE:
            - Key decisions reached
            - Voting outcomes (if any)
            
            3. ACTION ITEMS:
            - Tasks with responsible people
            - Deadlines (if mentioned)
            
            Transcript:
            {transcription}
            """

            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000
            )

            summary = completion.choices[0].message.content
            
            response_data = {
                "status": "success",
                "mode": "real",
                "filename": file.filename,
                "transcript": transcription,
                "summary": summary
            }
        else:
            # Mock responses for testing
            print("🤖 Using mock data...")
            mock_transcription = f"""This is a mock transcription of your audio file: {file.filename}

In a real meeting, this would contain the actual spoken content from your audio file.
The OpenAI API would transcribe this using Whisper-1 model.

Sample conversation:
- John: Let's discuss the Q4 project timeline
- Sarah: We need to extend the deadline by 2 weeks
- Mike: I agree, and we should allocate more budget
- Lisa: I'll handle the client communication"""

            mock_summary = """# Meeting Summary (Mock Data)

## 1. KEY DISCUSSION POINTS:
- Project timeline review for Q4
- Budget allocation and resource planning
- Team capacity and workload distribution

## 2. DECISIONS MADE:
- Approved 2-week extension for project deadline
- Increased Q4 budget by 15%
- Hired 2 additional developers

## 3. ACTION ITEMS:
- **John Doe**: Update project timeline by Friday
- **Sarah Smith**: Finalize budget document
- **Mike Johnson**: Schedule interviews for new hires
- **Lisa Brown**: Send client update email

*Note: This is mock data. Add a valid OPENAI_API_KEY environment variable for real AI summaries.*"""

            response_data = {
                "status": "success", 
                "mode": "mock",
                "filename": file.filename,
                "transcript": mock_transcription,
                "summary": mock_summary,
                "note": "Using mock data. Add OPENAI_API_KEY for real AI functionality."
            }

        return response_data

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")
    finally:
        # Cleanup temp file
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)
            print("🧹 Temporary file cleaned up")

# ✅ Frontend Serving (Add this at the END of the file)
try:
    # Serve static files from frontend build
    app.mount("/static", StaticFiles(directory="../frontend/dist"), name="static")
    
    # Serve React app for all routes except API routes
    @app.get("/{full_path:path}")
    async def serve_react_app(full_path: str):
        # Don't serve React for API routes
        if full_path.startswith("api") or full_path in ["docs", "redoc", "openapi.json"]:
            raise HTTPException(status_code=404, detail="Not found")
        return FileResponse("../frontend/dist/index.html")
    
    print("✅ Frontend serving configured")
except Exception as e:
    print(f"⚠️ Frontend serving not available: {e}")

# ✅ For direct script execution
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)