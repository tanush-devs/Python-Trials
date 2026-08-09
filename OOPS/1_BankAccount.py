class BankAccount:
    def __init__(self, name, balance = 0.0):
        self.account_holder = name
        self.balance = balance
        
    def deposit(self, amount):
        if amount < 0:
            print("Cant add negative amount...\nPlease enter a valid amount")
            return
        self.balance += amount
        
    def withdraw(self, amount):
        if amount < 0:
            print("Cant withraw negative amount...\nPlease enter a valid amount")
            return
        elif amount > self.balance:
            print(f"You dont have enough balance\nCurrent balance: '{self.balance}'")
            return
        self.balance -= amount

    def get_balance(self):
        return(self.balance)
    
    def current_status(self):
        print(f"Name : {self.account_holder}")
        print(f"Current balance : {self.balance}")

bk = BankAccount("Tanush")

bk.deposit(-5)
bk.deposit(50.5)
bk.current_status()
bk.withraw(50.5)
bk.withraw(-50)
print(bk.get_balance())
bk.current_status()