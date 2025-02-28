from fastapi import FastAPI
from fastapi.testclient import TestClient
from backend.app.api.endpoints.stand_endpoint import router  # Adjust the import as necessary

# Create a temporary FastAPI app for testing
app = FastAPI()
app.include_router(router)

client = TestClient(app)


def test_stands_endpoint():
    response = client.get("/stands/")
    assert response.status_code == 200
    data = response.json()
    assert "stands" in data
    # Check that the response contains exactly the expected list of stands
    expected = ["9001001001", "9001001002", "9001001098"]
    assert data["stands"] == expected
