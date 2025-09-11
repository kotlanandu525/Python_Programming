class employee:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
class Person(employee):
    def display(self):
        print("name=",self.name,"id=",self.id,"age=",self.age)
obj=Person("nandu","5af",22)
obj.display()