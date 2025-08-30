# 🏋️ ACEst Fitness & Gym – DevOps Assignment

This project is a **Flask web application** for ACEst Fitness & Gym, built as part of a DevOps assignment.
It demonstrates **Flask development, version control with Git/GitHub, automated testing with Pytest, containerization with Docker, and a CI/CD pipeline with GitHub Actions + GitHub Container Registry (GHCR)**.

---

## 🚀 Features

* Flask web application with **gym management features**:

  * `/` → Welcome page
  * `/members` → list of members
  * `/membership/<id>` → details of a specific member
  * `/workouts` → list of workout plans
  * `/trainers` → list of trainers
  * `/classes` → fitness class schedule
  * `/bmi?weight=70&height=1.75` → BMI calculator
* **JWT Authentication**:

  * `/login` → login with credentials to get JWT token
  * `/protected` → secured endpoint, requires valid token
* Unit tests with **Pytest** (positive + negative cases)
* Dockerized for portability
* GitHub Actions CI/CD pipeline:

  * Runs tests automatically
  * Builds & publishes Docker image to **GHCR**

---

## 📂 Project Structure

```
ACEst-Fitness/
│── app.py                 # Flask application
│── requirements.txt       # Dependencies
│── tests/
│    ├── __init__.py
│    ├── test_app.py       # API tests
│    └── test_auth.py      # JWT tests
│── Dockerfile             # Containerization
│── .github/
│    └── workflows/
│        └── main.yml      # CI/CD pipeline
│── README.md              # Documentation
```

---

## ⚙️ Run Locally

### 1. Clone Repo

```bash
git clone https://github.com/kalyanimuppidi01/ACEest_Fitness-and-Gym.git
cd ACEst-Fitness
```

### 2. Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Flask App

```bash
python app.py
```

App runs at 👉 [http://localhost:5000](http://localhost:5000)

---

## 🧪 Run Tests

Run all Pytest test cases:

```bash
pytest -v
```

Tests include:

* Members, workouts, trainers, classes
* Valid & invalid member lookup
* BMI calculator (valid & invalid inputs)
* JWT authentication (login success, login failure, protected access)

---

## 🐳 Run with Docker

### Build Image Locally

```bash
docker build -t aceest-fitness .
docker run -p 5000:5000 aceest-fitness
```

Open 👉 [http://localhost:5000](http://localhost:5000)

---

## 📦 Run from GitHub Container Registry (GHCR)

This repo is set up with **GitHub Actions** to automatically build and publish a Docker image.

### Pull the Latest Image

```bash
docker pull ghcr.io/<your-username>/acest-fitness:latest
```

### Run the Container

```bash
docker run -p 5000:5000 ghcr.io/<your-username>/acest-fitness:latest
```

---

## 🔐 JWT Authentication

### 1. Login to Get Token

```bash
curl -X POST http://localhost:5000/login \
     -H "Content-Type: application/json" \
     -d '{"username":"admin","password":"admin"}'
```

Response:

```json
{"access_token": "<your.jwt.token>"}
```

### 2. Access Protected Route

```bash
curl http://localhost:5000/protected \
     -H "Authorization: Bearer <your.jwt.token>"
```

Response:

```json
{"message": "Hello, admin. You are authorized!"}
```

---

## ⚡ CI/CD Pipeline (GitHub Actions)

* Triggered on every push/PR to `main`
* Jobs:

  1. **Build & Test** → installs dependencies + runs pytest
  2. **Docker Build & Push** → builds and publishes Docker image to GHCR

You can view runs under the **Actions** tab of this repo.

---

## 📌 Deliverables

* ✅ Flask app with multiple gym endpoints
* ✅ Unit tests (API + JWT)
* ✅ Dockerfile
* ✅ GitHub Actions pipeline
* ✅ README.md with full documentation
* ✅ Published Docker image on GHCR
