lst=[]
def func(name,roll,marks):
   lst.append((name,roll,marks))
    
print("enter name,roll,marks of 5 studs=")   
for i in range(5):
    name=input()
    roll=input()
    marks=int(input())
    func(name,roll,marks)


def greater(list):
    max=list[0][2]
    print("students greater than 75 marks are")
    for l in list:
        if l[2]>75:
            print(l[0])
        if l[2]>max:
            max=l[2]
            name=l[0]
            
    return name
            
print(lst)
print("highest marks for=",greater(lst))

    