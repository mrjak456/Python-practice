# Class creation
# https://www.analyticsvidhya.com/blog/2020/09/object-oriented-programming/s
class Car:
    car_type = "Seadan" # class variable
    def __init__(self,name,mileage):
        self.name = name  # instance variable
        self.mileage = mileage # instance variable

    def description(self):
        return f"The car {self.name} holds a mileage of {self.mileage} km per litre"
    def max_speed(self,speed):
        return f"The car {self.name} holds a maximum speed of {speed} km per hour"

Skoda = Car("Skoda Octavia", 15)
print(Skoda.description())
print(Skoda.max_speed(160))

Audi = Car("Audi A5", 12)
print(Audi.description())
print(Audi.max_speed(170))



    
