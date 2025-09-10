def menu():
    dict={}
    while True:
        print("1.add product:")
        print("2.remove book by id")
        print("3.serach for a product")
        print("4.update title of a book")
        print("5.display all the books")
          
        print("6.count no fo books in library ")
        print("7.book title exist")
        print("8.exit")
        
        opt=int(input("ente option"))
        if opt==8:
            break
        if opt not in range(1,8):
            print("invalid choice")
            continue
        if opt==1:
            print("enter bookid,title=")
            k,v=input().split(" ")
            dict[k]=v
            
        elif opt==2:
            print("enter id=")
            id=input()
            dict.pop(id)
       
        elif opt==3:
            print("enter psearch idt=")
            sid=input()
            if sid in dict.keys():
               print(dict[sid],"found")
        elif opt==4:
            print("enter id,new title of book")
            k,v=input().split(" ")
            dict[k]=v
        elif opt==5:
            print(" all the books in lib")
            for i in dict.values():
                print(i)
        elif opt==6:
            print("total nof books=",len(dict))
          
        else:
           tt=input("enter bookmtiyle")
           if tt in dict.values():
               print("book found")
           else:
               print("not found")
            
menu()