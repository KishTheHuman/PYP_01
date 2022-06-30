# Admin_registration_F

def admin_register():

    Admin_Details = []
    userN = input("Select Username:")
    Admin_Details.append(userN)
    pwd = int(input("Please enter a four digit code"))
    Admin_Details.append(pwd)

    with open("Admin_Logins.txt", "w") as f:
        f.write(userN)
        f.write(",")
        f.write(str(pwd))

# Registered customer mode_Function


def registered_customer_menu():
    print("Welcome registered customer!")
    backtomenu = int(input("\n enter 0 to go back to main menu."))
    if backtomenu == 0:
        Main_Menu()
    else:
        print("Invalid choice please enter 0")

# New Customer mode_Function


def new_customer_menu():
    print("Welcome new customer!")
    backtomenu = int(input("\n enter 0 to go back to main menu."))
    if backtomenu == 0:
        Main_Menu()
    else:
        print("Invalid choice please enter 0")

# Admin mode_Function


def admin_menu():  # Specific Menu for admins to login
    print("Admin Menu.")
    print("\nWelcome Admin! Please register yourself")
    admin_register()

    backtomenu = int(input("\n enter 0 to go back to main menu."))
    if backtomenu == 0:
        Main_Menu()
    else:
        print("Invalid choice please enter 0")

# Main Menu_Function


def Main_Menu():
    print("\nWelcome to System's Menu!")
    print("Please select 1-3 for service mode")
    print("\n1. Admin", "\n2. New Customer", "\n3. Registered Customer")
    print("4. Exit")
    while True:
        try:
            choice = int(input("\nEnter your choice."))
            if choice == 1:
                admin_menu()
                break
            elif choice == 2:
                new_customer_menu()
                break
            elif choice == 3:
                registered_customer_menu()
                break
            elif choice == 4:
                break
            else:
                print("Invalid choice. Enter numbers 0-4 please")
                Main_Menu()
        except ValueError:
            print("Invalid choice. Enter numbers 0-4 please")
    exit


Main_Menu()
