class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("name=",self.name,"salary=",self.salary)
class Manager(Employee):
    def __init__(self, name, salary,dept):
        super().__init__(name, salary)
        self.dept=dept
       
    def display(self):
        print("name=",self.name,"salary=",self.salary,"dept=",self.dept)
obj1=Employee("rishi",99999999)
obj1.display()
obj2=Manager("ramesh",55555,"mech")
obj2.display()