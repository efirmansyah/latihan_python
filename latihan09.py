class Car:
    def __init__(self, maxSpeed=0, mileage=0):
        self.maxSpeed = maxSpeed
        self.mileage = mileage

    def getMaxSpeed(self):
        return self.maxSpeed

    def getMileage(self):
        return self.mileage

#Second class
class Daihatsu(Car):

    def __init__(self, model=None, color=None):
        self.model = model
        self.color = color

    def getModel(self):
        return self.model

    def getColor(self):
        return self.color


daihat = Daihatsu("Alya", "White")

print(f"Modelnya adalah:", daihat.model )

daihat.maxSpeed = 200

print(daihat.getMaxSpeed())
