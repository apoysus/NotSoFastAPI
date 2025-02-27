import pytest
from fastapi import FastAPI, Request
from fastapi.testclient import TestClient
from notsofastapi import ratelimit
import time

app = FastAPI()

@app.get("/limited")
@ratelimit(limit=3, period=2)
async def limited_endpoint(request: Request):
    return {"message": "Allowed"}

client = TestClient(app)

def test_ratelimit():
    for _ in range(3):
        response = client.get("/limited")
        assert response.status_code == 200

    response = client.get("/limited")
    assert response.status_code == 429

    time.sleep(2)
    response = client.get("/limited")
    assert response.status_code == 200

if __name__ == "__main__":
    pytest.main()