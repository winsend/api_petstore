from pydantic import BaseModel, Field
<<<<<<< HEAD
=======

>>>>>>> fa5ed65 (Add cleanup after tests)
from typing import List, Optional

class Category(BaseModel):
    id: int
    name: str

class Tag(BaseModel):
    id: int
    name: str

class Pet(BaseModel):
    id: Optional[int] = None
    category: Optional[Category] = None
    name: str = Field(..., min_length=1, max_length=100)
    photoUrls: List[str] = Field(default_factory=list)
    tags: List[Tag] = Field(default_factory=list)
    status: str = Field(..., pattern="^(available|pending|sold)$")