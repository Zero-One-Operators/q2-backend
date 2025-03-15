from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.routers import chat
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
#from langchain.chat_models import init_chat_model
#from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

app = FastAPI()
app.include_router(
    chat.router,
    prefix="/chat",
    tags=["chat"],
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"status": "ok"}

#connect to langchain-openai
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI()

print(llm.invoke("Here is a fun fact about baseball:"))

#commented out only to run llm above without errors
#class Data(BaseModel):
 #  message: str  # The data class will have a message field
