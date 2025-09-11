class Bank:
    def __init__(self,balance):
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    
    def getbalance(self):
        return self.__balance
obj=Bank(5000)
obj.deposit(1000)
print("balance",obj.getbalance())
    
        