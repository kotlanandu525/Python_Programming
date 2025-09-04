def sumnatural(num):
    sum=0
    for i in range(1,num+1):
        sum+=i
    return sum
n=int(input("enter n="))
print("sum of ",n,"natural nums=",sumnatural(n))    
