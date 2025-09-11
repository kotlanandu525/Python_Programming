class Student:
    def __init__(self,name,rollno,marks):
        self.__name=name
        self.__rollno=rollno
        self.__marks=marks
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def getroll(self):
        return self.__rollno
obj=Student("nandu","ggaa",88)
obj.setname("naveen")
print(obj.getname())
print(obj.getroll())
    