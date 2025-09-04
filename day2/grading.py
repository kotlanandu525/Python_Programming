mark=int(input("enter marks of student"))
def evaluate(num):
    if num>40:
        if(num>80):
            return "distinction"
        elif num>70:
            return "A"
        elif num>50:
            return "B"
        else:
            return "c"
    else:
        return "fail"
        
    
    

res=evaluate(mark)
print("the result is",res)
        