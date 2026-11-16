# fastapi-cicd

Minimal FastAPI REST API built with Python 3.15.2 for learning GitHub Actions, CI/CD, automated testing, and cloud deployment.

## Project Structure

```text
fastapi-cicd/
├── .gitignore
├── pyproject.toml
├── README.md
├── src/
│   └── fastapi_cicd/
│       ├── __init__.py
│       └── main.py
└── tests/
    ├── __init__.py
    └── test_main.py
```

## Windows Setup (PowerShell)

1. Verify Python 3.15.2 is available:

   ```powershell
   py -3.15 --version
   ```

2. Create and activate the virtual environment:

   ```powershell
   py -3.15 -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks script execution for `Activate.ps1`, you can either run:

   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
   ```

   or invoke the virtual environment executables directly without activating (e.g., `.\.venv\Scripts\python.exe`).

3. Install the project and development dependencies:

   ```powershell
   python -m pip install -e ".[dev]"
   ```

## Running the Application

Start the development server with Uvicorn:

```powershell
uvicorn fastapi_cicd.main:app --reload
```

Available endpoints:

- `GET /` — Service metadata (`service`, `version`, `status`)
- `GET /health` — Health check (`{"status": "ok"}`)
- `GET /docs` — Interactive Swagger UI

## Running Tests and Linting

Run automated tests with Pytest:

```powershell
pytest
```

Run Ruff lint and format checks:

```powershell
ruff check .
ruff format --check .
```
