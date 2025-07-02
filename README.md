# 💰 Django Budget Tracker

A simple and powerful personal finance tracker built using Django. Helps users manage their income and expenses with monthly summaries and categories.

---

## ✨ Features

- User Registration and Login
- Add Income and Expense Transactions
- Categorize Transactions (Food, Salary, Travel, etc.)
- View Total Income, Expenses, and Current Balance
- Monthly Summary Table
- Bootstrap UI with Django Templates
- Delete Transactions

---

## 🛠 Tech Stack

- Python 3.8+
- Django 3.2+
- SQLite (Default DB)
- Bootstrap 5

---

## 🚀 Getting Started

### 1. Clone the repo:
```bash
git clone https://github.com/yourusername/django-budget-tracker.git
cd django-budget-tracker
```

### 2. Setup virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install requirements:
```bash
pip install -r requirements.txt
```

### 4. Apply migrations:
```bash
python manage.py migrate
```

### 5. Run the server:
```bash
python manage.py runserver
```

---

## 📂 Folder Structure
```
budget_tracker/
├── budget_tracker/         # Main project
├── transactions/           # App for income/expenses
├── templates/              # HTML templates
├── static/                 # Optional static files
├── db.sqlite3              # SQLite DB
├── .gitignore
├── README.md
└── requirements.txt
```