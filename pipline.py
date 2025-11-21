import sqlalchemy
from sqlalchemy import create_engine, text

print(sqlalchemy.__version__)

engine = create_engine("sqlite:///sql_warehouse.db")
connection = engine.connect()

# Create employees table
connection.execute(text("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    emp_name TEXT,
    emp_age INTEGER,
    emp_salary REAL
)
"""))

# Create departments table
connection.execute(text("""
CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dept_name TEXT,
    location TEXT,
    manager_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES employees(emp_id)
)
"""))

# Insert HR department
connection.execute(text("""
INSERT INTO departments (dept_name, location, manager_id)
SELECT 'HR', 'New York', 1
WHERE NOT EXISTS (
    SELECT 1 FROM departments WHERE dept_name='HR'
)
"""))

# Insert Finance department
connection.execute(text("""
INSERT INTO departments (dept_name, location, manager_id)
SELECT 'Finance', 'Chicago', 2
WHERE NOT EXISTS (
    SELECT 1 FROM departments WHERE dept_name='Finance'
)
"""))

# Insert IT department
connection.execute(text("""
INSERT INTO departments (dept_name, location, manager_id)
SELECT 'IT', 'San Francisco', 3
WHERE NOT EXISTS (
    SELECT 1 FROM departments WHERE dept_name='IT'
)
"""))

connection.commit()

result = connection.execute(text("SELECT * FROM departments"))
for row in result:
    print(row)
connection.close()
