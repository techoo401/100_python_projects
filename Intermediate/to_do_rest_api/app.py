from flask import Flask, jsonify, request, render_template
import sqlite3
from contextlib import contextmanager
from datetime import datetime

app = Flask(__name__)

DATABASE = "todo.db"


@contextmanager
def get_db():
    conn = sqlite3.connect(DATABASE, timeout=10)
    conn.row_factory = sqlite3.Row

    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def create_table():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                todo TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'pending',
                created_at TEXT NOT NULL
            )
        """)


def add_todo(todo):
    with get_db() as conn:
        cursor = conn.execute("""
            INSERT INTO todos (todo, created_at)
            VALUES (?, ?)
        """, (todo, datetime.now().isoformat(timespec="seconds")))

        return cursor.lastrowid

def get_all_todos():
    with get_db() as conn:
        todos = conn.execute("""
            SELECT * FROM todos
            ORDER BY id DESC
        """).fetchall()

        return [dict(todo) for todo in todos]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/todos", methods=["GET"])
def todos_route():
    todos = get_all_todos()
    return jsonify(todos), 200


@app.route("/todos/<int:todo_id>", methods=["GET"])
def single_todo_route(todo_id):
    with get_db() as conn:
        todo = conn.execute(
            "SELECT * FROM todos WHERE id = ?",
            (todo_id,)
        ).fetchone()

    if todo is None:
        return jsonify({"error": "Todo not found"}), 404

    return jsonify(dict(todo)), 200

@app.route("/todos", methods=["POST"])
def create_todo_route():
    data = request.get_json(silent=True)

    if not data or not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object"}), 400

    todo = data.get("todo")

    if not isinstance(todo, str) or not todo.strip():
        return jsonify({"error": "Todo is required"}), 400

    todo_id = add_todo(todo.strip())

    return jsonify({
        "message": "Todo created successfully",
        "id": todo_id
    }), 201

@app.route("/todos/<int:todo_id>", methods=["PUT"])
def complete_todo_route(todo_id):
    with get_db() as conn:
        cursor = conn.execute(
            "UPDATE todos SET status = ? WHERE id = ?",
            ("completed", todo_id)
        )

        if cursor.rowcount == 0:
            return jsonify({"error": "Todo not found"}), 404

    return jsonify({
        "message": "Todo marked as completed",
        "id": todo_id,
        "status": "completed"
    }), 200

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo_route(todo_id):
    with get_db() as conn:
        cursor = conn.execute(
            "DELETE FROM todos WHERE id = ?",
            (todo_id,)
        )

        if cursor.rowcount == 0:
            return jsonify({"error": "Todo not found"}), 404

    return jsonify({
        "message": "Todo deleted successfully",
        "id": todo_id
    }), 200

@app.route("/test-500")
def test_500():
    raise Exception("Testing 500 error")

@app.errorhandler(400)
def bad_request(error):
    return jsonify({
        "error": "Bad request",
        "message": "Please check your request data."
    }), 400

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "error": "Method not allowed",
        "message": "This HTTP method is not supported for this endpoint."
    }), 405

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "error": "Internal server error",
        "message": "Something went wrong on the server."
    }), 500

if __name__ == "__main__":
    create_table()
    app.run()