import uuid
from datetime import datetime
from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Person(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    display_name: Optional[str] = Field(default=None, index=True)
    first_name: Optional[str] = Field(default=None)
    last_name: Optional[str] = Field(default=None)
    headline: Optional[str] = Field(default=None)
    org: Optional[str] = Field(default=None)
    title: Optional[str] = Field(default=None)
    location: Optional[str] = Field(default=None)
    bio_summary: Optional[str] = Field(default=None)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)

    identities: List["Identity"] = Relationship(back_populates="person")


class Identity(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)
    person_id: uuid.UUID = Field(foreign_key="person.id")
    type: str = Field(index=True)  # email, phone, linkedin, etc.
    value: str
    label: Optional[str] = Field(default=None)
    verified: bool = Field(default=False)
    source_id: Optional[uuid.UUID] = Field(default=None)
    last_seen_at: Optional[datetime] = Field(default=None)

    person: Optional[Person] = Relationship(back_populates="identities")
