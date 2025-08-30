# ACEst Fitness & Gym

This project is a **Flask web application** for ACEst Fitness & Gym.
It demonstrates **Flask development, version control with Git/GitHub, automated testing with Pytest, containerization with Docker, and CI/CD with GitHub Actions**.

---

## 🚀 Features

* Flask web application with sample routes:

  * `/` → Welcome page
  * `/members` → JSON response with sample members
* Unit tests with **Pytest**
* Dockerized application for portability
* GitHub Actions CI/CD pipeline:

  * Runs tests automatically on push/pull request
  * Builds Docker image if tests pass

---

## 📂 Project Structure

```
ACEst-Fitness/
│── app.py                 # Flask application
│── requirements.txt       # Dependencies
│── tests/
│    ├── __init__.py
│    └── test_app.py       # Pytest test cases
│── Dockerfile             # Containerization
│── .github/
│    └── workflows/
│        └── main.yml      # CI/CD pipeline
│── README.md              # Project documentation
```

---

## ⚙️ Setup & Run Locally

### 1. Clone Repository

```bash
git clone https://github.com/kalyanimuppidi01/ACEest_Fitness-and-Gym.git
```

### 2. Create Virtual Environment

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

## 🧪 Running Tests

Run all Pytest test cases:

```bash
pytest -v
```

---

## 🐳 Running with Docker

### 1. Build Image

```bash
docker build -t aceest-fitness .
```

### 2. Run Container

```bash
docker run -p 5000:5000 aceest-fitness
```

Open [http://localhost:5000](http://localhost:5000)

---

## ⚡ CI/CD with GitHub Actions

* Workflow file: `.github/workflows/main.yml`
* Trigger: Runs automatically on every `push` and `pull_request`
* Pipeline Steps:

  1. Check out repository
  2. Set up Python
  3. Install dependencies
  4. Run tests with Pytest
  5. Build Docker image (only if tests pass)

You can see pipeline runs under the **Actions** tab of this repo.

---

## 📌 Deliverables

* Flask app (`app.py`)
* Tests (`tests/test_app.py`)
* `requirements.txt`
* `Dockerfile`
* GitHub Actions workflow (`main.yml`)
* This `README.md`

---
