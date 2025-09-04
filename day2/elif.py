weekno=int(input("enter weekno"))
def evaluate(num):
    if(num==1):
        return "Sunday"
    elif num==2:
        return "monday"
    elif num==3:
        return "tuesday"
    elif num==4:
        return "wednesday"
    elif num==5:
        return "thursda"
    elif num==6:
        return "friday"
    elif num==7:
        return "saturday"
    else :
        return "invalid"

res=evaluate(weekno)
print("the day is",)
        