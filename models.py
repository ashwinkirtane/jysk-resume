from pydantic import BaseModel
from typing import List

class Experience(BaseModel):
    company: str
    position: str
    years: str
    description: str

class Education(BaseModel):
    institution: str
    location: str
    degree: str
    years: str

class Skill(BaseModel):
    category: str
    items: List[str]
