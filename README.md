# Overview

This basic program manages a student database using SQLite. It provides CRUD operations (Create, Read, Update, Delete), custom search, data sorting, and calculates remaining days until graduation. Users interact with the program through a menu-driven interface simplifying student data management. 

My purposes for writing this program were simply to serve as a stating point for learning SQL and get introduced to relational database management. 

[Software Demo Video](https://youtu.be/Yu12rn251CU)

# Relational Database

This program utilizes a relational database with the following characteristics:

Database engine: SQLite

Data model: Relational model

Table structure:
- Table name: students
- Columns
    - rowid: Integer (Primary Key, auto-generated)
    - student_id: String 
    - first_name: String
    - last_name: String
    - email: String
    - enrollment_date: String (YYYY-MM-DD format)
    - estimated_graduation_date: String (YYYY-MM-DD format)

Relationships
- One-to-one relationship between the student ID and the student record.

Data Integrity:
- Primary key constraint on the `rowid` column ensures column ensures unique identification of each record.
- Data type constraints ensure consistency and validity of values

Data manipulation:
- Database functions allow for CRUD operations (Create, Read, Update, Delete) on the student records.
-Custom search functionality enables retrieving data based on specific criteria.
- Data sorting allows ordering students by enrollment date.

# Development Environment

- VS Code version 1.85.0
- Python
- Library random
- Library csv
- Library datetime
- Library sqlite3
- Library csv
- Library datetime

# Useful Websites

- [Wikipedia Relational database Page](https://en.wikipedia.org/wiki/Relational_database)
- [Oracle What is a Relational Database](https://www.oracle.com/database/what-is-a-relational-database/)
- [Ws Schools SQL Tutorial](https://www.w3schools.com/sql/)
- [SQLite Tutorial SQLite Inner Join](https://www.sqlitetutorial.net/sqlite-inner-join/)
- [SQLite Tutorial SQLite Aggregate Functions](https://www.sqlitetutorial.net/sqlite-aggregate-functions/)
- [SQLite Tutorial main page](https://www.sqlitetutorial.net/)
- [SQLite3 Official docs](https://docs.python.org/3.12/library/sqlite3.html)
- [YouTube SQLite in Python || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=c8yHTlrs9EA)
- [O'Reilly Introduction to SQLite Databases for Python Programming](https://learning.oreilly.com/course/introduction-to-sqlite/9781838982867/)


# Future Work

- Input validation: Additional input validation could be implemented for specific data formats, like email addresses and dates.
- User interface: A more user-friendly interface, like a text menu or graphical interface, could be developed for easier interaction with the database.
- Additional functionalities: Additional features like searching by multiple criteria, exporting data to different formats, and implementing user roles could be added.
- Add the ability to choose the name of the database and table you are working with. 
- Add the ability to work with multiple tables (like one for GPA)
- Add the ability to add new columns to the table