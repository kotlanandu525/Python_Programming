num=int(input("enter a numbeer"))
def evaluate(x):
    if(x%2==0):
        return "even"
    else:
        return "odd"
print(evaluate(num))