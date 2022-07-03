# ------------------------- Viewing_Medicine_Details_F -------------------------------------------------------

def View_meds():

    with open("Medicine_info.txt", "r") as f:
        f_contents = f.read()
        print(f_contents)

    while True:
        try:
            backtomenu = int(input("\n enter 0 to go back to main menu."))
        except ValueError:
            print("Invalid choice. Enter (0)")
            continue
        else:
            break
    if backtomenu != 0:
        print("Invalid choice. Enter (0)")
    else:
        Main_Menu()
    return


# ------------------------- Adding_Medicine_Details_F ---------------------------------------------------------

def Add_Meds():

    Med_id = (input("\nEnter Medicine ID :"))
    Med_name = (input("\nEnter Medicine Name :"))
    Med_expiry = str(input("\nEnter Med Expiry Date: (DD/MM/YYYY) "))
    Med_price = str(input("Enter Price :"))

    confirm = input("Are you sure? Y/N")

    if(confirm == "Y"):

        with open("Medicine_info.txt", "a") as f:
            f.write("\n")
            f.write(Med_id)
            f.write(" ")
            f.write(Med_name)
            f.write(" ")
            f.write(str(Med_expiry))
            f.write(" ")
            f.write(str(Med_price))  # Write Currency together with PRICE
        admin_inner_menu()
    else:
        admin_inner_menu()


# ------------------------- Admin_Inner_Menu_F --------------------------------------------------------------------

def admin_inner_menu():

    print("\nWelcome to Admin's Menu!")
    print("Please select task 1-6")
    print("\nAdd Medicine Details (1)")
    print("View Medicine Details (2)")
    print("Modify Medicine Details (3)")
    print("Delete Medicine Details (4)")
    print("Search Medicine Details (5)")
    print("View Customer orders (6)")
    print("\nExit to Main Menu (7)")
    while True:
        try:
            choice = int(input("\nEnter your choice."))
            if choice == 1:
                Add_Meds()
                break
            elif choice == 2:
                View_meds()
                break
            elif choice == 3:
                # Update_Med_Detail_F
                break
            elif choice == 4:
                # Delete_Med_Detail_F
                break
            elif choice == 5:
                # Search_Med_Detail_F
                break
            elif choice == 6:
                # View_CustomerOrders_F
                break
            elif choice == 7:
                Main_Menu()
                break
            else:
                print("Invalid choice. Enter numbers 0-7 please")
                break

        except ValueError:
            print("Invalid choice. Enter numbers 0-7 please")
            break
    return
# ------------------------- New_Customer_menu_F -----------------------------------------------------------------


def new_Custo_meu():

    print("What would you like to do?")
    print("\nSelect choice:\nView Available Medicine (1)",
          "\nRegister your details (2)", "\nExit to Main Menu (3)")

    while True:
        try:
            choice = int(input("\nEnter Selection"))
            if choice == 1:
                View_meds()
                break
            elif choice == 2:
                Custo_register()
            elif choice == 3:
                Main_Menu()
                break
            else:
                print("Invalid choice. Enter numbers 1-3.")
                Custo_menu()
                break
        except ValueError:
            print("Invalid choice. Enter numbers 1-3.")
            break

    return

# ------------------------- Customer_register_F ----------------------------------------------------------------


def Custo_register():

    CR_userN = input("\nInput Username:")
    CR_number = str(input("Enter Contact Number:"))
    CR_address = (input("Enter Address"))
    CR_email = input("Input Email:")
    CR_gender = input("Input Gender (M/F)")
    CR_dob = str(input("Date of birth (DD/MM/YYYY):"))

    while True:
        try:
            CR_pwd = str(input("\nPlease input a four digit code:"))
            CR_pwd_check = str(input("\nPlease confirm your four digit code:"))

            if CR_pwd != CR_pwd_check:
                print("Four digit code does not match! Try Again.")
                Custo_register()
                break

            else:
                print("Code Confirmed.")
                break

        except ValueError:
            print("Invalid input enter four digits.")
            break
    backtomenu = int(input("\n enter 0 to save and go back to main menu."))
    confirm = input("Are you sure? Y/N")

    if(confirm == "Y"):

        with open("Cust_details.txt", "a") as f:
            f.write("\n")
            f.write(CR_userN)
            f.write(" ")
            f.write(str(CR_pwd))
            f.write(" ")
            f.write(str(CR_address))
            f.write(" ")
            f.write(str(CR_number))
            f.write(" ")
            f.write(str(CR_email))
            f.write(" ")
            f.write(str(CR_gender))
            f.write(" ")
            f.write(str(CR_dob))
        Custo_menu()
    else:
        Custo_menu()

