#https://www.analyticsvidhya.com/blog/2020/09/object-oriented-programming

class Car:
    def __init__(self,name,mileage):
        self.__name = name
        self.mileage = mileage

        
    def description(self):
        return f"The car {self.name} holds the mileage of {self.mileage} km per litre"

    def max_speed(self,speed):
        return f"The car {self.name} holds a speed of {speed} km per hour"

class BMW(Car):
    def bmw_color(self,color):
        return f"The car {self.name} is in {color} color"

'''obj1 = BMW("BMW 7 series",14)
print(obj1.description())
print(obj1.max_speed(150))
print(obj1.bmw_color("black"))
'''
obj2 = Car("Audi Q7 series", 12)
#print(obj2.__name)
print(obj2._Car__name)







    
