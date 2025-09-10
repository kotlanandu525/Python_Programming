def func():
    list=[3,4,5,6,7]
    ecnt,ocnt=0,0
    for ele in list:
        
        if ele%2!=0:
            ocnt+=1
        else:
            ecnt+=1
    
    print("odd count=",ocnt)
    print("even count=",ecnt)
func()
         