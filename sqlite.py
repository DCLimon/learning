# From Corey Schafer's YT Tutorial on Python SQLite

# +---------+
# | Imports |
# +---------+

import sqlite3

from oop2 import Employee

# +-----------+
# | Create db |
# +-----------+

# Create connection to db, which also creates the named db if not existing
conn = sqlite3.connect('employee.db')  # ':memory:' argument creates in-RAM db

# Create cursor to query db
cursor = conn.cursor()

# Create Employees db
cursor.execute("""
    CREATE TABLE employees (
        first_name TEXT,
        last_name TEXT,
        pay integer
    )
""")

# Commit the current transaction to db, then close db connection
conn.commit()
conn.close()


# +-----------------------+
# | Add an Employee to db |
# +-----------------------+

# Open new connection & create cursor
conn = sqlite3.connect('employee.db')
cursor = conn.cursor()

# Add an employee to db, specified by ('first', 'last', pay) tuple
cursor.execute("INSERT INTO employees VALUES ('Corey', 'Shafer', 50000)")
conn.commit()  # commit the new employee


# +--------------+
# | Query the db |
# +--------------+

# Select all rows in employees w/ last_name 'Shafer', and return as an iterable.
cursor.execute("SELECT * FROM employees WHERE last_name='Shafer'")

# Return the 1st/next row meeting the query as a tuple.
# Return None if no further rows.
cursor.fetchone()

# Returns 1st/next 5 rows in the iterable meeting the query in a list of tuples.
# Return empty list if no more rows meet the query.
cursor.fetchmany(5)

# Return all remaining rows in the iterable from the query, in a list of tuples.
# Return empty list if no more rows meet the query.
cursor.fetchall()

conn.commit()

# Add new employee w/ same last_name, then fetch both via fetchall()
cursor.execute("INSERT INTO employees VALUES ('Mary', 'Shafer', 70000)")
conn.commit()

cursor.execute("SELECT * FROM employees WHERE last_name='Shafer'")
print(cursor.fetchall())  # List of 2 tuples


# +---------------------------------+
# | Insert Employee objects into db |
# +---------------------------------+

emp1 = Employee('John', 'Doe', 80000)
emp2 = Employee('Jane', 'Doe', 90000)

# Inserting via an f-string is vulnerable to SQL injection attack
# cursor.execute(f"INSERT INTO employees VALUES "
#                f"('{emp1.first_name}', '{emp1.last_name}', {emp1.pay})")  # NO

# Insert via using ? as placeholders, and then a tuple as an add'l argument
cursor.execute(f"INSERT INTO employees VALUES (?, ?, ?)",
               (emp1.first_name, emp1.last_name, emp1.pay))  # YES
conn.commit()

# Insert via dictionary of db_column: column_value format
cursor.execute(
    f"INSERT INTO employees VALUES (:first_name, :last_name, :pay)",
    {'first_name': emp2.first_name,
     'last_name': emp2.last_name,
     'pay': emp2.pay}
)  # YES
conn.commit()

# Query db using ? operator
cursor.execute("SELECT * FROM employees WHERE last_name=?",
               ('Shafer',))  # comma in () makes it a tuple
print(cursor.fetchall())

# Query db using dict
cursor.execute("SELECT * FROM employees WHERE last_name=:last_name",
               {'last_name': 'Doe'})
print(cursor.fetchall())
conn.close()


# +-----------------------+
# | Fxns to Manipulate db |
# +-----------------------+

# Using 'with' keyword prevents having to commit each change

# Fxn to insert employee
def insert_emp(emp):
    with conn:
        cursor.execute(
            f"INSERT INTO employees VALUES (:first_name, :last_name, :pay)",
            {'first_name': emp.first_name,
             'last_name': emp.last_name,
             'pay': emp.pay}
        )


# Fxn to get employees by last name. No context manager (with:) needed b/c
# SELECT statements do not require a commit
def get_emps_by_name(lastname):
    cursor.execute("SELECT * FROM employees WHERE last_name=:last_name",
               {'last_name': lastname})
    return cursor.fetchall()


# Fxn to update pay. Requires a commit.
def update_pay(emp, new_pay):
    with conn:
        cursor.execute(
            """UPDATE employees SET pay = :pay
            WHERE first_name=:first_name AND last_name=:last_name""",
            {'first_name': emp.first_name,
             'last_name': emp.last_name,
             'pay': new_pay}
        )


# Fxn to delete employees by name
def remove_emp(emp):
    with conn:
        cursor.execute(
            """DELETE from employees
            WHERE first_name=:first_name AND last_name=:last_name""",
            {'first_name': emp.first_name,
             'last_name': emp.last_name}
        )


# Use temp in-RAM db to try out fxns
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Create the in-RAM db
cursor.execute("""
    CREATE TABLE employees (
        first_name TEXT,
        last_name TEXT,
        pay integer
    )
""")
conn.commit()

# Insert employees 1 & 2
insert_emp(emp1)
insert_emp(emp2)

# Print employees named 'Doe'
doe_emps = get_emps_by_name('Doe')  # List of tuples
print(doe_emps)

# Give John Doe (emp2) a raise to $90,000
update_pay(emp2, 90000)
# Fire Jane Doe (emp1)
remove_emp(emp1)

# Re-print employees named 'Doe'
doe_emps = get_emps_by_name('Doe')  # List of tuples
print(doe_emps)

conn.close()
