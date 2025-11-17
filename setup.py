import sqlite3

connection = sqlite3.connect("sample.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY," \
               "name TEXT," \
               "marks INTEGER)"
               )
cursor.execute("INSERT INTO students (name,marks) VALUES (""'Zawberu', 85)")
connection.commit()
connection.close()

print("Database and table created successfully.")
