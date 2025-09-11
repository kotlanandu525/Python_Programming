class BankAccount:
    def __init__(self):
        self.__balance=0
    def deposit(self,amount):
        print(amount,"amount deposited ")
        self.__balance+=amount
    def withdraw(self,amount):
        if self.__balance-amount<0:
            print("insufficient balance")
        else:
            print(amount,"amount debited ")
            self.__balance-=amount
    def getbalance(self):
        return self.__balance
obj=BankAccount()
print("balance",obj.getbalance())
obj.deposit(5000)
print("balance",obj.getbalance())
obj.withdraw(6000)
print("balance",obj.getbalance())
    
        