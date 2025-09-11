from abc import ABC,abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def area(self,l,b):
        return l*b
class Circle(Shape):
    def area(self,r):
        return r*r*3.14

r=Rectangle()
print("area of rectangle=",r.area(5,6))
c=Circle()
print("area of corcle=",c.area(5))