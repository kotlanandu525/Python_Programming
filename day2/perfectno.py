n=int(input("enter n="))
def perfect(n):
   
    for i in range(1,n+1):
        num=i
        sum=0
        for j in range(1,(i//2)+1):
           if i%j==0:
               sum=sum+j
        if(num==sum):
            print(i,end=" ")
            
perfect(n)
        
               
           

    