from fastapi import FastAPI
from starlette.testclient import TestClient

app = FastAPI()


@app.get("/")
async def dummy():
    return {"msg": "Hello World"}


client = TestClient(app)


def test_dummy():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
