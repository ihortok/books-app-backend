from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.routers import authors, books


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    from app.database import engine

    await engine.dispose()


app = FastAPI(title="Books API", version="0.1.0", lifespan=lifespan)

app.include_router(authors.router)
app.include_router(books.router)
