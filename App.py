import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller.video_processing_controller import VideoProcessing

app = FastAPI()
videoProcessing = VideoProcessing()

app.include_router(videoProcessing.router)
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def health():
    return {"message": "Hello World"}
