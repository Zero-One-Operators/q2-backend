import datetime

from fastapi import APIRouter

from app.models.message import Message

router = APIRouter()


@router.post("/")
async def chat(message: Message):
    current_time = datetime.datetime.now()
    response = Message(
        message="Hello from the chat Agent! Your message: " + message.message , timestamp=current_time.isoformat()
    )

    return response.model_dump()
