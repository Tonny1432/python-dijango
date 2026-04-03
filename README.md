# 🚀 Django CRUD Student Management System

## 📌 Project Overview

This is a **basic Django CRUD (Create, Read, Update, Delete) web application** for managing student records.
The project demonstrates how data flows from **HTML forms → Django views → Database → back to UI**.

---

## 🎯 Features

* ➕ Add new student
* 📄 View all students
* ✏️ Update student details
* ❌ Delete student
* 🔐 Admin panel for manual data management

---

## 🧠 Concepts Covered

* Django Project & App structure
* Models (Database tables)
* Views (Business logic)
* Templates (HTML rendering)
* URL routing (dynamic URLs)
* Forms handling (POST request)
* CRUD operations
* Database migrations

---

## 🛠️ Tech Stack

* **Backend:** Python, Django
* **Frontend:** HTML
* **Database:** SQLite (default Django DB)

---

## 📂 Project Structure

```
day2/
│
├── day2/                # Main project folder
│   ├── settings.py
│   ├── urls.py
│
├── app/                 # Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── data.html
│   │   ├── edit.html
│
├── db.sqlite3
├── manage.py
```

---

## 🧱 Model (Database)

```python
class students(models.Model):
    s_name = models.CharField(max_length=50)
    s_age = models.IntegerField()
    s_dept = models.CharField(max_length=50)
    s_reg = models.IntegerField()
    s_email = models.CharField(max_length=100)
```

---

## 🔄 CRUD Operations

### ➕ Create (Add Student)

* HTML form sends POST request
* Data saved using:

```python
students.objects.create(...)
```

---

### 📄 Read (Display Students)

```python
students = students.objects.all()
```

* Displayed using template loop

---

### ✏️ Update (Edit Student)

```python
student = students.objects.get(id=id)
student.s_name = ...
student.save()
```

---

### ❌ Delete (Remove Student)

```python
student = students.objects.get(id=id)
student.delete()
```

---

## 🔗 URL Routing

### Project URLs (`day2/urls.py`)

```python
path('', include('app.urls'))
```

### App URLs (`app/urls.py`)

```python
path('', views.student_details),
path('delete/<int:id>/', views.delete_student),
path('edit/<int:id>/', views.edit_student),
```

---

## 🧠 How It Works (Flow)

```
User → URL → View → Model → Database
                         ↓
                     Template → User
```

---

## ▶️ How to Run

1. Install Django

```bash
pip install django
```

2. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

3. Start server

```bash
python manage.py runserver
```

4. Open browser

```
http://127.0.0.1:8000/
```

---

## 🔐 Admin Panel

Create superuser:

```bash
python manage.py createsuperuser
```

Open:

```
http://127.0.0.1:8000/admin/
```

---

## 💡 Key Learnings

* Difference between `.all()` and `.get()`
* Importance of `id` in CRUD operations
* Mapping between HTML → View → Model
* Handling POST requests safely
* Debugging Django errors

---

## 🚀 Future Improvements

* Add search functionality
* Add validation
* Convert to REST API
* Add frontend (React)

---

## 👨‍💻 Author

**Tonny**

---

## ⭐ Conclusion

This project is a **strong foundation for Django backend development** and prepares you for building real-world applications and APIs.

---
