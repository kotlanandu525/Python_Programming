def func():
    lst=[2,3,4,5,2,3,4]
    dict={}
    for i,val in enumerate(lst):
        if val in dict:
            dict[val]+=1
        else:
            dict[val]=1
    print(dict)
func()