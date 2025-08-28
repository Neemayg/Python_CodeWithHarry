def calculate_salary():
    print("Welcome to the Salary Calculator")
    print("1. Calculate salary for a permanent employee")
    print("2. Calculate salary for a temporary employee")
    choice = input("Enter your choice: ")

    if choice == '1':
        salary = 30000
        print(f"The monthly salary for a permanent employee is: Rs. {salary}")
    elif choice == '2':
        working_days = int(input("Enter number of working days: "))
        daily_rate = 200
        salary = working_days * daily_rate
        print(f"The salary for the temporary employee for {working_days} days is: Rs. {salary}")
    else:
        print("Invalid choice. Please try again.")

def main():
    username = "admin"
    password = "123"

    print("--- Admin Login ---")
    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")

    if entered_username == username and entered_password == password:
        logged_in = True
        while logged_in:
            print("\n--- Admin Menu ---")
            print("1. Calculate Salary")
            print("2. Logout")
            admin_choice = input("Enter your choice: ")

            if admin_choice == '1':
                calculate_salary()
            elif admin_choice == '2':
                print("Logging out...")
                logged_in = False
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Invalid credentials. Please try again.")

if __name__ == "__main__":
    main()