def test_create_item(client):
    response = client.post(
        "/items/",
        json={
            "name": "Notebook",
            "description": "Lenovo ThinkPad",
        },
    )

    assert response.status_code == 201

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

def test_update_item(client):
    # Crear el item
    client.post(
        "/items/",
        json={
            "name": "Notebook",
            "description": "Lenovo",
        },
    )

    # Actualizarlo
    response = client.put(
        "/items/1",
        json={
            "name": "Notebook Pro",
            "description": "Lenovo ThinkPad",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Notebook Pro"
    assert data["description"] == "Lenovo ThinkPad"

def test_update_item_not_found(client):
    response = client.put(
        "/items/999",
        json={
            "name": "Notebook",
            "description": "Lenovo",
        },
    )

    assert response.status_code == 404

def test_update_item_invalid_data(client):
    client.post(
        "/items/",
        json={
            "name": "Notebook",
            "description": "Lenovo",
        },
    )

    response = client.put(
        "/items/1",
        json={
            "name": 123,
        },
    )

    assert response.status_code == 422

def test_partial_update_item(client):
    client.post(
        "/items/",
        json={
            "name": "Notebook",
            "description": "Lenovo",
        },
    )

    response = client.put(
        "/items/1",
        json={
            "description": "Lenovo ThinkPad",
        },
    )

    assert response.status_code == 200

    data = response.json()

    # El nombre debe permanecer igual
    assert data["name"] == "Notebook"

    # Solo cambia la descripción
    assert data["description"] == "Lenovo ThinkPad"

# Eliminar

def test_delete_item(client):
    client.post(
        "/items/",
        json={
            "name": "Notebook",
            "description": "Lenovo",
        },
    )

    response = client.delete("/items/1")

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "Notebook"

def test_delete_item_not_found(client):
    response = client.delete("/items/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Item with id 999 not found"

def test_deleted_item_cannot_be_retrieved(client):
    client.post(
        "/items/",
        json={
            "name": "Notebook",
            "description": "Lenovo",
        },
    )

    delete_response = client.delete("/items/1")
    assert delete_response.status_code == 200

    get_response = client.get("/items/1")

    assert get_response.status_code == 404