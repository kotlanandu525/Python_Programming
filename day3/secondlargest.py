def func():
    list=[3,4,5,6,7]
    max=list[0]
    for e in list:
        if e>max:
            max1=e
            max2=max
            max=e
    print("second largest=",max2)
func()
         