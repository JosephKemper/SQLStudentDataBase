import sqlite3


def connect_database():
    # Connect to database:
    connection = sqlite3.connect('customer.db')
    # Create a cursor
    cursor = connection.cursor()
    return connection, cursor

# Commit any changes and close connection to database
def close_database(connection):
    connection.commit()
    connection.close()

# Query database and show all records
def show_all():
    connection, cursor = connect_database()

    # Query Data base
    cursor.execute("SELECT rowid, * FROM customers")
    customers = cursor.fetchall()

    for customer in customers:
        print(customer)

    close_database(connection)


# Add a single record to the database
def add_record(first, last, email):
    connection, cursor = connect_database()

    cursor.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))

    close_database(connection)


# Delete a single record from the database
