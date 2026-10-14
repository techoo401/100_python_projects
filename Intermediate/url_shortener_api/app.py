
from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3
import secrets
import string
from urllib.parse import urlparse

app = Flask(__name__)
DATABASE = "urls.db"


# ---------- DATABASE ----------

def get_db():
    conn = sqlite3.connect(DATABASE, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS urls (
                short TEXT PRIMARY KEY,
                long TEXT NOT NULL
            )
        """)


def get_original_url(short_code):
    with get_db() as conn:
        row = conn.execute(
            "SELECT long FROM urls WHERE short = ?",
            (short_code,)
        ).fetchone()

    return row["long"] if row else None


def is_valid_url(value):
    if not isinstance(value, str) or not value.strip():
        return False

    try:
        parsed = urlparse(value.strip())
        return (
            parsed.scheme in ("http", "https")
            and bool(parsed.hostname)
            and not any(char.isspace() for char in value.strip())
        )
    except ValueError:
        return False


def is_valid_code(code):
    return (
        isinstance(code, str)
        and 1 <= len(code) <= 30
        and code.isascii()
        and code.isalnum()
    )


def generate_code(length=6):
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def save_url(long_url, short_code=None):
    if not is_valid_url(long_url):
        return None, "Please enter a valid HTTP or HTTPS URL."

    long_url = long_url.strip()

    try:
        with get_db() as conn:
            # Custom code or randomly generated code
            if short_code:
                if not is_valid_code(short_code):
                    return None, (
                        "Short code must be 1–30 letters or digits."
                    )
                code = short_code
                conn.execute(
                    "INSERT INTO urls(short, long) VALUES (?, ?)",
                    (code, long_url)
                )
            else:
                # Retry if a randomly generated code collides.
                for _ in range(10):
                    code = generate_code()
                    try:
                        conn.execute(
                            "INSERT INTO urls(short, long) VALUES (?, ?)",
                            (code, long_url)
                        )
                        break
                    except sqlite3.IntegrityError:
                        continue
                else:
                    return None, "Could not generate a unique code. Try again."

        return code, None

    except sqlite3.IntegrityError:
        return None, "That short code is already taken."
    except sqlite3.Error:
        app.logger.exception("Database operation failed")
        return None, "A database error occurred."


# ---------- WEBSITE ----------

@app.route("/", methods=["GET", "POST"])
def home():
    short_url = None
    message = None
    success = False

    if request.method == "POST":
        long_url = request.form.get("url", "").strip()
        short_code = request.form.get("short", "").strip() or None

        code, error = save_url(long_url, short_code)

        if error:
            message = error
        else:
            short_url = url_for(
                "visit_short_url",
                short_code=code,
                _external=True
            )
            message = "Your short URL was created successfully!"
            success = True

    return render_template(
        "index.html",
        short_url=short_url,
        message=message,
        success=success
    )


# ---------- JSON API ----------

@app.route("/api/shorten", methods=["POST"])
def api_shorten():
    if not request.is_json:
        return jsonify({
            "success": False,
            "error": "Content-Type must be application/json."
        }), 400

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "success": False,
            "error": "Request body must be a JSON object."
        }), 400

    long_url = data.get("url")
    short_code = data.get("short_code")

    if not isinstance(long_url, str) or not long_url.strip():
        return jsonify({
            "success": False,
            "error": "A URL is required."
        }), 400

    if short_code is not None and (
        not isinstance(short_code, str) or not short_code.strip()
    ):
        return jsonify({
            "success": False,
            "error": "short_code must be a non-empty string."
        }), 400

    code, error = save_url(long_url, short_code)

    if error:
        status = 409 if error == "That short code is already taken." else 400
        if error == "A database error occurred.":
            status = 500

        return jsonify({
            "success": False,
            "error": error
        }), status

    return jsonify({
        "success": True,
        "short_code": code,
        "short_url": url_for(
            "visit_short_url",
            short_code=code,
            _external=True
        )
    }), 201


# ---------- REDIRECT ----------

@app.route("/<short_code>")
def visit_short_url(short_code):
    long_url = get_original_url(short_code)

    if not long_url:
        return render_template("404.html"), 404

    return redirect(long_url, code=302)


# ---------- ERROR HANDLERS ----------

@app.errorhandler(404)
def not_found(error):
    if request.path.startswith("/api/"):
        return jsonify({
            "success": False,
            "error": "API endpoint not found."
        }), 404

    return render_template("404.html"), 404


@app.errorhandler(405)
def method_not_allowed(error):
    if request.path.startswith("/api/"):
        return jsonify({
            "success": False,
            "error": "Method not allowed."
        }), 405

    return "Method not allowed.", 405


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
