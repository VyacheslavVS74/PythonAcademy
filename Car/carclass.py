class CarClass:
    def __init__(self, brand, model, year, prob):
        self.brand = brand
        self.model = model
        self.year = year
        self.prob = int(prob)

    def show_car(self):
        print(f"{self.brand}, {self.model}, {self.year} год, {self.prob} км")

