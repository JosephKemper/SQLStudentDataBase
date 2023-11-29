import sqlite3

# To store in memory for one time use
#connection = sqlite3.connect(":memory:")

# To store for permanent use
connection = sqlite3.connect("customer.db")

# Create a cursor
my_cursor = connection.cursor()

# Create a table
# Triple quotes lets the table entry be completed over multiple lines. 
my_cursor.execute("""CREATE TABLE customers (
                  first_name text,
                  last_name text,
                  email text
                  )
""")

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

