n=int(input("enter n="))
def palindrome(n):
   
    for i in range(1,n+1):
        num=i
        rev=0
        while num>0:
            rev=rev+(facto(num%10))
            num//=10
        if i==rev:
            print(i,end=" ")
def facto(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
        
palindrome(n)
    