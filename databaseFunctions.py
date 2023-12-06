import sqlite3

# This is a decorator function that wraps around other functions to handle database connection and disconnection.
def function_template(function):
    def wrapper(*args, **kwargs):
        # Connect to the SQLite database:
        connection = sqlite3.connect('students.db')
        # Create a cursor object which allows us to execute SQL commands:
        cursor = connection.cursor()

        # Make sure the table exists properly
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                first_name TEXT,
                last_name TEXT,
                email TEXT
            )
        ''')

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
def show_all(cursor, students=None):
    if students is None:
        # If no subset of students is provided, select all students from the database:
        cursor.execute("SELECT rowid, * FROM students")
        students = cursor.fetchall()

    # Print each students record:
    for student in students:
        print(student)

# This function adds a single students record to the database.
@function_template
def add_student(cursor, first, last, email):
    cursor.execute("INSERT INTO students VALUES (?, ?, ?)", (first, last, email))

# This function adds a list of students records to the database.
@function_template
def add_students_list(cursor, list):
    cursor.executemany("INSERT INTO students VALUES (?, ?, ?)", list)

# This function deletes a single students record from the database.
@function_template
def delete_student(cursor, rowid):
    cursor.execute("DELETE from students WHERE rowid = (?)", (rowid,))

# This function looks up students based on a provided column they wish to search and search text, and then prints the found students.
@function_template
def custom_search (cursor, column_name, search_text):
    cursor.execute(f"SELECT * from students WHERE {column_name} = (?)", (search_text,))
    found_students = cursor.fetchall()

    show_all(found_students)

# This function prints the names of all columns in the 'students' table.
@function_template
def print_column_names(cursor):
    cursor.execute("PRAGMA table_info(students)")
    columns = cursor.fetchall()
    for column in columns:
        print(column[1])

# Lookup record by rowid and return as a tuple or none if record does not exist
@function_template
def lookup_by_rowid(cursor, rowid):
    cursor.execute("SELECT first_name, last_name, email FROM students WHERE rowid = ?", (rowid,))
    record = cursor.fetchone()
    return record
