# ATM Interface in Python

class ATM:
    def __init__(self):
        self.balance = 10000  # Initial balance
        self.pin = "1234"     # Default PIN

    def authenticate(self):
        attempts = 3
        while attempts > 0:
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.pin:
                print("\n✅ Authentication successful.\n")
                return True
            else:
                attempts -= 1
                print(f"❌ Incorrect PIN. {attempts} attempt(s) left.\n")
        print("🔒 Too many incorrect attempts. Exiting.")
        return False

    def show_menu(self):
        print("========= ATM Menu =========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("============================")

    def check_balance(self):
        print(f"💰 Your current balance is ₹{self.balance}\n")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount <= 0:
                print("⚠️ Invalid deposit amount.\n")
            else:
                self.balance += amount
                print(f"✅ ₹{amount} deposited successfully.\n")
        except ValueError:
            print("⚠️ Please enter a valid number.\n")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("⚠️ Invalid withdrawal amount.\n")
            elif amount > self.balance:
                print("❌ Insufficient balance.\n")
            else:
                self.balance -= amount
                print(f"✅ ₹{amount} withdrawn successfully.\n")
        except ValueError:
            print("⚠️ Please enter a valid number.\n")

    def run(self):
        if not self.authenticate():
            return
        while True:
            self.show_menu()
            choice = input("Select an option (1-4): ")
            print()
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print("👋 Thank you for using the ATM. Goodbye!")
                break
            else:
                print("⚠️ Invalid selection. Try again.\n")


# Run the ATM Interface
if __name__ == "__main__":
    atm = ATM()
    atm.run()
# Brainwave-Matrix-Solutions
