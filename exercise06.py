class Mobil():
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

carX = Mobil(300, 18)
print(carX.max_speed, carX.mileage)