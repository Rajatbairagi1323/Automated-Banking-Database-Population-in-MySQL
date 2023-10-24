# This script is responsible for generating and populating employee data into a MySQL database.
# It utilizes the faker library to create random employee data for an employee table.

import mysql.connector
from faker import Faker

def generate_employee_data(db):
    """
    Function to generate and populate employee data in the Employee table.
    """
    cursor = db.cursor()

    # Create the Employee table if it does not exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        emp_id INT PRIMARY KEY AUTO_INCREMENT,
        emp_name VARCHAR(255) NOT NULL,
        contact_info BIGINT NOT NULL,
        start_date DATE,
        cust_id INT,
        FOREIGN KEY (cust_id) REFERENCES customer (cust_id)
    )
    """)
    db.commit()

    # Use the Faker library to generate dummy employee data and insert it into the employee table
    fake = Faker()
    for _ in range(25):
        emp_name = fake.name()
        contact_info = fake.random_int(min=6000000000, max=9999999999)
        start_date = fake.date_between(start_date='-365d', end_date='today')
        cust_id = fake.random_int(min=1, max=25)
        cursor.execute("""
        INSERT INTO employee (emp_name, contact_info, start_date, cust_id)
        VALUES (%s, %s, %s, %s)
        """, (emp_name, contact_info, start_date, cust_id))
    db.commit()

    cursor.close()

    print("employee table populated successfully")
