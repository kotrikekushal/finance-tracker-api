#  Finance Tracker API (Django REST Framework)

##  Overview

This project is a **Python-based Finance Tracking Backend System** built using **Django and Django REST Framework**.
It allows users to manage their financial records (income & expenses), analyze spending, and generate useful summaries.

The system is designed with clean backend logic, proper API structure, and user-based data handling.

---

## Features

###  Authentication

* User Registration
* User Login (Session-based)
* User Logout
* User-specific data access

---

###  Expense Management (CRUD)

* Add Expense / Income
* View all records
* Update records
* Delete records

---

###  Filtering & Search

* Search by title
* Filter by amount range
* Filter by date range

---

###  Analytics & Insights

* Total Income
* Total Expense
* Current Balance
* Monthly Report
* Top 5 Expenses
* Lowest 5 Expenses
* Average Expense
* Max / Min Expense
* Category-wise Summary

---

##  Tech Stack

* Python
* Django
* Django REST Framework
* SQLite (default database)

---

##  Project Structure

```
expense_tracker/
│
├── expense_tracker/   # Project settings
├── expenses/          # Main app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── db.sqlite3
├── manage.py
```

---

##  Setup Instructions

### 1️ Clone Repository

```bash
git clone <your-repo-link>
cd expense_tracker
```

---

### 2️ Install Dependencies

```bash
pip install django djangorestframework
```

---

### 3 Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 4️ Run Server

```bash
python manage.py runserver
```

---

##  API Endpoints

###  Authentication

| Method | Endpoint       | Description   |
| ------ | -------------- | ------------- |
| POST   | /api/register/ | Register user |
| POST   | /api/login/    | Login user    |
| POST   | /api/logout/   | Logout user   |

---

###  Expenses

| Method | Endpoint                   | Description   |
| ------ | -------------------------- | ------------- |
| POST   | /api/expenses/add/         | Add record    |
| GET    | /api/expenses/             | View records  |
| PUT    | /api/expenses/update/<id>/ | Update record |
| DELETE | /api/expenses/delete/<id>/ | Delete record |

---

###  Filtering

| Endpoint                                  | Description    |
| ----------------------------------------- | -------------- |
| /api/expenses/search/?q=keyword           | Search records |
| /api/expenses/filter/?from_date=&to_date= | Filter by date |

---

###  Analytics

| Endpoint               | Description              |
| ---------------------- | ------------------------ |
| /api/summary/          | Income, Expense, Balance |
| /api/monthly-report/   | Monthly total            |
| /api/top-5/            | Top expenses             |
| /api/lowest-5/         | Lowest expenses          |
| /api/average/          | Average expense          |
| /api/max-min/          | Max / Min expense        |
| /api/category-summary/ | Category breakdown       |

---

##  Key Design Decisions

* Used **Django ORM** for database handling
* Implemented **session-based authentication**
* Ensured **user-specific data isolation**
* Designed **clean REST APIs**
* Focused on **readability and maintainability**

---

##  Assumptions

* Each user manages their own financial data
* Categories are simple text-based values
* Authentication is session-based (not token-based)

---

##  Highlights

* Clean backend architecture
* Strong use of Django REST Framework
* Efficient data aggregation (Sum, Avg, Max, Min)
* Real-world financial analytics features

---

##  Future Improvements (Optional)

* Token-based authentication (JWT)
* Pagination
* Role-based access (Admin, Viewer, Analyst)
* CSV export
* API documentation (Swagger)

---

##  Author

Developed as part of a backend assessment project to demonstrate Python and API development skills.

---

##  Conclusion

This project demonstrates strong backend development skills including API design, data handling, authentication, and analytics processing using Python and Django.

---
