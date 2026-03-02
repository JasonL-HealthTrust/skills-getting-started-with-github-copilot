def test_get_activities_returns_all(client):
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    # topology: expecting at least a few named activities
    assert "Chess Club" in data
    assert isinstance(data["Chess Club"], dict)
    # count participants matches initial fixture
    assert len(data["Chess Club"]["participants"]) == 2
