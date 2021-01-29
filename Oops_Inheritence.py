class Car:
    car_type = "Seadon"
    def __init__(self,name,mileage):
        self.name = name
        self.mileage = mileage

    def description(self):
        return f'The Car {self.name} has the mileage of {self.mileage} per litre'

    def max_speed(self,speed):
        return f'The Car {self.name} has the maximum speed of {speed} per km'

    
car1 = Car("BMW",12)
print(car1.car_type)
print(car1.description())
print(car1.max_speed(200))

class Audi(Car):
    car_color = "Blue"

    def self_description(self,model):
        return f"The Car {self.name} is the {model} car"

car2 = Audi("Q7 Series", 14)
print(car2.car_type)
print(car2.description())
print(car2.max_speed(250))
print(car2.self_description("Latest"))




      
