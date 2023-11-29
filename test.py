import sqlite3

# To store in memory for one time use
#connection = sqlite3.connect(":memory:")

# To store for permanent use
connection = sqlite3.connect("customer.db")

# Create a cursor
my_cursor = connection.cursor()

# Create a table
# Triple quotes lets the table entry be completed over multiple lines. 
#my_cursor.execute("""CREATE TABLE customers (
#                  first_name text,
#                  last_name text,
#                  email text
#                  )
#""")

# For inserting one name into a database
# SQL commands are always in upper case
# my_cursor.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')")
# my_cursor.execute("INSERT INTO customers VALUES ('Joseph', 'Kemper', 'JosephKemper@gmail.com')")

# List of many names
# many_customers = [
#     ('John', 'Doe', 'john.doe@example.com'),
#     ('Jane', 'Doe', 'jane.doe@example.com'),
#     ('Jim', 'Brown', 'jim.brown@example.com'),
#     ('Jill', 'Smith', 'jill.smith@example.com'),
#     ('Jack', 'Johnson', 'jack.johnson@example.com'),
#     ('Julia', 'Davis', 'julia.davis@example.com'),
#     ('Jerry', 'Miller', 'jerry.miller@example.com'),
#     ('Jasmine', 'Wilson', 'jasmine.wilson@example.com'),
#     ('Jake', 'Moore', 'jake.moore@example.com'),
#     ('Joyce', 'Taylor', 'joyce.taylor@example.com'),
#     ('Joe', 'Anderson', 'joe.anderson@example.com'),
#     ('Jenny', 'Thomas', 'jenny.thomas@example.com')
# ]

# To add in many names into a customer list
# my_cursor.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# Query the database
my_cursor.execute("SELECT rowid, * FROM customers")
# my_cursor.fetchone() # Get one from DB
# my_cursor.fetchmany(3) # Get 3 from DB Gets the first 3 entered into the list
customers = my_cursor.fetchall() # Get everything from DB 
# Data can is stored in a tuple inside of a list. 
# Data can be accessed in the same way a list/tuple can

for customer in customers:
    print (f"{customer[0]} {customer[1]} {customer [2]} {customer[3]}")
#    print(customer)

# SQLite data types
# NULL - Does it exist or not
# INTEGER - number
# REAL - decimal
# TEXT - text string
# BLOB - everything else

# Commit our command
connection.commit()

# Close our connection #Best practice
connection.close()

