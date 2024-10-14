import os
import sqlite3

from sqlite3 import OperationalError


def initiate_db():
    cursor.execute("""CREATE TABLE IF NOT EXISTS products(
                   title TEXT NOT NULL,
                   description TEXT,
                   price INTEGER NOT NULL,
                   image TEXT NOT NULL
                   )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY,
                   username TEXT NOT NULL,
                   email TEXT NOT NULL,
                   age INTEGER NOT NULL,
                   balance INTEGER NOT NULL
                   )""")
    db.commit()
    for i in range(1, 5):
        cursor.execute("INSERT INTO products VALUES (?, ?, ?, ?)",
                       (f"Product{i}",
                        f"Description of Product{i}",
                        100 * i,
                        f'bot/images/product{i}.jpg')
                       )
    db.commit()


def get_all_products():
    data = cursor.execute("SELECT * FROM products")
    return data.fetchall()


def add_user(username, email, age):
    cursor.execute("""INSERT INTO users(username, email, age, balance) VALUES (?, ?, ?, ?)""",
                   (username, email, age, 1000))
    db.commit()


def is_included(username):
    user = cursor.execute("SELECT * FROM users WHERE username == ?", (username,)).fetchone()
    if user:
        return True
    return False


DB_NAME = "database.db"

if DB_NAME not in os.listdir():
    with open(DB_NAME, 'w'):
        pass

db = sqlite3.connect(DB_NAME)
cursor = db.cursor()

try:
    cursor.execute("SELECT * FROM products")
except OperationalError:
    initiate_db()
