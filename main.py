import databaseFunctions as functions

def menu():
    while True:
        print("1. Print All Entries in the Database")
        print("2. Add a Single Student")
        print("3. Delete a Single Student")
        print("4. Perform a custom search of the Database")
        print("5. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print('Okay here is the Current Students in the Database')
            functions.show_all()
        elif choice == "2":
            print('Please enter the students information below')
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email Address: ")
            functions.add_student(first_name, last_name, email)
            print(f"We have added {first_name} {last_name} to the database")
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
            print("Exiting the Program")
            break
        else:
            ("Invalid option. Please enter the number of the menu item you wish to select.")