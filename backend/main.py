from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
import tempfile

# ✅ Load environment variables (Railway will provide these)
openai_api_key = os.getenv("OPENAI_API_KEY")

# Use mock mode if no API key, real mode if key exists
USE_REAL_AI = bool(openai_api_key)

if USE_REAL_AI:
    from openai import OpenAI
    client = OpenAI(api_key=openai_api_key)
    print("✅ Using real OpenAI API")
else:
    print("⚠️ Using mock mode - add OPENAI_API_KEY for real AI")

app = FastAPI(title="Meeting Summarizer API")

# ✅ Production CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "https://*.railway.app",
        "https://*.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Meeting Summarizer API", "mode": "real" if USE_REAL_AI else "mock"}

@app.post("/summarize")
async def summarize_meeting(file: UploadFile):
    """Handles meeting audio upload → transcription → summary generation"""
    tmp_path = None
    
    try:
        # Validate file type
        if not file.content_type or not (file.content_type.startswith('audio/') or file.content_type in ['application/octet-stream']):
            raise HTTPException(status_code=400, detail="Please upload an audio file")

        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
            content = await file.read()
            if len(content) == 0:
                raise HTTPException(status_code=400, detail="Uploaded file is empty")
            tmp.write(content)
            tmp_path = tmp.name

        if USE_REAL_AI:
            # Real AI processing
            with open(tmp_path, "rb") as audio_file:
                transcription = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file
                ).text

            prompt = f"""
            Summarize this meeting transcript:
            {transcription}
            
            Provide:
            1. Key discussion points
            2. Decisions made  
            3. Action items with responsible people
            """

            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
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
            mock_transcription = f"Mock transcription of {file.filename}. Add OPENAI_API_KEY for real transcription."
            mock_summary = """Mock Summary:
1. KEY DISCUSSION POINTS:
- Project timeline review
- Budget planning

2. DECISIONS MADE:
- Approved Q4 budget
- Extended deadlines

3. ACTION ITEMS:
- John: Update project plan
- Jane: Schedule team meeting

Add OPENAI_API_KEY for real AI summaries."""
            
            response_data = {
                "status": "success", 
                "mode": "mock",
                "filename": file.filename,
                "transcript": mock_transcription,
                "summary": mock_summary,
                "note": "Using mock data. Add OPENAI_API_KEY for real AI functionality."
            }

        return JSONResponse(content=response_data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")
    finally:
        # Cleanup
        if tmp_path and os.path.exists(tmp_path):
            os.remove(tmp_path)

@app.get("/health")
async def health_check():
    return {"status": "healthy", "mode": "real" if USE_REAL_AI else "mock"}