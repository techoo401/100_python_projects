from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()

@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_db_connection()

    tasks = conn.execute(
        "SELECT * FROM tasks"
    ).fetchall()

    conn.close()

    return jsonify([dict(task) for task in tasks])

@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    conn = get_db_connection()

    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    conn.close()

    if task is None:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(dict(task))

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    conn = get_db_connection()

    cursor = conn.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (data["title"],)
    )

    conn.commit()

    task_id = cursor.lastrowid

    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    conn.close()

    return jsonify(dict(task)), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()

    if not data or "title" not in data or "completed" not in data:
        return jsonify({
            "error": "Title and completed are required"
        }), 400

    conn = get_db_connection()

    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    if task is None:
        conn.close()
        return jsonify({"error": "Task not found"}), 404

    conn.execute(
        """
        UPDATE tasks
        SET title = ?, completed = ?
        WHERE id = ?
        """,
        (data["title"], data["completed"], task_id)
    )

    conn.commit()

    updated_task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    conn.close()

    return jsonify(dict(updated_task))

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db_connection()

    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?",
        (task_id,)
    ).fetchone()

    if task is None:
        conn.close()
        return jsonify({"error": "Task not found"}), 404

    conn.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Task deleted successfully"})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)