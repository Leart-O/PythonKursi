import sqlite3

connection = sqlite3.connect('example.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS WorkPlace (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
''')

connection.commit()

cursor.executemany('''
INSERT INTO employees (name, position, department, salary)
VALUES (?, ?, ?, ?)
''', [
    ('John Doe', 'Software Engineer', 'IT', 75000.00),
    ('Jane Smith', 'Data Analyst', 'Marketing', 65000.00),
    ('Emily Johnson', 'Project Manager', 'Operations', 85000.00),
])

connection.commit()

cursor.execute('SELECT * FROM employees')

rows = cursor.fetchall()
for row in rows:
    print(f"employee id: {row[0]}, name: {row[1]}, position: {row[2]}, department: {row[3]}, salary: {row[4]}")

connection.close()