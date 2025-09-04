cname=input("enter name:")
cno=input("enter rollno")
lmr=int(input("enter last month reading"))
pmr=int(input("enter present month reading"))
units=pmr-lmr
def currentbill(no):
    if(no>300):
        return (no-300)*7.80 + 100*6.3 +100*5.1 + 50*4.2 + 50*3.8
    elif no>200:
        return (no-200)*6.3  +100*5.1 + 50*4.2 + 50*3.8
    elif no>100:
        return (no-100)*5.1 + 50*4.2 + 50*3.8
    elif no>50:
        return (no-50)*4.2 + 50*3.8
    else:
        return no*3.8
    
res=currentbill(units)
print("his month current bill is=",res)
    