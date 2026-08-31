from pathlib import Path
import sys

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from app import app


client = TestClient(app)


def test_github_skills_activity_is_listed():
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    assert "GitHub Skills" in data

    activity = data["GitHub Skills"]
    assert "GitHub" in activity["description"]
    assert activity["schedule"]
    assert activity["max_participants"] > 0
