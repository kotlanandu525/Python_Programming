a=int(input("enter a"))
b=int(input("enter b"))
a,b=b,a
a=a^b
b=a^b
a=a^b

a=a+b
b=a-b
a=a-b

print("a value=",a)
print("b value=",b)