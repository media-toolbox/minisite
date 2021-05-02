import pytest
from async_asgi_testclient import TestClient

from minisite.main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_index():
    response = await client.get("/")
    assert response.status_code == 200
    assert response.text.startswith("<!DOCTYPE html>")
    assert "Lorem ipsum dolor sit amet" in response.text
