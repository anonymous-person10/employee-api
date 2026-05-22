# Employee API — Simple Python REST API

This repository contains a minimal Python REST API for managing employee data using FastAPI.

Quick start

1. Create and activate a virtual environment:

```powershell
python -m venv venv
venv\\Scripts\\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app:

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

API endpoints

- `GET /employees` — list employees
- `POST /employees` — create employee
- `GET /employees/{id}` — get by id
- `PUT /employees/{id}` — update
- `DELETE /employees/{id}` — delete

Git workflow

```powershell
git init
git add .
git commit -m "Initial commit: Employee API"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo>.git
git push -u origin main
```

Replace the remote URL above with your GitHub repository URL.
