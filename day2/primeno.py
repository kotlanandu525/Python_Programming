n=int(input("enter n="))
def prime(n):
    for i in range(2,int(n**0.5)+1):
        if(n%i==0):
            return False
    return True
print(n," is pime no=",prime(n)) 
