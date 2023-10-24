# This script is responsible for generating and populating branch data into a MySQL database.
# It utilizes the faker library to create random branch data for a branch table.

import mysql.connector
from faker import Faker

def generate_branch_data(db):
    """
    Function to generate and populate branch data in the branch table.
    """
    cursor = db.cursor()

    # Create the branch table if it does not exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS branch (
        branch_id INT PRIMARY KEY AUTO_INCREMENT,
        city VARCHAR(255) NOT NULL,
        assets VARCHAR(255),
        liabilities VARCHAR(255),
        cust_id INT,
        FOREIGN KEY (cust_id) REFERENCES customer (cust_id)
    )
    """)
    db.commit()

    # Use the Faker library to generate dummy branch data and insert it into the branch table
    fake = Faker()
    for _ in range(25):
        city = fake.city()
        assets = fake.random_int(min=10000, max=1000000)
        liabilities = fake.random_int(min=10000, max=1000000)
        cust_id = fake.random_int(min=1, max=25)
        cursor.execute("""
        INSERT INTO branch (city, assets, liabilities, cust_id)
        VALUES (%s, %s, %s, %s)
        """, (city, assets, liabilities, cust_id))
    db.commit()

    cursor.close()

    print("branch table populated successfully")
