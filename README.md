# 🗓️ Expiry Tracker CLI (Python + PostgreSQL)

A command-line based Expiry Tracking System built using **Python** and **PostgreSQL**.  
This application helps users manage items with purchase and expiry dates and track products that are about to expire.

> ✅ 95% of the code written independently  
> ⚡ Completed within one day  

---

## 📌 Features

- ➕ Add items with:
  - Category (Item Name)
  - Purchase Date
  - Expiry Date
  - Quantity

- 📋 View all stored items in formatted table view  
- ⏳ View items expiring within the next 3 days  
- ❌ Delete items by name  
- 🔐 Secure parameterized SQL queries  
- 🔄 Transaction handling with commit & rollback  
- 📊 Clean CLI table output using `tabulate`  

---

## 🛠️ Tech Stack

- Python 3.x
- PostgreSQL
- psycopg2
- tabulate

---

## 🗄️ Database Schema

```sql
CREATE TABLE itemlist ( 
    id SERIAL PRIMARY KEY,
    category VARCHAR(100) NOT NULL,
    purches_At DATE NOT NULL,
    expiry_date DATE NOT NULL,
    quantity VARCHAR(100) NOT NULL
);
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/expiry-tracker-cli.git
cd expiry-tracker-cli
```

### 2️⃣ Install Dependencies

```bash
pip install psycopg2 tabulate
```

If psycopg2 gives installation issues on Windows:

```bash
pip install psycopg2-binary
```

### 3️⃣ Setup PostgreSQL Database

Create a database:

```sql
CREATE DATABASE project;
```

Update the connection credentials in the script:

```python
conn = psycopg2.connect(
    host="localhost",
    database="project",
    user="postgres",
    password="your_password"
)
```

### 4️⃣ Run the Application

```bash
python your_script_name.py
```

---

## 🖥️ Application Flow

```
1. Add Items
2. View Items
3. View Expiring Items
4. Delete Items
-1. Exit
```

The system runs in a continuous loop until the user exits.

---

## 🔐 Security & Best Practices Implemented

- Parameterized queries to prevent SQL Injection  
- Exception handling using try/except  
- Proper transaction control using commit & rollback  
- Modular function-based structure  
- Clean database cursor handling  

---

## 📚 What I Learned

- PostgreSQL database connectivity with Python  
- Writing and executing SQL queries manually  
- Handling transactions and exceptions  
- Designing CLI-based systems  
- Structuring small backend projects cleanly  

---

## 🚀 Future Improvements

- Add update functionality  
- Add user authentication  
- Convert into a Flask/Django web app  
- Add email notifications for expiring items  
- Dockerize the project  

---

## 👨‍💻 Author

**Suraj Patil**  
Computer Science Student | Backend Learner  

---
