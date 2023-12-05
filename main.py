import databaseFunctions

def menu():
    while True:
        print("1.")
        print("2.")
        print("3.")
        print(".")
        print("x. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print('')
        elif choice == "2":
            print('')
        elif choice == "x":
            print("Exiting the Program")
            break
        else:
            ("Invalid option. Please enter the number of the menu item you wish to select.")