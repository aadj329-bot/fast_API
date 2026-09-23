# FastAPI Portfolio API

A portfolio API built with Python and FastAPI. Built to be beginner-friendly.

This project showcases my profile, skills, current status, and portfolio projects through simple API endpoints.

## Features

- Returns profile information
- Lists programming languages, frameworks, tools, and concepts
- Shows current learning goals and project status
- Lists portfolio projects
- Includes a health-check endpoint
- Uses Pydantic models to validate API data
- Includes automated tests with pytest
- Runs test automatically with GitHub Actions

## Technologies

- Python
- FastAPI
- Pydantic
- Uvicorn
- Pytest
- GitHub Actions

## Project Structure

```text
fast_API_Portfolio_API/
├── app/
│   ├── main.py
│   └── routes/
│       ├── profile.py
│       ├── projects.py
│       ├── skills.py
│       └── status.py
├── tests/
│   └── test_main.py
├── .github/
│   └── workflows/
│       └── test.yml
├── .gitignore
├── pyproject.toml
├── requirements.txt
├── run.py
└── README.md
```

## Setup

Clone the repository:

```bash
git clone https://github.com/aadj329-bot/fast_API_Portfolio_API.git
cd fast_API_Portfolio_API
```

Create a virtual environment:

### Windows PowerShell

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Run the API

Start the application with:

```bash
python run.py
```

The API will be available at:

http://127.0.0.1:8000

FastAPI also provides interactive documentation at:

http://127.0.0.1:8000/docs

With an alternative documentation page at:

http://127.0.0.1:8000/redoc

## Available Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Returns a welcome message |
| GET | `/health` | Returns the health status of the API |
| GET | `/profile` | Returns the profile information |
| GET | `/skills` | Returns skills and technologies |
| GET | `/status` | Returns current status and goals |
| GET | `/projects` | Returns portfolio projects | 


## Running Tests

Run the test suite with:

```bash
python -m pytest
```

The tests will verify several aspect:

- successful response from the API endpoints
- expected response data
- invalid routes returning 404
- unsupported methods returning 405
- response fields having the expected types
- project data being returned correctly

## Continuous Integration

This project uses GitHub Actions for continuous integration.

The workflow runs automatically when:

- Code is pushed to the repository
- A pull request is opened or updated

The workflow:

    1. Check out the repository
    2. Install Python
    3. Install dependencies from `requirements.txt`
    4. Runs the pytest test suite

The workflow file is located at:

.github/workflows/test.yml

## What I Am Learning

This project is helping me practice:

    - Python project organization
    - Building REST APIs with FastAPI
    - Creating routes and response models
    - Validating data with Pydantic
    - Writing automated tests
    - Using Git and GitHub
    - Using continuous integration
    - Improving code through small, tested changes

## Future Improvements

Future improvements will include:

    - Adding more portfolio projects
    - Connecting the API to a database
    - Adding authentication
    - Adding project filtering
    - Adding individual project lookup by ID
    - Deploying the API
    - Adding a frontend
    - Improved error handling

## Author

Created by Aaron D. Johnson.

GitHub: https://github.com/aadj329-bot



