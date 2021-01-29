class Audi:    
    def description(self):
        print("This is the description of Audi")
class BMW:
    def description(self):
        print("This is the description of BMW")
        
audi = Audi()
bmw = BMW()

for car in (audi,bmw):
    car.description()
