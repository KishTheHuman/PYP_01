# ------------------- Customer_Login_F ----------------------------------


# ------------------- Admin_Login_F ----------------------------------


def Admin_login():
    file1 = open("Logins.txt", "r")
    lines = file1.readlines()
    A_userN = input("Enter Username: ")
    A_pwd = input("Enter your four digit code")

    for line in lines:
        [username, pin] = line.split()

        if(A_userN == username and A_pwd == pin):
            print("Welcome Back.")
            admin_surface_menu()
            return

    print("No match found. Try again.")
    admin_surface_menu()

# ------------------------- Admin_registration_F ---------------------
# /// NOTICE: IT DOES NOT SAVE UNTIL EXITING ENTIRE PROGRAM ///


def admin_register():
    userN = input("\nSelect Username:")
    pwd = int(input("\nPlease enter a four digit code"))
    backtomenu = int(input("\n enter 0 to go back to main menu."))

    confirm = input("Are you sure? Y/N")

    if(confirm == "Y"):

        with open("Logins.txt", "a") as f:
            f.write(userN)
            f.write(" ")
            f.write(str(pwd))
            Main_Menu()
    else:
        Main_Menu()

# ------------------Registered customer mode_Function------------------------


def registered_customer_menu():
    print("Welcome registered customer!")
    backtomenu = int(input("\n enter 0 to go back to main menu."))
    if backtomenu == 0:
        Main_Menu()

    else:
        print("Invalid choice please enter 0")

# --------------------- New Customer mode_Function ----------------------------


def new_customer_menu():
    print("Welcome new customer!")
    backtomenu = int(input("\n enter 0 to go back to main menu."))
    if backtomenu == 0:
        Main_Menu()

    else:
        print("Invalid choice please enter 0")


# ------------------------------- Admin mode_Function ------------------------------------------


def admin_surface_menu():  # Specific Menu for admins to login
    print("\nWelcome to Admin Menu!")
    print("Select Admin Mode.")
    print("\n1. New", "\n2. Registered Admin.", "\n3. Exit to Main menu.")

    while True:
        try:
            choice = int(input("\nEnter Selection"))
            if choice == 1:
                admin_register()
                break
            elif choice == 2:
                Admin_login()
                break
            elif choice == 3:
                Main_Menu()
                break
            else:
                print("Invalid choice. Enter numbers 1-3.")
                admin_surface_menu()
        except ValueError:
            print("Invalid choice. Enter numbers 1-3.")
    exit

# ----------------------------------- Main Menu_Function ---------------------------------------


def Main_Menu():
    print("\nWelcome to System's Menu!")
    print("Please select 1-3 for service mode")
    print("\n1. Admin", "\n2. New Customer", "\n3. Registered Customer")
    print("4. Exit")
    while True:
        try:
            choice = int(input("\nEnter your choice."))
            if choice == 1:
                admin_surface_menu()
                break
            elif choice == 2:
                new_customer_menu()
                break
            elif choice == 3:
                registered_customer_menu()
                break
            elif choice == 4:
                exit
                break
            else:
                print("Invalid choice. Enter numbers 0-4 please")
                Main_Menu()
        except ValueError:
            print("Invalid choice. Enter numbers 0-4 please")
    exit


Main_Menu()
