# Notes REST API

A simple REST API built with **Python, Flask, and SQLite** to create, retrieve, update, and delete notes. Includes a web-based landing page to interact with the API.

## Features

- Create notes with a title and content
- Retrieve all notes or a single note by ID
- Update existing notes
- Delete notes
- Store notes persistently using SQLite
- Return JSON responses from API endpoints
- Interactive landing page for creating, viewing, and deleting notes

## Tech Stack

- **Python** — Backend programming
- **Flask** — REST API and web server
- **SQLite** — Database
- **HTML, CSS, JavaScript** — Frontend
- **Fetch API** — HTTP requests from the frontend to the backend

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/notes` | Retrieve all notes |
| `GET` | `/notes/<id>` | Retrieve a note by ID |
| `POST` | `/notes` | Create a new note |
| `PUT` | `/notes/<id>` | Update an existing note |
| `DELETE` | `/notes/<id>` | Delete a note |

### Example: Create a Note

**Request**

```http
POST /notes
Content-Type: application/json
```

**JSON Body**

```json
{
  "title": "Learn Flask",
  "content": "Build a REST API using Flask and SQLite."
}
```

### Example: Retrieve Notes

```http
GET /notes
```

The API returns notes in JSON format, including their IDs, titles, content, and creation timestamps.

## Installation and Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd <your-project-folder>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install Flask
```

### 4. Run the application

```bash
python app.py
```

Open the following URL in your browser:

```text
http://127.0.0.1:5000/
```

The SQLite database is created or accessed by the application according to its database initialization code.

## How It Works

1. The user interacts with the landing page.
2. JavaScript sends HTTP requests using the Fetch API.
3. Flask receives the requests and processes the API routes.
4. SQLite stores, retrieves, updates, or deletes notes.
5. Flask returns responses, usually in JSON format.
6. JavaScript updates the page using the returned data.

## Learning Objectives

This project provides practical experience with:

- REST API fundamentals and HTTP methods
- Flask routes and request handling
- JSON request and response bodies
- SQLite database operations
- CRUD operations
- Frontend-to-backend communication using `fetch()`
- HTTP status codes and error handling

## Current Scope

The landing page currently supports viewing, creating, and deleting notes. The API also defines endpoints for retrieving a single note and updating a note; these operations can be tested separately using a tool such as Postman.

## Future Improvements

- Add input validation and consistent error responses
- Add automated API tests
- Implement editing notes directly from the landing page
- Add authentication if the API needs multiple users

## License

This project is available for learning and personal development. Add a license file if you intend to distribute it publicly.
