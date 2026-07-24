def test_create_item(client):
    response = client.post(
        "/items/",
        json={
            "name": "Notebook",
            "description": "Lenovo ThinkPad",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Notebook"
    assert data["description"] == "Lenovo ThinkPad"
    assert "created_at" in data


def test_get_item_by_id(client):

    client.post(
        "/items/",
        json={
            "name": "Mouse",
            "description": "Wireless",
        },
    )

    response = client.get("/items/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Mouse"