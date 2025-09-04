m=int(input("enter rows="))
n=int(input("enter cols=5"))

def pattern(m,n):
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(i==j ):
                print("$",end="")
            else:
                print("*",end=" ")
        print()
        
pattern(m,n)