
class vehicle :

    def __init__(self,brand,model,year,speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def ass(self):
        print(self.speed)

    def beake(self):
        print(self.model)

    def honk(self):
        print(self.year)

class child(vehicle):
    
    def ass(self):
        print(self.speed)
    
    def honk(self):
        print(self.year)

obj1 = vehicle("HP",2018,2024,200)
obj2 = child("HP",2018,2024,200)
obj2.ass()
obj2.beake()
obj2.honk()

