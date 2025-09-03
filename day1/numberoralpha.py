let=input("enter")
def evaluate(x):
    if(x.isalpha()):
        return "alphabet"
    elif x.isdigit():
        return "number"
    else:
        return "symbol#"
    
print(evaluate(let))