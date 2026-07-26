# Yoruba Bridge

A simple Django web application designed for handling language translations. Built with a clean project structure, custom templates, and lightweight routing.

## 📌 Features

* **Django Backend:** Clean architecture separating project settings (`language`) from translation logic (`translate`).
* **Custom Frontend UI:** Renders HTML templates like `aishat.html` for user interactions.
* **Database Integration:** SQLite database set up and configured out of the box (`db.sqlite3`).

---

## 📂 Project Structure

```text
language/
│
├── language/                   # Core Django project directory
│   ├── settings.py             # Global settings & configurations
│   ├── urls.py                 # Main URL routing
│   ├── asgi.py & wsgi.py       # Deployment configurations
│   └── __init__.py
│
├── translate/                  # Translator app module
│   ├── migrations/             # Database migrations
│   ├── admin.py                # Admin portal configuration
│   ├── apps.py                 # App configuration
│   ├── models.py               # Data models
│   ├── views.py                # Request and response logic
│   ├── urls.py                 # App-level routes
│   └── tests.py                # Test cases
│
├── templates/                  # Interface templates
│   └── aishat.html             # Main frontend page
│
├── db.sqlite3                  # Local database
├── manage.py                   # Django management script
└── requirements.txt            # Project dependencies
```
---

## ⚙️ How to Run the Project Locally

Follow these steps to get the app running on your machine:

### 1. Prerequisites

Make sure you have **Python 3.12+** installed on your system.

### 2. Set Up a Virtual Environment

Navigate to the project folder and create a virtual environment:

* **On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate

```


* **On Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate

```



### 3. Install Required Packages

Install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt

```

### 4. Run Migrations

Apply the initial database setup:

```bash
python manage.py migrate

```

### 5. Start the Server

Start the Django development server:

```bash
python manage.py runserver

```

Head over to `http://127.0.0.1:8000/` in your browser to view the app.

---

## 🧪 Testing

To run the unit tests inside the `translate` app, run:

```bash
python manage.py test translate

```

```

```
