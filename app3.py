import random
from datetime import datetime
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bank_db"
)

cursor = conn.cursor()

class BankAccount:
    def __init__(self, name, balance=5000):
        self.account_holder = name
        self.balance = balance

        # Generate ATM Card Number
        self.atm_card_number = random.randint(1000000000000000, 9999999999999999)

        # Set ATM PIN
        self.atm_pin = input("Set 4-digit ATM PIN: ")

    # Verify ATM Details
    def verify_atm(self):
        card = input("Enter ATM Card Number: ")
        pin = input("Enter ATM PIN: ")

        if str(self.atm_card_number) == card and self.atm_pin == pin:
            return True
        else:
            print("Invalid ATM Card Number or PIN.")
            return False

    # Print Receipt
    def print_receipt(self, transaction_type, amount):
        print("\n========== TRANSACTION RECEIPT ==========")
        print(f"Date & Time     : {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
        print(f"Account Holder  : {self.account_holder}")
        print(f"ATM Card Number : {self.atm_card_number}")
        print(f"Transaction Type: {transaction_type}")
        print(f"Transaction Amt : ₹{amount}")
        print(f"Available Balance: ₹{self.balance}")
        print("Account Status  : ACTIVE")
        print("=========================================")

    # Deposit Method
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            sql = """
        UPDATE accounts
        SET balance = %s
        WHERE atm_card_number = %s
        """

            values = (self.balance, self.atm_card_number)

            cursor.execute(sql, values)
            conn.commit()
            print(f"\n₹{amount} deposited successfully.")
            self.print_receipt("DEPOSIT", amount)
        else:
            print("Invalid deposit amount.")

    # Withdraw Method
    def withdraw(self, amount):
        if self.verify_atm():

            if amount <= self.balance:
                self.balance -= amount
                sql = """
            UPDATE accounts
            SET balance = %s
            WHERE atm_card_number = %s
            """

            values = (self.balance, self.atm_card_number)

            cursor.execute(sql, values)
            conn.commit()
            print(f"\n₹{amount} withdrawn successfully.")
            self.print_receipt("WITHDRAW", amount)
        else:
            print("Insufficient balance.")

    # Check Balance Method
    def check_balance(self):
        if self.verify_atm():

            print("\n----- Account Details -----")
            print(f"Account Holder : {self.account_holder}")
            print(f"Current Balance: ₹{self.balance}")
            print("----------------------------")


# Main Program
account = None

while True:
    print("\n========== BANK MENU ==========")
    print("1. Create Bank Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Create Account
    if choice == "1":
        if account is None:

            name = input("Enter Account Holder Name: ")
            account = BankAccount(name)

            sql = """
        INSERT INTO accounts
        (account_holder, atm_card_number, atm_pin, balance)
        VALUES (%s, %s, %s, %s)
        """

            values = (
            account.account_holder,
            account.atm_card_number,
            account.atm_pin,
            account.balance
                )

            cursor.execute(sql, values)
            conn.commit()

            print("Account saved to MySQL successfully!")

            print("Account saved to MySQL successfully!")

            print("Bank Account Created Successfully")
            print(f"Welcome {name}")
            print("Initial Balance: ₹5000")
            print(f"Your ATM Card Number: {account.atm_card_number}")

        else:
            print("Account already exists.")

    # Deposit
    elif choice == "2":
        if account:

            try:
               amount = float(input("Enter deposit amount: ₹"))
               account.deposit(amount)

            except ValueError:
             print("Please enter a valid amount.")

        else:
            print("Please create an account first.")

    # Withdraw
    elif choice == "3":
        if account:

             try:
               amount = float(input("Enter withdrawal amount: ₹"))
               account.withdraw(amount)

             except ValueError:
              print("Please enter a valid amount.")


        else:
            print("Please create an account first.")

    # Check Balance
    elif choice == "4":
        if account:

            account.check_balance()

        else:
            print("Please create an account first.")

    # Exit
    elif choice == "5":
        print("\nThank you for using our bank system!")
        break

    else:
        print("Invalid choice. Please try again.")