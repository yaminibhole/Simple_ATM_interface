import time

# Initialize user details
user_pin = 77771

user_balance = 97432.50
user_name = "Ms. ABC"

def display_menu():
    print("\t\t0. Logout and Exit")
    print("\t\t1. View Account Balance")
    print("\t\t2. Withdraw Cash")
    print("\t\t3. Deposit Cash")
    print("\t\t4. Change PIN")
    print("\t\t5. Return Card")

def authenticate_user():
    num_of_tries = 3
    while num_of_tries > 0:
        input_pin = int(input("Please enter your 4-digit PIN: "))
        if input_pin == user_pin:
            print("Account authorized!\n\n")
            return True
        else:
            num_of_tries -= 1
            print("PIN incorrect! Number of tries left -", num_of_tries, end="\n\n")

    print("Exiting...")
    time.sleep(2)
    print("You have been logged out. Thank you!\n\n")
    return False

def view_account_balance():
    print("Loading Account Balance...")
    time.sleep(1.5)
    print("Your current balance is Rs.", user_balance, end="\n\n\n")

def withdraw_cash():
    global user_balance  # Declare user_balance as a global variable
    print("Opening Cash Withdrawal...")
    time.sleep(1.5)

    while True:
        withdraw_amt = float(input("Enter the amount you wish to withdraw: "))

        if withdraw_amt > user_balance:
            print("Can't withdraw Rs.", withdraw_amt)
            print("Please enter a lower amount!")
            continue
        else:
            print("Withdrawing Rs.", withdraw_amt)
            confirm = input("Confirm? Y/N: ")
            if confirm in ('Y', 'y'):
                user_balance -= withdraw_amt
                print("Amount withdrawn - Rs.", withdraw_amt)
                print("Remaining balance - Rs.", user_balance, end="\n\n\n")
                break
            else:
                print("Cancelling transaction...")
                time.sleep(1)
                print("Transaction Cancelled!\n\n")
                break

def deposit_cash():
    global user_balance  # Declare user_balance as a global variable
    print("Loading Cash Deposit...")
    time.sleep(1.5)

    deposit_amt = float(input("Enter the amount you wish to deposit: "))
    print("Depositing Rs.", deposit_amt)
    confirm = input("Confirm? Y/N: ")
    if confirm in ('Y', 'y'):
        user_balance += deposit_amt
        print("Amount deposited - Rs.", deposit_amt)
        print("Updated balance - Rs.", user_balance, end="\n\n\n")
    else:
        print("Cancelling transaction...")
        time.sleep(1)
        print("Transaction Cancelled!\n\n")

def change_pin():
    global user_pin  # Declare user_pin as a global variable
    print("Loading PIN Change...")
    time.sleep(1.5)

    pin_new = int(input("Enter your new PIN: "))
    print("Changing PIN to", pin_new)
    confirm = input("Confirm? Y/N: ")
    if confirm in ('Y', 'y'):
        user_pin = pin_new
        print("PIN changed successfully! \n\n")
    else:
        print("Cancelling PIN change...")
        time.sleep(1)
        print("Process Cancelled!\n\n")

def return_card():
    print("Loading Card Return...")
    time.sleep(1.5)

    print("Returning your ATM Card")
    confirm = input("Confirm? Y/N: ")
    if confirm in ('Y', 'y'):
        print("Card returned successfully! \n\n")
    else:
        print("Cancelling process...")
        time.sleep(1)
        print("Process Cancelled!\n\n")

# Main program
print("Welcome to your bank account", user_name, end="\n\n")

while True:
    display_menu()
    choice = int(input("Enter number to proceed: "))
    print("\n\n")

    if choice == 0:
        print("Exiting...")
        time.sleep(2)
        print("You have been logged out. Thank you!\n\n")
        break
    elif choice in (1, 2, 3, 4, 5):
        if authenticate_user():
            if choice == 1:
                view_account_balance()
            elif choice == 2:
                withdraw_cash()
            elif choice == 3:
                deposit_cash()
            elif choice == 4:
                change_pin()
            else:
                return_card()
    else:
        print("Invalid input!")
        print("\t\t0. Enter 0 to Logout and Exit!\n\n")
