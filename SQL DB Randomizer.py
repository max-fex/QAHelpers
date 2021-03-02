###############################################################
# Creation of pseudo random SQL database for testing purposes #
###############################################################

import random as r
import sqlite3


first_name = ['John', 'Alice', 'Todd', 'Kenny', 'Sam', 'Max', 'Martin']
last_name = ['Smith', 'Hamprshire', 'O', 'Roonie', 'Moore']
gender = ['M', 'F', 'U']
grades = ['Trainee', 'Junior', 'Middle', 'Senior', 'Architect']

create_table_employee = "CREATE TABLE employees (" \
                    "ID INTEGER PRIMARY KEY, " \
                    "Name VARCHAR(20) NOT NULL, " \
                    "Gender CHAR (1), " \
                    "Speciality INT(2) NOT NULL, " \
                    "Grade VARCHAR(6))"

number_of_records = 200

def db_randomizer():
    random_name = str(first_name[r.randrange(len(first_name))] + " " + last_name[r.randrange(len(last_name))])
    random_gender = str(gender[r.randrange(len(gender))])
    random_specialty = str(r.randint(1, 6))
    random_grade = str(grades[r.randrange(len(grades))])
    fill_in_table_employee = "INSERT INTO employees (Name, Gender, Speciality, Grade) " \
                         "VALUES ('" + random_name + "', '" + random_gender + "', '" + random_specialty + "', '" + random_grade + "')"
    return fill_in_table_employee

connection = sqlite3.connect("my_db.db")
c = connection.cursor()

c.execute(create_table_employee)
for i in range (number_of_records):
    c.execute(db_randomizer())

select_employee_sqllite3_object = c.execute("SELECT * FROM employees")

select_employee_string = select_employee_sqllite3_object.fetchall()
for k in range(len(select_employee_string)):
    print(select_employee_string[k])

"""c.execute("DELETE FROM employees")
"""

"""l = (c.execute("SELECT Name FROM employees WHERE Gender = 'M'"))

l_n = []
for element in l:
    l_n.append(element.replace("('", "").replace("',)"))

counter = 0
popular_name = ""
"""

connection.commit()
connection.close()
