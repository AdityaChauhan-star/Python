#Task 3 : ATM simulator

# Create a program that simulates the all atmfunctionalities and operations
# (Check balance,Deposit, Withdraw).

class ATM:
    def __init__(self):
        self.balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False


def main():
    atm = ATM()

    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            print(f"Current Balance: ${atm.check_balance()}")

        elif choice == "2":
            try:
                amount = float(input("Enter the amount to deposit: "))
                if atm.deposit(amount):
                    print(f"Deposit successful. Current Balance: ${atm.check_balance()}")
                else:
                    print("Invalid deposit amount. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        elif choice == "3":
            try:
                amount = float(input("Enter the amount to withdraw: "))
                if atm.withdraw(amount):
                    print(f"Withdrawal successful. Current Balance: ${atm.check_balance()}")
                else:
                    print("Insufficient funds or invalid withdrawal amount.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        elif choice == "4":
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
