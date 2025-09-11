class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print("name=",self.name,"rollno=",self.rollno,"marks=",self.marks)
obj=Student("nandu","5af",66)
obj.display()
obj2=Student("ramesh","5ag",99)
obj2.display()
        