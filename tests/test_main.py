from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Aaron's GitHub API"}


def test_profile_endpoint():
    response = client.get("/profile")
    data = response.json()

    assert response.status_code == 200
    assert data["username"] == "Aaron"
    assert data["full_name"] == "Aaron D. Johnson"
    assert data["primary_language"] == ["Python"]
    assert data["secondary_language"] == ["SQL"] 

def test_skills_endpoint():
    response = client.get("/skills")
    data = response.json()

    assert response.status_code == 200
    assert "Python" in data["languages"]
    assert "FastAPI" in data["frameworks"]
    assert "Pytest" in data["frameworks"]
    assert "GitHub" in data["tools"]
    assert "CI/CD" in data["concepts"]

def test_status_endpoint():
    response = client.get("/status")
    data = response.json()

    assert response.status_code == 200
    assert data["motivation_level"] == "High" 
    assert len(data["goals"]) >= 3
    assert data["current_projects"] == "Building personal FastAPI portfolio API"

def test_projects_endpoint():
    response = client.get("/projects")
    data = response.json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 2

    project_names = {project["name"] for project in data}

    assert "fastAPI Portfolio API" in project_names
    assert "File Organizer" in project_names 

    fastapi_project = next(
        project for project in data 
        if project["name"] == "fastAPI Portfolio API" 
    )

    file_organizer_project = next(
        project for project in data
        if project["name"] == "File Organizer"
    )

    assert fastapi_project["visibility"] == "public"
    assert file_organizer_project["visibility"] == "public"

def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_invalid_route_404():
    response = client.get("/defunk_route")

    assert response.status_code == 404   


def test_profile_has_expected_field_types():
    response = client.get("/profile")
    data = response.json()

    assert isinstance(data["username"], str)
    assert isinstance(data["primary_language"], list)
    assert isinstance(data["projects_count"], int)

def test_post_to_profile_is_not_allowed():
    response = client.post("/profile")

    assert response.status_code == 405

def test_status_response_contract():
    response = client.get("/status")
    data = response.json()

    assert isinstance(data["goals"], list)
    assert len(data["goals"]) > 0
    assert isinstance(data["motivation_level"], str)
    assert isinstance(data["last_updated"], str)
    






