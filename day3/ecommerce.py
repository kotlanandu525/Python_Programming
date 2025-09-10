def menu():
    lst=[]
    while True:
        print("1.add product:")
        print("2.remove product")
        print("3.serach for a product")
        print("4.display all products")
        print("5.cnt of total no of products")
          
        print("6.sort the carrt ")
        print("7.clear the cart")
        print("8.exit")
        
        opt=int(input("ente option"))
        if opt==8:
            break
        if opt not in range(1,8):
            print("invalid choice")
            continue
        if opt==1:
            print("enter product=")
            item=input()
            lst.append(item)
        elif opt==2:
            print("enter product=")
            item=input()
            lst.remove(item)
        elif opt==3:
            print("enter product=")
            item=input()
            if item in lst:
               print(item,"found")
        elif opt==4:
            print(lst)
        elif opt==6:
            print(" sorted the card=",sorted(lst))
        elif opt==5:
            print("total nof products=",len(lst))
          
        else:
            print("clearing the cart",lst.clear())
            
menu()