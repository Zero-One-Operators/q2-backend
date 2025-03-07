import datetime

import pytest
from starlette.testclient import TestClient
from app.main import app
from app.models.message import Message

client = TestClient(app)

FAKE_TIME = datetime.datetime(2021, 7, 1, 12, 0, 0)


@pytest.fixture
def patch_datetime_now(monkeypatch):
    class MockNow(datetime.datetime):
        @classmethod
        def now(cls):
            return FAKE_TIME

    monkeypatch.setattr(datetime, "datetime", MockNow)


def test_endpoint_hello_returns_(patch_datetime_now):
    message = Message(message="Hello World!", timestamp="2021-07-01T12:00:00")
    expected_response = Message(
        message="Hello from the chat Agent! Your message: " + message.message, timestamp=FAKE_TIME.isoformat()
    )

    response = client.post("/chat", json=message.model_dump())
    assert response.status_code == 200

    response_json = response.json()
    assert response_json == expected_response.model_dump()
