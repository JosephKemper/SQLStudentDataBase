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
        print("8. Print Student Database by enrollment date")
        print("9. Calculate days until estimated graduation for student")
        print("10. Quit")
        print()

        choice = input("Enter your choice: ")
        print()
        if choice == "1":
            print('Okay here is the Current Students in the Database')
            functions.show_all()

        elif choice == "2":
            print('Please enter the students information below')
            student_id = input("10 digit student id: ")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email Address: ")
            enrollment_date = input("Enrollment Date (YYYY-MM-DD): ")
            estimated_graduation = input("Estimated Graduation (YYYY-MM-DD): ")
            if first_name and last_name and email:  # Check if all fields are filled
                functions.add_student(student_id, first_name, last_name, email, enrollment_date, estimated_graduation)
                print(f"We have added {first_name} {last_name} to the database")
            else:
                print("All fields must be filled. Please try again.")

        elif choice == "3":
            student_id = input("Please enter the student id of the student you wish to delete: ")
            record = functions.lookup_by_student_id(student_id)
            if record is not None:
                functions.delete_student(student_id)
            else:
                print("No student found with the given student id.")
            print(f"We have removed {record[1]} {record[2]} from the database")

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
            confirm_delete = input("Are you sure you want to delete all students from the database (Y/N)? ")
            if confirm_delete == "Y" or confirm_delete == "y":
                functions.delete_all_students()
                print("All students have been deleted from the database.")
            else:
                print("Ok. No changes were made. Returning to menu.")

        elif choice == "7":
            student_id = input("Please enter the student id of the student you wish to modify: ")
            first_name = input("New First Name (leave blank to keep the same): ")
            last_name = input("New Last Name (leave blank to keep the same): ")
            email = input("New Email Address (leave blank to keep the same): ")
            enrollment_date = input("New Enrollment Date (leave blank to keep the same): ")
            estimated_graduation_date = input("New Estimated Graduation Date (leave blank to keep the same): ")
            functions.modify_student(student_id, first_name or None, last_name or None, email or None, enrollment_date or None, estimated_graduation_date or None)
            print(f"We have updated the student with student id {student_id} in the database")

        elif choice == "8":
            print("Here is the current students in the database listed by order they enrolled")
            functions.print_by_enrollment_date()

        elif choice == "9":
            student_id = input("Enter the student id of the student you wish to calculate the days remaining until estimated graduation for: ")
            days_remaining = functions.calculate_days_until_graduation(student_id)
            record = functions.lookup_by_student_id(student_id)
            print(f"{record[1]} {record[2]} has {days_remaining} day/s remaining until his/her estimated graduation date.")

        elif choice == "10":
            print("Exiting the Program")
            break
        else:
            ("Invalid option. Please enter the number of the menu item you wish to select.")

menu()