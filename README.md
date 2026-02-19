**🗓️ Expiry Tracker CLI (Python + PostgreSQL)**

A command-line based Expiry Tracking System built using Python and PostgreSQL.<br>
This application helps users manage items with purchase and expiry dates and track products that are about to expire.<br>

✅ 95% of the code written independently<br>
⚡ Completed within one day

📌 Features

➕ Add items with:
+ Category (Item Name)
+ Purchase Date
+ Expiry Date
+ Quantity
📋 View all stored items in formatted table view<br>
⏳ View items expiring within the next 3 days<br>
❌ Delete items by name<br>
🔐 Secure parameterized SQL queries<br>
🔄 Transaction handling with commit & rollback<br>
📊 Clean CLI table output using tabulate<br>

🛠️ Tech Stack<br>
    🐍 Python<br>
    🐘 PostgreSQL<br>
    🔌 psycopg2 <br>
    📊 tabulate<br>

🗄️ Database Schema<br>
CREATE TABLE itemlist (<br> 
    id SERIAL PRIMARY KEY,<br>
    category VARCHAR(100) NOT NULL,<br>
    purches_At DATE NOT NULL,<br>
    expiry_date DATE NOT NULL,<br>
    quantity VARCHAR(100) NOT NULL<br>
);<br>


⚙️ Installation & Setup
1️⃣ Clone the Repository<br>
git clone https://github.com/your-username/expiry-tracker-cli.git<br>
cd expiry-tracker-cli

2️⃣ Install Dependencies<br>
pip install psycopg2 tabulate

If psycopg2 gives installation issues on Windows:<br>
pip install psycopg2-binary

3️⃣ Setup PostgreSQL Database<br>
Create a database:<br>
CREATE DATABASE project;

Update the connection credentials in the script:<br>
conn = psycopg2.connect(<br>
    host="localhost",<br>
    database="project",<br>
    user="postgres",<br>
    password="your_password"<br>
)<br>

4️⃣ Run the Application
python your_script_name.py

🖥️ Application Flow
1. Add Items
2. View Items
3. View Expiring Items
4. Delete Items<br>
-1. Exit<br>
The system runs in a continuous loop until the user exits.<br>


🔐 Security & Best Practices Implemented
+ Parameterized queries to prevent SQL Injection
+ Exception handling using try/except
+ Proper transaction control using commit & rollback
+ Modular function-based structure
+ Clean database cursor handling
