num=int(input("enter a numbeer"))
def evaluate(x):
    if(x%5==0 and x%11==0):
        return "divisible by both 5 and 11"
    else:
        return "not divisible"
print(evaluate(num))