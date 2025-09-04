m=int(input("enter rows="))
n=int(input("enter cols"))

def pattern(m,n):
    for i in range(1,m+1):
        for j in range(1,n+1):
            print("*",end=" ")
        print()
        
pattern(m,n)