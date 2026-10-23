
from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime
from contextlib import contextmanager

app = Flask(__name__)
DATABASE = 'notes_api.db'


# ---------- DATABASE ----------

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


def push_note(title, content):
    created_at = datetime.now().isoformat()

    with get_db() as conn:
        cursor = conn.execute(
            '''INSERT INTO notes (title, content, created_at)
               VALUES (?, ?, ?)''',
            (title, content, created_at)
        )
        return cursor.lastrowid


def notes():
    with get_db() as conn:
        rows = conn.execute('SELECT * FROM notes').fetchall()
        return [dict(row) for row in rows]


def find_note(note_id):
    with get_db() as conn:
        row = conn.execute(
            'SELECT * FROM notes WHERE id = ?',
            (note_id,)
        ).fetchone()

        return dict(row) if row else None


# ---------- VALIDATION ----------

def get_json_data():
    if not request.is_json:
        return None, (
            jsonify(success=False,
                    message='Content-Type must be application/json'),
            415
        )

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return None, (
            jsonify(success=False, message='Invalid JSON object'),
            400
        )

    return data, None


def validate_note(data):
    for field in ('title', 'content'):
        value = data.get(field)

        if not isinstance(value, str) or not value.strip():
            return f"'{field}' must be a non-empty string"

    return None


# ---------- ROUTES ----------

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes()), 200


@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = find_note(note_id)

    if note is None:
        return jsonify(
            success=False, message='Note not found'
        ), 404

    return jsonify(note), 200


@app.route('/notes', methods=['POST'])
def create_note():
    data, error = get_json_data()

    if error:
        return error

    message = validate_note(data)
    if message:
        return jsonify(success=False, message=message), 400

    note_id = push_note(
        data['title'].strip(),
        data['content'].strip()
    )

    return jsonify(
        success=True,
        message='Note created successfully',
        id=note_id
    ), 201


@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data, error = get_json_data()

    if error:
        return error

    message = validate_note(data)
    if message:
        return jsonify(success=False, message=message), 400

    with get_db() as conn:
        result = conn.execute(
            '''UPDATE notes
               SET title = ?, content = ?
               WHERE id = ?''',
            (
                data['title'].strip(),
                data['content'].strip(),
                note_id
            )
        )

        if result.rowcount == 0:
            return jsonify(
                success=False, message='Note not found'
            ), 404

    return jsonify(
        success=True, message='Note updated successfully'
    ), 200


@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    with get_db() as conn:
        result = conn.execute(
            'DELETE FROM notes WHERE id = ?',
            (note_id,)
        )

        if result.rowcount == 0:
            return jsonify(
                success=False, message='Note not found'
            ), 404

    return jsonify(
        success=True, message='Note deleted successfully'
    ), 200


# ---------- ERROR HANDLERS ----------

@app.errorhandler(404)
def not_found(error):
    return jsonify(
        success=False, message='Resource not found'
    ), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify(
        success=False, message='HTTP method not allowed'
    ), 405


@app.errorhandler(sqlite3.Error)
def database_error(error):
    app.logger.exception('Database error')
    return jsonify(
        success=False, message='Internal database error'
    ), 500


@app.errorhandler(500)
def internal_error(error):
    app.logger.exception('Internal server error')
    return jsonify(
        success=False, message='Internal server error'
    ), 500


if __name__ == '__main__':
    app.run()
