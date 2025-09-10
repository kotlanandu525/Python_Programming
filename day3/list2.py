def func():
    l=[]
    print("enter nos")
    for i in range(5):
        k=int(input())
        l.append(k)
    print("negative numbers:")
    for ele in l:
        if ele<0:
            print(ele)
func()
    