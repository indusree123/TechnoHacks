class ATM:
    def __init__(self, balance=0):
        self.balance = balance
    def check_balance(self):
        return self.balance
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount} successfully. New balance: {self.balance}"
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawn {amount} successfully. New balance: {self.balance}"
        else:
            return "Insufficient balance."
def main():
    atm = ATM()
    while True:
        print("ATM Operations")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = int(input("Enter your choice (1, 2, 3, or 4): "))

        if choice == 1:
            balance = atm.check_balance()
            print(f"Your balance is: {balance}")
        elif choice == 2:
            amount = float(input("Enter the amount to deposit: "))
            result = atm.deposit(amount)
            print(result)
        elif choice == 3:
            amount = float(input("Enter the amount to withdraw: "))
            result = atm.withdraw(amount)
            print(result)
        elif choice == 4:
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
main()
