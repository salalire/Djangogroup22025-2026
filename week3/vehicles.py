class vehicles:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def printinfo(self):
        print("Brand:",self.brand)
        print("Year:",self.year)

class car(vehicles):
    def __init__(self,brand,year,model):
        super().__init__(brand,year)
        self.model=model
    def printinfo(self):
        print("Brand:",self.brand)
        print("Year:",self.year)
        print("Model:",self.model)
        
        
v1=vehicles("boying",2023)
v1.printinfo()
car1=car("Ferari",1996,"gf123")
car1.printinfo()
 
