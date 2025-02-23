import datetime

from pydantic import BaseModel


class Message(BaseModel):
    message: str
    timestamp: str = datetime.datetime.now().isoformat()
