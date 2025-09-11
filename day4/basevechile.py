class vechile:
    def __init__(self,license_plate,owner_name):
        self.__license_plate=license_plate
        self.__owner_name=owner_name
        
    def setlicense_plate(self,num):
        self.__license_plate=num
    def setowner_name(self,name):
        self.__owner_name=name
    def getlicense_plate(self):
        return self.__license_plate
    def getowner_name(self):
        return self.__owner_name
    def display():
        pass
    def calculate_parking_fee():
        pass
    
    
class bike(vechile):
    def __init__(self, license_plate, owner_name,helmet):
        super().__init__(license_plate, owner_name)
        self.helmet=helmet
    def display(self):
        print("platenum=",self.getlicense_plate(),"ownername=",self.getowner_name(),"helmet=",self.helmet)
    def calculate_parking_fee(self,hrs):
        cost=hrs*20
        print("parking cost bike=",cost)
        
    
    
class car(vechile):
    def __init__(self, license_plate, owner_name,seats):
        super().__init__(license_plate, owner_name)
        self.seats=seats
    def display(self):
        print("platenum=",self.getlicense_plate(),"ownername=",self.getowner_name(),"seats=",self.seats)
    def calculate_parking_fee(self,hrs):
        cost=hrs*50
        print("parking cost bike=",cost)
        
class bike(vechile):
    def __init__(self, license_plate, owner_name,load):
        super().__init__(license_plate, owner_name)
        self.load=load
    def display(self):
        print("platenum=",self.getlicense_plate(),"ownername=",self.getowner_name(),"helmet=",self.load)
    def calculate_parking_fee(self,hrs):
        cost=hrs*80
        print("parking cost bike=",cost)
        
class Parkingspot:
    def __init__(self,spotid,size):
        self.__spotid=spotid
        self.__size=size
        def getsize():
            return size
        def getspotid():
            return spotid
        
        
    
        
    
            
    
                