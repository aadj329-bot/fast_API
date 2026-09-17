from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_profile_endpoint():
    response = client.get("/profile")
    data = response.json()

    assert response.status_code == 200
    assert data["username"] == "Aaron"
    assert data["full_name"] == "Aaron D Johnson"
    assert data["primary_language"] == "Python"
    assert data["secondary_language"] == "SQL" 

def test_skills_endpoint():
    response = client.get("/skills")
    data = response.json()

    assert response.status_code == 200
    assert "Python" in data["languages"]
    assert "FastAPI" in data["frameworks"]
    assert "Pytest" in data["frameworks"]
    assert "GitHub" in data["tools"]
    assert "CI/CD" in data["concepts"]

def test_status_endpoints():
    response = client.get("/status")
    data = response.json()

    assert response.status_code == 200
    assert data["motivation_level"] == "High" 
    assert data["last_updated"] == "2026-09-15"
    assert len(data["goals"]) >= 3

def test_invalid_route_404():
    response = client.get("/defunk_route")
    assert response.status_code == 404    

    