# ----------------------------------- Customer_menu_Function -----------------------------------------


def Custo_inner_menu():
    print()


# ----------------------------------- Customer_menu_Function ----------------------------------------


def Custo_menu():
    print("\nWelcome to Customer Menu!")
    print("Select Customer Mode.")
    print("\n1. New Customer", "\n2. Registered Customer.",
          "\n3. Exit to Main menu.")

    while True:
        try:
            choice = int(input("\nEnter Selection"))
            if choice == 1:
                new_Custo_meu()
                break
            elif choice == 2:
                Custo_login()
                break
            elif choice == 3:
                Main_Menu()
                break
            else:
                print("Invalid choice. Enter numbers 1-3.")
                Custo_menu()
                break
        except ValueError:
            print("Invalid choice. Enter numbers 1-3.")
            break
    return

# ------------------- Customer_Login_F ----------------------------------------------------------------


def Custo_login():
    file1 = open("Custo_details.txt", "r")
    lines = file1.readlines()
    CL_userN = input("Enter Username: ")
    CL_pwd = input("Enter your four digit code")

    for line in lines:
        [username, pin] = line.split()

        if(CL_userN == username and CL_pwd == pin):
            print("Welcome Back.")
            Custo_menu()
            return

    print("No match found. Try again.")
    Custo_menu()

# ------------------- Admin_Login_F ---------------------------------------------------------------------


def Admin_login():
    file1 = open("Logins.txt", "r")
    lines = file1.readlines()
    AL_userN = input("Enter Username: ")
    AL_pwd = input("Enter your four digit code")

    for line in lines:
        [username, pin] = line.split()

        if(AL_userN == username and AL_pwd == pin):
            print("Login Succesfull.")
            admin_inner_menu()
            return

    print("No match found. Try again.")
    admin_surface_menu()

# ------------------------- Admin_registration_F ---------------------------------------------------------


def admin_register():
    AR_userN = input("\nSelect Username:")
    AR_pwd = str(input("\nPlease enter a four digit code"))
    backtomenu = int(input("\n enter 0 save and go back to main menu."))

    confirm = input("Are you sure? Y/N")

    if(confirm == "Y"):

        with open("Logins.txt", "a") as f:
            f.write("\n")
            f.write(AR_userN)
            f.write(" ")
            f.write(str(AR_pwd))
        Main_Menu()
    else:
        Main_Menu()

# ------------------Registered customer mode_Function-------------------------------------------------------


def registered_customer_menu():
    print("Welcome registered customer!")
    backtomenu = int(input("\n enter 0 to go back to main menu."))
    if backtomenu == 0:
        Main_Menu()

    else:
        print("Invalid choice please enter 0")

# --------------------- New Customer mode_Function ---------------------------------------------------------


def new_customer_menu():
    print("Welcome new customer!")
    backtomenu = int(input("\n enter 0 to go back to main menu."))
    if backtomenu == 0:
        Main_Menu()

    else:
        print("Invalid choice please enter 0")


# ------------------------------- Admin menu_Function -----------------------------------------------------


def admin_surface_menu():  # Specific Menu for admins to login
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
                break
        except ValueError:
            print("Invalid choice. Enter numbers 1-3.")
            break
    return

# ----------------------------------- Main Menu_Function -------------------------------------------------------


def Main_Menu():
    print("\nWelcome to System's Menu!")
    print("Please select 1/2 for service mode")
    print("\n1. Admin", "\n2. Customer")
    print("3. Exit Program")
    while True:
        try:
            choice = int(input("\nEnter your choice."))
            if choice == 1:
                admin_surface_menu()
                break
            elif choice == 2:
                Custo_menu()
                break
            elif choice == 3:
                exit
                break

            else:
                print("Invalid choice. Enter numbers 0-3 please")
                Main_Menu()
                break
        except ValueError:
            print("Invalid choice. Enter numbers 0-3 please")
            break
    exit


Main_Menu()
