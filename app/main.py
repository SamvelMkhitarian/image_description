from contextlib import asynccontextmanager

import uvicorn
from app.database import engine
from app.endpoints import router as endpoint_router
from fastapi import FastAPI
from app.models import Base


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(endpoint_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
