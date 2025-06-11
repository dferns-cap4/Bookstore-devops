from fastapi.testclient import TestClient
from app.main import app, HealthCheckResponse


client = TestClient(app)

def test_create_book():
    response = client.post("/books/", json={"title": "Clean Code", "author": "Robert C. Martin"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Clean Code"
    assert data["author"] == "Robert C. Martin"
    assert "id" in data

def test_get_books():
    # Assuming test_create_book ran and added one book
    response = client.get("/books/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert data[0]["title"] == "Clean Code"

def test_health_check():
    response = client.get('/health-check')
    assert response.status_code == 200
    response.json() == {"message": "Healthy"}