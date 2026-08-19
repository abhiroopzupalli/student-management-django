# Student Management System (Django + MySQL)

A simple CRUD web application to manage student records — add, view, search, edit,
and delete students. Built with Django, MySQL, and Bootstrap.

## Features
- Add / edit / delete student records
- Search students by name, roll number, or department
- Django admin panel for quick data management
- Responsive UI with Bootstrap

## Tech Stack
- Python, Django
- MySQL (via mysqlclient)
- HTML, CSS (Bootstrap 5)

## Setup Instructions

1. **Clone/copy this project** and open a terminal inside the `student_management` folder.

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate      # on Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   If `mysqlclient` fails to install on Windows, download the matching wheel from
   https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient or switch to SQLite
   (see step 4).

4. **Set up the database**

   **Option A — MySQL (recommended, matches the JD's SQL skill requirement):**
   ```sql
   CREATE DATABASE student_db CHARACTER SET utf8mb4;
   ```
   Then update the password in `student_management/settings.py` under `DATABASES`.

   **Option B — SQLite (fastest way to try it out):**
   In `student_management/settings.py`, comment out the MySQL `DATABASES` block
   and uncomment the SQLite block right below it.

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create an admin user (optional, for /admin panel)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the server**
   ```bash
   python manage.py runserver
   ```
   Visit http://127.0.0.1:8000/ to use the app, or http://127.0.0.1:8000/admin/
   for the admin panel.

## Project Structure
```
student_management/
├── manage.py
├── requirements.txt
├── student_management/      # project settings, urls
└── students/                 # app: models, views, forms, templates
```

## Possible Extensions (good talking points in an interview)
- Add pagination to the student list
- Add REST API endpoints with Django REST Framework
- Add authentication so only logged-in staff can edit/delete
- Deploy to Render/Railway with a managed MySQL database

## Author
Zupalli Abhiroop Kumar
