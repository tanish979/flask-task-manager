# 🧠 Flask Task Manager

A high-performance backend system for task management, built using **Flask**, **PostgreSQL**, **Redis**, **Celery**, and **Docker**.  
Designed for **scalability, modularity, and maintainability** with **JWT authentication, background jobs, and database migrations**.

---

## 🚀 Features

- ✅ **Modular Flask architecture** with Blueprints, Services & Repositories  
- 🔐 **JWT Authentication** with Role-Based Access Control (RBAC)  
- 📝 **CRUD operations** for tasks (Create, Read, Update, Soft Delete)  
- 📤 **CSV upload support** for bulk task creation  
- ⏱️ **Scheduled background jobs** via Celery & Redis  
- ⚡ **Redis caching** for performance optimization  
- 🐘 **PostgreSQL database** with SQLAlchemy & connection pooling  
- 🔐 **Secure API** with validation, rate limiting, and best practices  
- 🐳 **Full Dockerization** for easy deployment  
- 🧪 **Unit & integration testing** via Pytest  

---

## 🛠️ Tech Stack

| Layer            | Technology                     |
|------------------|--------------------------------|
| **Framework**    | Flask                          |
| **Database**     | PostgreSQL + SQLAlchemy        |
| **Queue/Cache**  | Redis                          |
| **Background Jobs** | Celery                     |
| **Auth**         | JWT, RBAC, Rate Limiting       |
| **Containerization** | Docker + Docker Compose   |
| **Testing**      | Pytest                         |

---

## 📁 Project Structure

```
flask-task-manager/
├── app/
│   ├── models/           # Database models
│   │   ├── task.py       # Task model
│   │   ├── csv_handler.py # CSV processing
│   ├── routes/           # API endpoints
│   ├── services/         # Business logic
│   │   ├── cache_service.py
│   ├── config.py         # Application configuration
│   ├── extensions.py     # Database and extensions setup
├── tests/                # Unit tests
├── .env                  # Environment variables
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── run.py                # Entry point
├── sample_tasks.csv      # Sample CSV file
└── README.md
```

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- Python 3.9+
- Docker & Docker Compose
- PostgreSQL & Redis (if running locally)

### 🚀 Running with Docker

```bash
git clone https://github.com/tanish979/flask-task-manager.git
cd flask-task-manager

# Set up environment
cp .env.example .env  # or manually create .env file

# Build and run the containers
docker-compose up --build
```

📌 **The API will be running at:** `http://localhost:5000`

---

## 📄 Sample `.env` File

```ini
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=supersecretkey
JWT_SECRET_KEY=your_jwt_secret

DATABASE_URL=postgresql://postgres:123@db:5432/task_db
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
```

---

## 📬 API Endpoints

| Method | Route         | Description |
|--------|---------------|-------------|
| POST   | `/auth/register` | Register a new user |
| POST   | `/auth/login`    | Login and receive JWT token |
| GET    | `/tasks`         | Retrieve all tasks |
| POST   | `/tasks`         | Create a new task |
| PUT    | `/tasks/<id>`    | Update a task |
| DELETE | `/tasks/<id>`    | Soft delete a task |
| POST   | `/upload`        | Bulk upload tasks via CSV |

---

## 🔐 Authentication Flow (JWT)

### 1️⃣ Login to Get Token
```http
POST /auth/login
Content-Type: application/json

{
  "username": "admin",
  "password": "yourpassword"
}
```

### 2️⃣ Use JWT Token in Requests
```http
Authorization: Bearer <your_token>
```

---

## 📤 CSV Upload (Bulk Task Creation)

Upload tasks in bulk via the `/upload` endpoint.

### ✅ Endpoint
```http
POST /upload
```

🔐 Requires Authorization Header:
```http
Authorization: Bearer <your_jwt_token>
```

### 📄 Sample CSV Format

```csv
title,description
Buy groceries,Get milk, eggs, and bread
Finish report,Complete backend report by 5PM
Call client,Discuss project scope with client
```

Save this as `sample_tasks.csv`.

---

## 🧪 Example Using `curl`

```bash
curl -X POST http://localhost:5000/upload \
  -H "Authorization: Bearer <your_jwt_token>" \
  -F "file=@sample_tasks.csv"
```

---

## 📦 Add CSV File to Project

```bash
touch sample_tasks.csv
# Paste the sample content above
git add sample_tasks.csv
git commit -m "Add sample CSV for bulk task upload"
git push
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 🧼 Code Formatting & Linting

```bash
black app/ tests/
flake8 app/
```

---

## 🔁 Postman Collection (Optional)

You can import the full Postman collection from:  
`[Insert your Postman collection link here]`

---

## ✨ Roadmap

- [ ] Swagger / OpenAPI docs
- [ ] Pagination & advanced filtering
- [ ] Admin panel frontend (React or Streamlit)
- [ ] CI/CD with GitHub Actions
- [ ] Email notifications (Celery + SMTP)

---

## 📄 License

MIT License. See `LICENSE` file.

---

## 👨‍💻 Author

**Tanish**  
📌 [GitHub: tanish979](https://github.com/tanish979)  
💼 Backend Intern — Building high-performance Flask systems  

---

## 🤝 Contributions

PRs welcome! Please open issues or feature requests.

---

## 🐳 Docker Quick Start (One-liner)

```bash
docker-compose down -v && docker-compose up --build
```
