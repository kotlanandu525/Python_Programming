def func(k):
    list=[3,4,5,6,7]
    for i in range(k,len(list)):
        list[k]=list[k+1]
    list = list[:-1]
    print(list)
func(3)