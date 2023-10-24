# This script is responsible for generating and populating account data into a MySQL database.
# It utilizes the faker library to create random account data for an account table.

import mysql.connector
from faker import Faker

def generate_account_data(db):
    """
    Function to generate and populate account data in the account table.
    """
    cursor = db.cursor()

    # Create the account table if it does not exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS account(
        account_number INT PRIMARY KEY AUTO_INCREMENT,
        account_balance INT,
        cust_id INT,
        FOREIGN KEY (cust_id) REFERENCES customer (cust_id)
    )
    """)
    db.commit()

    # Use the Faker library to generate dummy account data and insert it into the account table
    fake = Faker()
    for _ in range(25):
        account_balance = fake.random_int(min=1000, max=100000)
        cust_id = fake.random_int(min=1, max=25)
        cursor.execute("""
        INSERT INTO account (account_balance, cust_id)
        VALUES (%s, %s)
        """, (account_balance, cust_id))
    db.commit()

    cursor.close()

    print("account table populated successfully")
