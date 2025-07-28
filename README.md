# 🛠️ Project Management System (FastAPI + SQLModel)

A modern, production-ready backend for project and user management, built with **FastAPI**, **SQLModel**, and **PostgreSQL**.  
Includes JWT authentication, role-based access control, and auto-generated API docs.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone (https://github.com/parth-kukadiya01/parth-assignment-.git)
cd parth_assignment
```

### 2. Set up the environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Configure the database

```bash
# Copy the example configuration file
cp .env.example .env

# Edit the .env file with your database credentials
```

### 4. Run the application

```bash
python main.py
```

### 5. Access the API

Open your browser and navigate to `http://localhost:8000/docs` to access the auto-generated API documentation.

---

## 📚 Documentation

### Authentication

- Register a new user: `POST /register`
- Login: `POST /login`
- Get current user: `GET /me`

### Projects

- Get all projects: `GET /projects`
- Create a new project: `POST /projects`
- Get a specific project: `GET /projects/{project_id}`
- Update a project: `PUT /projects/{project_id}`
- Delete a project: `DELETE /projects/{project_id}`

### Users

- Get all users: `GET /users`
- Get a specific user: `GET /users/{user_id}`
- Update a user: `PUT /users/{user_id}`
- Delete a user: `DELETE /users/{user_id}`

### Running test cases
```bash
PYTHONPATH=. app/tests/test_api.py
```
