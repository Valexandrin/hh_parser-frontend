from pydantic import BaseModel
from datetime import datetime


class Vacancy(BaseModel):
    uid: int
    area: str
    description: str = None
    employer: str
    name: str
    published_at: datetime
    requirement: str = None
    responsibility: str = None
    salary_from: str = None
    salary_to: str = None
    schedule: str
    status: str
    url: str = None
