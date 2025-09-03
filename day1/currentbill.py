cname=input("enter name:")
cno=input("enter rollno")
lmr=int(input("enter last month reading"))
pmr=int(input("enter present month reading"))
cost=float(input("enter cost per unit="))
units=pmr-lmr
cb=units*cost
print("customer name=",cname,"customer no=",cno)
print("total bill per this month",cb)