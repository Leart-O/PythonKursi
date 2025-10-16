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

connection.commit()

cursor.execute('''
INSERT INTO employees (name, position, department, salary)
VALUES (????)
''', ('John Doe', 'Software Engineer', 'IT', 75000.00))

connection.commit()

cursor.execute('SELECT * FROM employees')
