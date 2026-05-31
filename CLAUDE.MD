# Project: flask-todo-app

A simple to-do list web app built with Python and Flask. Used for learning purposes.

## Tech Stack

- Python 3.x
- Flask (web framework)
- HTML/Jinja2 templates
- JSON file for data storage (tasks.json)
- No database

## Project Structure

- `app.py` — the Flask application, all routes go here
- `templates/` — HTML templates using Jinja2
- `tasks.json` — stores all tasks as a JSON array

## Task Data Structure

Each task is a JSON object:
```json
{
  "id": 1,
  "title": "Buy groceries",
  "done": false
}