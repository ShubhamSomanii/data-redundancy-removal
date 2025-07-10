import sqlite3
import re

# Connect to database
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
''')

# Check valid email
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    return re.match(pattern, email)

# Insert data
def insert_data(name, email):
    if not is_valid_email(email):
        print("❌ Invalid email format.")
        return
    try:
        cursor.execute("INSERT INTO entries (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print("✅ Data inserted.")
    except sqlite3.IntegrityError:
        print("⚠️ Duplicate email found.")

# Show data
def show_entries():
    cursor.execute("SELECT * FROM entries")
    for row in cursor.fetchall():
        print(row)

# Main menu
while True:
    print("\n--- MENU ---")
    print("1. Add Entry")
    print("2. Show Entries")
    print("3. Exit")
    choice = input("Choice: ")

    if choice == '1':
        name = input("Enter name: ")
        email = input("Enter email: ")
        insert_data(name, email)
    elif choice == '2':
        show_entries()
    elif choice == '3':
        break
    else:
        print("❌ Invalid choice.")
