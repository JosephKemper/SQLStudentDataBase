import databaseFunctions as functions

def menu():
    while True:
        print()
        print("1. Print All Entries in the Database")
        print("2. Add a Single Student")
        print("3. Delete a Single Student")
        print("4. Perform a custom search of the Database")
        print("5. Add a list of students from a CSV file")
        print("6. Delete all students from database")
        print("7. Modify a single student")
        print("6. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print('Okay here is the Current Students in the Database')
            functions.show_all()

        elif choice == "2":
            print('Please enter the students information below')
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email Address: ")
            if first_name and last_name and email:  # Check if all fields are filled
                functions.add_student(first_name, last_name, email)
                print(f"We have added {first_name} {last_name} to the database")
            else:
                print("All fields must be filled. Please try again.")

        elif choice == "3":
            rowid = input("Please enter the row id of the student you wish to delete")
            record = functions.lookup_by_rowid(rowid)
            if record is not None:
                functions.delete_student(rowid)
            else:
                print("No student found with the given row id.")
            print(f"We have removed {record[0]} {record[1]} from the database")

        elif choice == "4":
            print('The columns in the student database are as follows.')
            functions.print_column_names()
            column_name = input("Please enter the column name you wish to search: ")
            search_text = input("Please enter what you are searching for: ")
            functions.custom_search(column_name, search_text)

        elif choice == "5":
            file_name = input("Please enter the file name you wish to load into the database: ")
            number_students_added = functions.add_students_from_csv_file(file_name)
            print(f"We have added {number_students_added} student/s to the database.")

        elif choice == "6":
            confirm_delete = input("Are you sure you want to delete all students from the database (Y/N?")
            if confirm_delete == "Y" or confirm_delete == "y":
                functions.delete_all_students()
                print("All students have been deleted from the database.")
            else:
                print("Returning to menu.")

        elif choice == "7":
            rowid = input("Please enter the row id of the student you wish to modify")
            first_name = input("New First Name (leave blank to keep the same): ")
            last_name = input("New Last Name (leave blank to keep the same): ")
            email = input("New Email Address (leave blank to keep the same): ")
            functions.modify_student(rowid, first_name or None, last_name or None, email or None)
            print(f"We have updated the student with row id {rowid} in the database")

        elif choice == "8":
            print("Exiting the Program")
            break
        else:
            ("Invalid option. Please enter the number of the menu item you wish to select.")

menu()