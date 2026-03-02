import pytest


def test_signup_success(client):
    email = "newstudent@mergington.edu"
    # choose an activity that exists
    response = client.post("/activities/Chess%20Club/signup?email=newstudent@mergington.edu")
    assert response.status_code == 200
    data = response.json()
    assert "Signed up" in data["message"]

    # verify participant present
    activities = client.get("/activities").json()
    assert email in activities["Chess Club"]["participants"]


def test_signup_activity_not_found(client):
    response = client.post("/activities/Nonexistent/signup?email=a@b.com")
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_duplicate_email(client):
    email = "duplicate@mergington.edu"
    # first attempt should succeed
    r1 = client.post(f"/activities/Gym%20Class/signup?email={email}")
    assert r1.status_code == 200
    # second attempt should be rejected
    r2 = client.post(f"/activities/Gym%20Class/signup?email={email}")
    assert r2.status_code == 400
    assert "already signed up" in r2.json()["detail"]
