import time
import random
from datetime import datetime

class ATM:
    def __init__(self, card_number, name, pin, mobile_number, balance=0):
        self.card_number = card_number
        self.name = name
        self.pin = pin
        self.mobile_number = mobile_number
        self.balance = balance
        self.transaction_history = []
        self.attempts_left = 3
        self.otp = None

    def log_transaction(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append(f"{message} at {timestamp}")
        self.send_notification(message)

    def send_notification(self, message):
        print(f"\n📲 SMS to {self.mobile_number}: {message}. Current balance: ${self.balance:.2f}")

    def send_otp(self):
        self.otp = str(random.randint(100000, 999999))
        print(f"\n🔐 Sending OTP to your registered mobile: {self.mobile_number}")
        print(f"(For testing, OTP is: {self.otp})")  # In real app, OTP would be sent via SMS

    def verify_otp(self):
        entered_otp = input("Enter the OTP: ")
        if entered_otp == self.otp:
            print("✅ OTP Verified.")
            return True
        else:
            print("❌ Incorrect OTP. Access denied.")
            return False

    def check_pin(self):
        while self.attempts_left > 0:
            entered_pin = input("Enter your PIN: ")
            if entered_pin == self.pin:
                self.send_otp()
                return self.verify_otp()
            else:
                self.attempts_left -= 1
                print(f"Incorrect PIN. Attempts left: {self.attempts_left}")
        print("❌ Account locked due to too many failed attempts.")
        return False

    def check_balance(self):
        print(f"\nHello {self.name}")
        print(f"Card: **** **** **** {self.card_number[-4:]}")
        print(f"Your current balance is: ${self.balance:.2f}")
        self.log_transaction("Checked balance")

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                self.balance += amount
                print(f"✅ Deposited ${amount:.2f}")
                self.log_transaction(f"Deposited ${amount:.2f}")
            else:
                print("❌ Invalid deposit amount.")
        except ValueError:
            print("❌ Invalid input. Enter a number.")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"✅ Withdrew ${amount:.2f}")
                self.log_transaction(f"Withdrew ${amount:.2f}")
            else:
                print("❌ Invalid amount or insufficient funds.")
        except ValueError:
            print("❌ Invalid input. Enter a number.")

    def change_pin(self):
        new_pin = input("Enter new PIN: ")
        confirm_pin = input("Confirm new PIN: ")
        if new_pin == confirm_pin:
            self.pin = new_pin
            print("✅ PIN successfully changed.")
            self.log_transaction("Changed PIN")
        else:
            print("❌ PINs do not match.")

    def show_transaction_history(self, count=5):
        print("\n📄 Last Transactions:")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for txn in self.transaction_history[-count:]:
                print(f"- {txn}")

    def run(self):
        if not self.check_pin():
            return

        print(f"\n👋 Welcome {self.name}!")

        while True:
            print("\n📋 ATM Menu:")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Change PIN")
            print("5. Transaction History")
            print("6. Exit")

            choice = input("Select an option: ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                amount = input("Enter amount to deposit: ")
                self.deposit(amount)
            elif choice == "3":
                amount = input("Enter amount to withdraw: ")
                self.withdraw(amount)
            elif choice == "4":
                self.change_pin()
            elif choice == "5":
                self.show_transaction_history()
            elif choice == "6":
                print("👋 Session ended. Thank you for using the ATM!")
                break
            else:
                print("❌ Invalid option. Please try again.")

            time.sleep(1)  # simulate slight delay


# === Run the ATM Program ===
if __name__ == "__main__":
    user_atm = ATM(
        card_number="1234567890123456",
        name="Swathi",
        pin="1234",
        mobile_number="+91-9876543210",
        balance=2000
    )
    user_atm.run()
