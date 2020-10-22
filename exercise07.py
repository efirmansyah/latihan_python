# 9th Meeting, creating Parent and Child class
# First class
class Motor:
    def __init__(self, maxCC=0, maxSpeed=0):
        self.maxCC = maxCC
        self.maxSpeed = maxSpeed

    def getMaxCC(self):
        return self.maxCC

    def getMaxSpeed(self):
        return self.maxSpeed

# Second class
class Honda(Motor):

    def __init__(self, type=None, gear=None, color=None):
        self.type = type
        self.gear = gear
        self.color = color

    def getType(self):
        return self.type

    def getGear(self):
        return self.gear

    def getColor(self):
        return self.gear


motorhonda =  Honda("Honda", "7", "Red" )

print(f"Merk motornya adalah: {motorhonda.type}")

print(f"Jumlah Gearnya motornya adalah: {motorhonda.gear}")

motorhonda.maxCC = "200km"

print(f"Kecepatannya adalah: ", motorhonda.getMaxCC())

print(f"Warna motornya adalah:", motorhonda.color)

