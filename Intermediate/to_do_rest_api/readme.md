# Todo REST API

A simple REST API built with **Python, Flask, and SQLite** to manage todos using CRUD operations.

## Features

- Create a todo
- Retrieve all todos or a single todo
- Mark a todo as completed
- Delete a todo
- JSON responses and HTTP error handling
- Custom HTML homepage and 404 page

## Tech Stack

- Python
- Flask
- SQLite
- REST API
- Postman

## Installation

```bash
git clone <your-repository-url>
cd <project-folder>

python -m venv venv
```

Activate the virtual environment:

**Windows**
```bash
venv\Scripts\activate
```

Install Flask:

```bash
python -m pip install flask
```

Run the application:

```bash
python app.py
```

The API runs at `http://127.0.0.1:5000`.

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/todos` | Get all todos |
| GET | `/todos/<id>` | Get a single todo |
| POST | `/todos` | Create a todo |
| PUT | `/todos/<id>` | Mark a todo as completed |
| DELETE | `/todos/<id>` | Delete a todo |

## Create a Todo

Send a `POST` request to `/todos` with a JSON body:

```json
{
  "todo": "Learn REST API"
}
```

## Database

SQLite stores todos in `todo.db`, with the following fields:

- `id` — Unique identifier
- `todo` — Todo description
- `status` — Pending or completed
- `created_at` — Creation timestamp

## Run Tests

Install pytest and run the automated tests:

```bash
python -m pip install pytest
python -m pytest -v
```

## Purpose

Built as a Python learning project to practice REST API development, database operations, HTTP methods, error handling, and automated testing.
