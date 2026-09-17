from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/profile")
    data = response.json()

    assert response.status_code == 200
    assert "Python" in data["languages"]
    assert "FastAPI" in data["frameworks"]
    assert "Pytest" in data["frameworks"]
    assert "GitHub" in data["tools"]