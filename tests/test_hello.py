from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_endpoint_hello_returns_world():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}
