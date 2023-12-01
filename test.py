import sqlite3

# Wrapper function to use as template for all functions
def function_template(function):
    def wrapper(*args, **kwargs):
        # Connect to database:
        connection = sqlite3.connect('customer.db')
        # Create a cursor
        cursor = connection.cursor()

        result = function(cursor, *args, **kwargs)

        # Commit any changes and close connection to database
        connection.commit()
        connection.close()

# Query database and show all records
@function_template
def show_all(cursor):
    # Query Data base
    cursor.execute("SELECT rowid, * FROM customers")
    customers = cursor.fetchall()

    for customer in customers:
        print(customer)



# Add a single record to the database
@function_template
def add_record(cursor, first, last, email):
    cursor.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))



# Delete a single record from the database
