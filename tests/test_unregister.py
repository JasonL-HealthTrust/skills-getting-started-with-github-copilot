import pytest


def test_unregister_success(client):
    # make sure a known participant exists
    email = "michael@mergington.edu"
    response = client.delete(f"/activities/Chess%20Club/signup?email={email}")
    assert response.status_code == 200
    assert "Unregistered" in response.json()["message"]

    activities = client.get("/activities").json()
    assert email not in activities["Chess Club"]["participants"]


def test_unregister_activity_not_found(client):
    r = client.delete("/activities/Bogus/signup?email=a@b.com")
    assert r.status_code == 404
    assert r.json()["detail"] == "Activity not found"


def test_unregister_email_not_signed_up(client):
    r = client.delete("/activities/Chess%20Club/signup?email=not@here.com")
    assert r.status_code == 404
    assert r.json()["detail"] == "Student not signed up for this activity"
