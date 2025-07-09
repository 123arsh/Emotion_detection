from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReflectionRequest(BaseModel):
    text: str

class EmotionResponse(BaseModel):
    emotion: str
    confidence: float

# Mock emotion list
EMOTIONS = ["Happy", "Sad", "Angry", "Anxious", "Excited", "Calm", "Nervous"]

@app.post("/analyze", response_model=EmotionResponse)
def analyze_emotion(request: ReflectionRequest):
    if not request.text.strip():
        raise HTTPException(status_code=400, detail="Text input is required.")
    # Fake analysis: pick a random emotion and confidence
    emotion = random.choice(EMOTIONS)
    confidence = round(random.uniform(0.7, 0.99), 2)
    return {"emotion": emotion, "confidence": confidence} 