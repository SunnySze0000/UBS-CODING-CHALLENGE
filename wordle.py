from fastapi import FastAPI, HTTPException, status, Header, Depends
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

app = FastAPI()

class WordleGameRequest(BaseModel):
    word: str

@app.post("/wordle-game")
async def wordle_game(request: WordleGameRequest):
    # Process the game logic here
    result = {
        "message": f"Word '{request.word}' processed",
        "status": "success"
    }
    
    return result
