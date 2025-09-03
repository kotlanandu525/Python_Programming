num=int(input("enter a numbeer"))
def evaluate(x):
    if((x%4==0 and x%100!=0) or x%400==0):
        return "leap year"
    else:
        return "not a leap year"
print(evaluate(num))