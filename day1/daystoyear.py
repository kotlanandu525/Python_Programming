days=int(input("enter no of days"))
def converter(days):
    rem=days%365
   
    years=days//365
    d=rem%30
    months=rem//30
    return months,years,d
x,y,z=converter(days)
print("months=",round(x,2),"years",round(y,2),"days",z)
