import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn

# Import your existing app
from backend.main import app as fastapi_app

# Create unified app
app = FastAPI()

# Mount your API routes
app.include_router(fastapi_app.router)

# Serve static files (React build)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve React app for all other routes
@app.get("/{full_path:path}")
async def serve_react_app(full_path: str):
    if full_path.startswith("api/") or full_path == "docs" or full_path == "redoc":
        # Let FastAPI handle API routes
        return await fastapi_app.handle_request(full_path)
    else:
        # Serve React index.html for all other routes
        return FileResponse("static/index.html")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)