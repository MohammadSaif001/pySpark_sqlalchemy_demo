from email.mime import text
import sqlite3

connection = sqlite3.connect("student_database.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY," \
               "name TEXT," \
               "marks INTEGER)"
               )
cursor.execute("INSERT INTO students (name,marks) VALUES (""'Zawberu', 85)")
print("Inserted data successfully in database ")
connection.commit()


print("Database and table created successfully.")
result = connection.execute("SELECT * FROM students")
for row in result:
    print(row)
connection.close()