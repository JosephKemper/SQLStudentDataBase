import sqlite3
import csv

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
                student_id INTEGER,
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
def add_student(cursor, student_id, first, last, email):
    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)", (student_id, first, last, email))

# This function adds a list of students records pulled from a file to the database.
@function_template
def add_students_from_csv_file(cursor, csv_filename):
    try:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_headers = next(csv_reader)
            if csv_headers != ['student_id', 'first_name', 'last_name', 'email']:
                print("Invalid file format. The file must have a header row with 'student_id', 'first_name', 'last_name', and 'email'.")
                return
            student_data = list(csv_reader)
        cursor.executemany("INSERT INTO students VALUES (?, ?, ?, ?)", student_data)
        return len(student_data)
    except FileNotFoundError:
        print(f"File not found: {csv_filename}")
    except csv.Error as csv_error:
        print(f"Error reading file: {csv_error}")
    except Exception as unexpected_error:
        print(f"Unexpected error: {unexpected_error}")

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

@function_template
def delete_all_students(cursor):
    cursor.execute("DELETE FROM students")

@function_template
def modify_student(cursor, rowid, first=None, last=None, email=None):
    # Check which fields are provided and build the SQL command accordingly
    sql_command = "UPDATE students SET "
    parameters = []
    if first is not None:
        sql_command += "first_name = ?, "
        parameters.append(first)
    if last is not None:
        sql_command += "last_name = ?, "
        parameters.append(last)
    if email is not None:
        sql_command += "email = ?, "
        parameters.append(email)
    # Remove the last comma and space
    sql_command = sql_command[:-2]
    # Add the WHERE clause
    sql_command += " WHERE rowid = ?"
    parameters.append(rowid)
    # Execute the SQL command
    cursor.execute(sql_command, parameters)