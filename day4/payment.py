class Payment:
    def pay(self,amount):
        pass
class CashPayment(Payment):
    def pay(self,amount):
        print("you paid $",amount,"cash")
class CardPayment(Payment):
    def pay(self,amount):
        print("you paid $",amount,"cash through card")
class UPIPayment(Payment):
    def pay(self,amount):
        print("you paid $",amount,"cash through UPI")

p=[CashPayment(),CardPayment(),UPIPayment()]
for o in p:
    o.pay(10000)