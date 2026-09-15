from fastapi import APIRouter
from pydantic import BaseModel

class Skills(BaseModel):
    languages: list
    frameworks: list
    tools: list
    concepts: list

router = APIRouter(prefix="/skills")

@router.get("", response_model=Skills)
def get_skills():
    return Skills(
        languages=["Python", "SQL"],
        frameworks=["FastAPI", "Pytest"],
        tools=["Git", "GitHub", "Docker"],
        concepts=["API design", "automation", "CI/CD", "debugging"]
    )