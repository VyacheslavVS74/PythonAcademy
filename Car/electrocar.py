from Car import carclass


class ElectroCar(carclass.CarClass):
    def __init__(self, brand, model, year, prob):
        super().__init__(brand, model, year, prob)
        self.battery = 100

    def description_baattery(self):
        print(f"Этот автомобиль имеет мощность {self.battery}%")
