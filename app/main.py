from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session

app = FastAPI()

@app.get("/")
async def read_root(session: AsyncSession = Depends(get_session)):
    result = await session.execute("SELECT 1")
    return {"message": "Connected to DB!"}
