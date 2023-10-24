# This script is responsible for generating and populating customer data into a MySQL database.
# It utilizes the faker library to create random customer data for a customer table.

import mysql.connector
from faker import Faker

def generate_customer_data(db):
    """
    Function to generate and populate customer data in the customer table.
    """
    cursor = db.cursor()

    # Create the customer table if it does not exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customer(
        Cust_id INT PRIMARY KEY AUTO_INCREMENT,
        dob DATE,
        name VARCHAR(255),
        age INT,
        address VARCHAR(255) NOT NULL,
        contact_info BIGINT
    )
    """)
    db.commit()

    # Use the Faker library to generate dummy customer data and insert it into the customer table
    fake = Faker()
    for _ in range(25):
        dob = fake.date_of_birth()
        name = fake.name()
        age = fake.random_int(min=18, max=60)
        address = fake.address()
        contact_info = fake.random_int(min=6000000000, max=9999999999)
        cursor.execute("""
        INSERT INTO customer (dob, name, age, address, contact_info)
        VALUES (%s, %s, %s, %s, %s)
        """, (dob, name, age, address, contact_info))
    db.commit()

    cursor.close()

    print("customer table populated successfully")
