num1=input("enter a numbeer")
num2=input("enter a numbeer")
num3=input("enter a numbeer")
def evaluate(x,y,z):
    if x>y:
        if x>z:
               return x
        else:
            return z
    else:
        if y>z:
            return y
        else :
            return z
            
     
    
print("greate number",evaluate(num1,num2,num3))