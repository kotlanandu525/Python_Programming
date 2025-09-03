num=int(input("enter a numbeer"))
def evaluate(x):
    if(x<0):
        return "negative"
    elif(x>0):
        return "positive"
    else:
        return "zero"
print(evaluate(num))