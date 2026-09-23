from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl 

class Project(BaseModel):
    name: str
    description: str 
    language: str
    url: HttpUrl 
    visibility: str 

router = APIRouter(prefix="/projects")

@router.get("", response_model=list[Project])
def projects():
    return[
        Project(
            name="fastAPI Portfolio API",
            description="A personal portfolio API built with Python and FastAPI.",
            language="Python",
            url="https://github.com/aadj329-bot/fast_API",
            visibility="public"
        ),
        Project(
            name="File Organizer",
            description="A Python project for organizing files.",
            language="Python",
            url="https://github.com/aadj329-bot/file_organizer",
            visibility="public"
        )
    ]