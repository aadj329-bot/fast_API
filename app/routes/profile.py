from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl 

class Profile(BaseModel):
    username: str
    full_name: str
    bio: str
    location: str
    github_url: HttpUrl 
    primary_language: list
    secondary_language: list
    current_focus: str
    learning_path: str
    projects_count: int

router = APIRouter(prefix="/profile")

@router.get("", response_model=Profile)
def get_profile():
    return Profile(
        username="Aaron",
        full_name="Aaron D. Johnson",
        bio="Python developer focused on automation, backend APIs, and continuous integration.",
        location="Michigan, United States",
        github_url="https://github.com/aadj329-bot",
        primary_language=["Python"],
        secondary_language=["SQL"],
        current_focus="Building automation tools and backend APIs using Python and FastAPI.",
        learning_path="Certification in Python for Everybody and exploring advanced backend topics.",
        projects_count=5
    )



