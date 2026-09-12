from flask import Flask, render_template, request, redirect, abort
import sqlite3
from urllib.parse import urlparse

app = Flask(__name__)


def init_db():
    connection = sqlite3.connect("urls.db")

    connection.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT UNIQUE NOT NULL,
            original_url TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def is_valid_url(url):
    try:
        result = urlparse(url)

        return (
            result.scheme in ("http", "https")
            and result.netloc
        )

    except ValueError:
        return False


def save_url(short_code, original_url):
    connection = sqlite3.connect("urls.db")

    connection.execute(
        """
        INSERT INTO urls (short_code, original_url)
        VALUES (?, ?)
        """,
        (short_code, original_url)
    )

    connection.commit()
    connection.close()


# 1. Shorten URL
@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        url = request.form["url"].strip()
        short_code = request.form["short_code"].strip()

        if not is_valid_url(url):
            return render_template(
                "index.html",
                error="Please enter a valid URL. Example: https://facebook.com"
            )

        try:
            save_url(short_code, url)

        except sqlite3.IntegrityError:
            return render_template(
                "index.html",
                error="This short code already exists. Please choose another one."
            )

        short_url = f"http://127.0.0.1:5000/{short_code}"

        return render_template(
            "index.html",
            short_url=short_url
        )

    return render_template("index.html")


# 2. Open Short URL
@app.route("/<short_code>")
def redirect_to_url(short_code):

    connection = sqlite3.connect("urls.db")

    result = connection.execute(
        """
        SELECT original_url
        FROM urls
        WHERE short_code = ?
        """,
        (short_code,)
    ).fetchone()

    connection.close()

    if result is None:
        abort(404)

    return redirect(result[0])


# 3. Show All URLs
@app.route("/urls")
def show_urls():

    connection = sqlite3.connect("urls.db")

    urls = connection.execute(
        """
        SELECT short_code, original_url
        FROM urls
        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()

    return render_template(
        "urls.html",
        urls=urls
    )

@app.route("/delete/<short_code>", methods=["POST"])
def delete_url(short_code):
    connection = sqlite3.connect("urls.db")

    connection.execute(
        """
        DELETE FROM urls
        WHERE short_code = ?
        """,
        (short_code,)
    )

    connection.commit()
    connection.close()

    return redirect("/urls")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)