class Car:
    def __init__(self):
        self.accelerate=False
        self.brake=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.accelerate=True
        print("Car Starting")

car=Car()
car.start()

del car
print(car)