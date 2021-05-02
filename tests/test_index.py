from starlette.testclient import TestClient

from minisite.main import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.text.startswith("<!DOCTYPE html>")
    assert "Lorem ipsum dolor sit amet" in response.text
