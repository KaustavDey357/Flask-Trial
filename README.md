
# Flask Trial

A simple Flask-based TODO app using SQLite and SQLAlchemy for data storage.

## 🛠️ Features

- Create, read, delete TODO tasks
- Task completion flagging
- SQLite database integration via SQLAlchemy
- Date-stamped tasks

## 🧩 Technology Stack

- **Flask** – lightweight web framework
- **Flask-SQLAlchemy** – ORM for working with SQLite
- **Jinja2** – templating engine for HTML views
- **Bootstrap** (optional) – for UI styling

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- `pip` or `venv` for virtual environments

### Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/KaustavDey357/Flask-Trial.git
   cd Flask-Trial


2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Database Setup

Before running the app, initialize the database:

```python
from app import app, db

with app.app_context():
    db.create_all()
```

Alternatively, add this inside `app.py`:

```python
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

### Running the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` to view your TODO app.

---

## 📦 Project Structure

```
Flask-Trial/
├── app.py              # Main Flask application
├── models.py           # Database models (e.g., `Todo`)
├── templates/
│   └── index.html      # Task list & form
|   └── base.html       # The base template 
|   └── update.html     # The update task page
├── static/             # CSS / JS / images (if any)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## 🚧 Known Issues / TODOs

* [ ] Validation to prevent empty tasks
* [ ] Add user authentication
* [ ] Better error handling & input sanitization
* [ ] Deployment support (Docker, Heroku, etc.)

---

## 📄 License

MIT License © 2025 Kaustav Dey

---

## 🙏 Acknowledgments

* Based on Flask's quickstart guide
* Inspiration from online tutorials and official Flask documentation


---

### ✅ Next Actions

- Update `models.py` import if your model is defined inline in `app.py`
- Add any extra features (pagination, filters, styling, etc.)
- Include deployment notes if hosted on Heroku, Docker, etc.

Let me know if you'd like additions like CI setup, deployment workflows, or license tweaks!
::contentReference[oaicite:0]{index=0}
```
