from fastapi import FastAPI

from app.routers import chat

app = FastAPI()
app.include_router(
    chat.router,
    prefix="/chat",
    tags=["chat"],
)


@app.get("/")
async def root():
    return {"status": "ok"}
