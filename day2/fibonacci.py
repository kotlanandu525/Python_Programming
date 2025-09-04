n=int(input("enter n="))
def fibonacci(n):
    ft=0
    st=1
    print(ft,st,end=" ")
    for i in range(2,n+1):
        tt=ft+st
        print(tt,end=" ")
        ft=st
        st=tt
        
fibonacci(n)