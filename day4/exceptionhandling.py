try:
    a=int(input("enter a"))
    b=int(input("enter b"))
    res=a/b
    print(res)
except ZeroDivisionError:
    print("error occured")
else:
    print("no error occured")
finally:
    print("this is the final block")
    