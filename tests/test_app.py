import pytest
from src.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_empty(client):
    response = client.get('/items')
    assert response.status_code == 200

def test_add_item(client):
    response = client.post('/items', json={"name": "test"})
    assert response.status_code == 201

def test_get_items(client):
    response = client.get('/items')
    assert isinstance(response.json, list)

def test_update_item(client):
    client.post('/items', json={"name": "old"})
    response = client.put('/items/0', json={"name": "new"})
    assert response.status_code == 200

def test_delete_item(client):
    client.post('/items', json={"name": "delete"})
    response = client.delete('/items/0')
    assert response.status_code == 200

def test_invalid_update(client):
    response = client.put('/items/99', json={})
    assert response.status_code == 404

def test_invalid_delete(client):
    response = client.delete('/items/99')
    assert response.status_code == 404

def test_add_multiple(client):
    client.post('/items', json={"name": "1"})
    client.post('/items', json={"name": "2"})
    response = client.get('/items')
    assert len(response.json) >= 2

def test_content_type(client):
    response = client.post('/items', json={"name": "test"})
    assert response.content_type == 'application/json'

def test_response_structure(client):
    response = client.get('/items')
    assert isinstance(response.json, list)

