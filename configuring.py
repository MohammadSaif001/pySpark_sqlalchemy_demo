from sqlalchemy import create_engine, text

#!Database se connect
engine = create_engine("sqlite:///mydatabase.db")  
connection = engine.connect()

connection.execute(text("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    marks REAL
)
"""))


connection.execute(text("""
INSERT INTO students (name, age, marks)
VALUES ('Saif', 21, 89.5),
       ('Ayesha', 22, 92.0)
"""))

connection.commit()

result = connection.execute(text("SELECT * FROM students"))
for row in result:
    print(row)
