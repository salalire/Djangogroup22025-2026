
class BankAccount:
    def init(self, initial_balance=0):
        self.__balance = initial_balance   

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.__balance:
            print("Insufficient balance! Withdrawal denied.")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")

    def get_balance(self):
        return self.__balance

account = BankAccount(100)

account.deposit(50)      
account.withdraw(30)      
account.withdraw(200)     
print("Final Balance:", account.get_balance())
