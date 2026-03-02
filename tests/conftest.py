import copy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities as activities_store


@pytest.fixture(scope="session")
def client():
    """TestClient instance for the FastAPI app."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activities dict before each test.

    A deep copy of the original data is kept on module import, and this fixture
    restores the dictionary to its initial state on every function invocation.
    """
    # make a deep copy so that nested lists/dicts are restored too
    initial = copy.deepcopy(
        {
            "Chess Club": {
                "description": "Learn strategies and compete in chess tournaments",
                "schedule": "Fridays, 3:30 PM - 5:00 PM",
                "max_participants": 12,
                "participants": ["michael@mergington.edu", "daniel@mergington.edu"],
            },
            "Programming Class": {
                "description": "Learn programming fundamentals and build software projects",
                "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
                "max_participants": 20,
                "participants": ["emma@mergington.edu", "sophia@mergington.edu"],
            },
            "Gym Class": {
                "description": "Physical education and sports activities",
                "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
                "max_participants": 30,
                "participants": ["john@mergington.edu", "olivia@mergington.edu"],
            },
            "Basketball": {
                "description": "Competitive basketball team and practice sessions",
                "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
                "max_participants": 15,
                "participants": ["james@mergington.edu"],
            },
            "Tennis Club": {
                "description": "Learn and practice tennis skills with experienced coaches",
                "schedule": "Tuesdays and Saturdays, 3:30 PM - 5:00 PM",
                "max_participants": 10,
                "participants": ["noah@mergington.edu", "ava@mergington.edu"],
            },
            "Painting & Drawing": {
                "description": "Explore various painting and drawing techniques",
                "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
                "max_participants": 16,
                "participants": ["isabella@mergington.edu"],
            },
            "Drama Club": {
                "description": "Perform in school plays and theatrical productions",
                "schedule": "Thursdays, 3:30 PM - 5:30 PM",
                "max_participants": 25,
                "participants": ["lucas@mergington.edu", "mia@mergington.edu"],
            },
            "Debate Team": {
                "description": "Develop argumentation and public speaking skills",
                "schedule": "Mondays and Fridays, 3:30 PM - 4:30 PM",
                "max_participants": 18,
                "participants": ["alexander@mergington.edu"],
            },
            "Science Club": {
                "description": "Conduct experiments and explore scientific concepts",
                "schedule": "Thursdays, 4:00 PM - 5:30 PM",
                "max_participants": 22,
                "participants": ["charlotte@mergington.edu", "benjamin@mergington.edu"],
            },
        }
    )
    activities_store.clear()
    activities_store.update(initial)
