import sqlite3

DB_NAME = 'not_telegram.db'


with open(DB_NAME, 'w'):
    pass


db = sqlite3.connect(DB_NAME)
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL UNIQUE,
age INTEGER,
balance INTEGER NOT NULL
)""")


for i in range(1, 11):
    cursor.execute("INSERT INTO users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{i}', f'example{i}@gmail.com', i * 10, 1000))


cursor.execute("UPDATE users SET balance = ? WHERE mod(id, 2) <> ?", (500, 0))

cursor.execute("DELETE FROM users WHERE mod(id, 3) == ?", (1, ))

db.commit()

cursor.execute("SELECT username, email, age, balance FROM users WHERE age != ?", (60,))

all_data = cursor.fetchall()
for row in all_data:
    print("Имя: {} | Почта: {} | Возраст: {} | Баланс: {}".format(*row))
