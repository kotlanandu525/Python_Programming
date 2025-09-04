n=int(input("enter n="))
def palindrome(n):
   
    for i in range(1,n+1):
        num=i
        rev=0
        while num>0:
            rev=rev+(num%10)**3
            num//=10
        if i==rev:
            print(i,end=" ")
        
        
palindrome(n)
    