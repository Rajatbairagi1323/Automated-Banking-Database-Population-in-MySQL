# import the required modules
import mysql.connector

# import functions to generate data for tables
from customer import generate_customer_data
from employee import generate_employee_data
from loan import generate_loan_data
from branch import generate_branch_data
from payment import generate_payment_data
from account import generate_account_data

# Function to create and return a database connection
def create_database_connection(host, user, password, database_name):
    """
    Function to create a database connection.
    """
    db = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database_name
    )
    return db

# Function to create database and populate tables
def create_database():
    """
    Function to create a database, populate tables, and establish connections.
    """
    host = input("Enter host name: ")
    user = input("Enter user name: ")
    password = input("Enter password: ")
    database_name = input("Enter database name: ")

    # Create connection and cursor
    db = create_database_connection(host, user, password, "")
    cursor = db.cursor()

    # Drop the database if it exists
    cursor.execute(f"DROP DATABASE IF EXISTS {database_name}")

    # Create a new database
    create_database_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
    cursor.execute(create_database_query)

    print(f"\nDatabase '{database_name}' created successfully.\n")

    # Close the connection to create the new database
    cursor.close()
    db.close()

    # Establish connection to the created database
    db = create_database_connection(host, user, password, database_name)
    cursor = db.cursor()

    # Call other scripts to populate tables
    generate_customer_data(db)
    generate_employee_data(db)
    generate_loan_data(db)
    generate_branch_data(db)
    generate_payment_data(db)
    generate_account_data(db)

    # close the connection
    cursor.close()
    db.close()

# Main function
if __name__ == "__main__":
    create_database()
