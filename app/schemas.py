import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AuthorCreate(BaseModel):
    name: str


class AuthorUpdate(BaseModel):
    name: str | None = None


class AuthorResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    name: str
    created_at: datetime
    updated_at: datetime


class BookCreate(BaseModel):
    title: str
    author_id: uuid.UUID
    year: int | None = None
    description: str | None = None


class BookUpdate(BaseModel):
    title: str | None = None
    author_id: uuid.UUID | None = None
    year: int | None = None
    description: str | None = None


class BookResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    title: str
    author_id: uuid.UUID
    author: AuthorResponse
    year: int | None
    description: str | None
    created_at: datetime
    updated_at: datetime
