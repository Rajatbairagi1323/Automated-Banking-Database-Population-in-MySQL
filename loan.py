# This script is responsible for generating and populating loan data into a MySQL database.
# It utilizes the faker library to create random loan data for a loan table.

import mysql.connector
from faker import Faker

def generate_loan_data(db):
    """
    Function to generate and populate loan data in the loan table.
    """
    cursor = db.cursor()

    # Create the loan table if it does not exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS loan (
        loan_number INT PRIMARY KEY AUTO_INCREMENT,
        loan_amount INT,
        cust_id INT,
        FOREIGN KEY (cust_id) REFERENCES customer (cust_id)
    )
    """)
    db.commit()

    # Use the Faker library to generate dummy loan data and insert it into the loan table
    fake = Faker()
    for _ in range(25):
        loan_amount = fake.random_int(min=1000, max=100000)
        cust_id = fake.random_int(min=1, max=25)
        cursor.execute("""
        INSERT INTO loan (loan_amount, cust_id)
        VALUES (%s, %s)
        """, (loan_amount, cust_id))
    db.commit()

    cursor.close()

    print("loan table populated successfully")
