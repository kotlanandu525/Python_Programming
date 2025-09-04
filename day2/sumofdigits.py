n=int(input("enter n="))
def sumofdigit(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    return sum
print("sum of digits of ",n, "iss",sumofdigit(n))
    