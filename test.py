import sqlite3

# To store in memory for one time use
#connection = sqlite3.connect(":memory:")

# To store for permanent use
connection = sqlite3.connect("customer.db")

