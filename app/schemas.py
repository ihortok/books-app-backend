import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class BookCreate(BaseModel):
    title: str
    author: str
    year: int | None = None
    description: str | None = None


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    year: int | None = None
    description: str | None = None


class BookResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    title: str
    author: str
    year: int | None
    description: str | None
    created_at: datetime
    updated_at: datetime
