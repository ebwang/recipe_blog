from typing import Optional
from datetime import datetime
from sqlmodel import Field, SQLModel


class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    publish_date: datetime = Field(default_factory=datetime.today)