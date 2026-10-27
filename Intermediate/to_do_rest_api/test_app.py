
import pytest
import app as todo_app


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Give each test its own temporary database.
    test_db = tmp_path / "test_todo.db"
    monkeypatch.setattr(todo_app, "DATABASE", str(test_db))

    todo_app.create_table()

    return todo_app.app.test_client()


def create_todo(client, name="Learn testing"):
    return client.post("/todos", json={"todo": name})


def test_create_todo(client):
    response = create_todo(client)

    assert response.status_code == 201
    assert "id" in response.get_json()


def test_get_all_todos(client):
    create_todo(client, "Learn Flask")
    create_todo(client, "Learn pytest")

    response = client.get("/todos")

    assert response.status_code == 200
    assert len(response.get_json()) == 2


def test_get_single_todo(client):
    created = create_todo(client).get_json()
    todo_id = created["id"]

    response = client.get(f"/todos/{todo_id}")

    assert response.status_code == 200
    assert response.get_json()["todo"] == "Learn testing"


def test_missing_todo(client):
    response = client.get("/todos/999")

    assert response.status_code == 404


def test_complete_todo(client):
    todo_id = create_todo(client).get_json()["id"]

    response = client.put(f"/todos/{todo_id}")

    assert response.status_code == 200

    todo = client.get(f"/todos/{todo_id}").get_json()
    assert todo["status"] == "completed"


def test_delete_todo(client):
    todo_id = create_todo(client).get_json()["id"]

    response = client.delete(f"/todos/{todo_id}")

    assert response.status_code == 200
    assert client.get(f"/todos/{todo_id}").status_code == 404


def test_invalid_todo(client):
    response = client.post("/todos", json={"todo": "   "})

    assert response.status_code == 400


def test_unknown_route(client):
    response = client.get("/this-route-does-not-exist")

    assert response.status_code == 404
    assert response.is_json
