class Car:
    def __init__(self, size="suv", cylinders=8):
        self.size = size
        self.cylinders = cylinders
        self.cylinders_used = cylinders
    
    def drive(self):
        print("is driving")

class Mustang(Car):
    def driving(self):
        self.drive()

    def eco_mode(self):
        print("Eco mode activated")

        self.cylinders_used = self.cylinders/2



