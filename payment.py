# This script is responsible for generating and populating payment data into a MySQL database.
# It utilizes the faker library to create random payment data for a payment table.

import mysql.connector
from faker import Faker

def generate_payment_data(db):
    """
    Function to generate and populate payment data in the payment table.
    """
    cursor = db.cursor()

    # Create the payment table if it does not exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS payment(
        payment_no INT PRIMARY KEY AUTO_INCREMENT,
        payment_date DATE,
        payment_amount INT NOT NULL,
        loan_number INT,
        FOREIGN KEY (loan_number) REFERENCES loan (loan_number)
    )
    """)
    db.commit()

    # Use the Faker library to generate dummy payment data and insert it into the payment table
    fake = Faker()
    for _ in range(25):
        payment_date = fake.date_between(start_date='-30d', end_date='today')
        payment_amount = fake.random_int(min=100, max=10000)
        loan_number = fake.random_int(min=1, max=25)
        cursor.execute("""
        INSERT INTO payment (payment_date, payment_amount, loan_number)
        VALUES (%s, %s, %s)
        """, (payment_date, payment_amount, loan_number))
    db.commit()

    cursor.close()

    print("payment table populated successfully")
