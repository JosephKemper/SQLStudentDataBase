import sqlite3

# This is a decorator function that wraps around other functions to handle database connection and disconnection.
def function_template(function):
    def wrapper(*args, **kwargs):
        # Connect to the SQLite database:
        connection = sqlite3.connect('customer.db')
        # Create a cursor object which allows us to execute SQL commands:
        cursor = connection.cursor()

        # Call the function passed to the decorator, passing the cursor and any other arguments it needs:
        result = function(cursor, *args, **kwargs)

        # Commit any changes made during the function call and close the connection to the database:
        connection.commit()
        connection.close()
        
        # Return the result of the function call:
        return result
    
    # Return the new function that includes database connection, function call, and database disconnection:
    return wrapper

# This function queries the database and prints all records, or a provided subset of records.
@function_template
def show_all(cursor, customers=None):
    if customers is None:
        # If no subset of customers is provided, select all customers from the database:
        cursor.execute("SELECT rowid, * FROM customers")
        customers = cursor.fetchall()

    # Print each customer record:
    for customer in customers:
        print(customer)

# This function adds a single customer record to the database.
@function_template
def add_customer(cursor, first, last, email):
    cursor.execute("INSERT INTO customers VALUES (?, ?, ?)", (first, last, email))

# This function adds a list of customer records to the database.
@function_template
def add_customer_list(cursor, list):
    cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", list)

# This function deletes a single customer record from the database.
@function_template
def delete_customer(cursor, rowid):
    cursor.execute("DELETE from customers WHERE rowid = (?)", (rowid,))

# This function looks up customers based on a provided search item and search text, and then prints the found customers.
@function_template
def lookup_customer (cursor, search_item, search_text):
    cursor.execute(f"SELECT * from customers WHERE {search_item} = (?)", (search_text,))
    found_customers = cursor.fetchall()

    show_all(found_customers)

# This function prints the names of all columns in the 'customers' table.
@function_template
def print_column_names(cursor):
    cursor.execute("PRAGMA table_info(customers)")
    columns = cursor.fetchall()
    for column in columns:
        print(column[1])

