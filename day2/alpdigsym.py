a=input("enter a character =")
def determine(a):
    if int(a)>=0 and int(a)<=9:
        return "number"
    elif( a>='a' and a<='z')or (a>='A' and a<='Z'):
        return "alphabet"
    else:
        return "symbol"
    
print("you entered a=",determine(a))