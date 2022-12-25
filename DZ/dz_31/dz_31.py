
class Auto:
    def __init__(self, model, year, production, power, color, price):
        self.model = model
        self.production = production
        self.year = year
        self.power = power
        self.color = color
        self.price = price

    @staticmethod
    def verify_model(model):
        if not isinstance(model, str):
            raise TypeError('Название модели должно быть строкой.')

    @staticmethod
    def verify_year(year):
        if not isinstance(year, int) or year < 1860 or year > 2023:
            raise TypeError('Год должен быть числом не меньше 1860 и не больше 2023.')

    @staticmethod
    def verify_production(production):
        if not isinstance(production, str):
            raise TypeError('Производитель должен быть строкой.')

    @staticmethod
    def verify_power(power):
        if not isinstance(power, int):
            raise TypeError('Мощность двигателя должна быть числом.')

    @staticmethod
    def verify_color(color):
        if not isinstance(color, str):
            raise TypeError('Цвет машины должен быть строкой.')

    @staticmethod
    def verify_price(price):
        if not isinstance(price, int):
            raise TypeError('Цена должна быть числом.')

    @property
    def model(self):
        return f'Название модели: {self.__model}'

    @model.setter
    def model(self, model):
        self.verify_model(model)
        self.__model = model

    @property
    def production(self):
        return f'Производитель: {self.__production}'

    @production.setter
    def production(self, production):
        self.verify_production(production)
        self.__production = production

    @property
    def year(self):
        return f'Год выпуска: {self.__year}'

    @year.setter
    def year(self, year):
        self.verify_year(year)
        self.__year = year

    @property
    def power(self):
        return f'Мощность двигателя: {self.__power} л.с.'

    @power.setter
    def power(self, power):
        self.verify_power(power)
        self.__power = power

    @property
    def color(self):
        return f'Цвет машины: {self.__color}'

    @color.setter
    def color(self, color):
        self.verify_color(color)
        self.__color = color

    @property
    def price(self):
        return f'Цена: {self.__price}'

    @price.setter
    def price(self, price):
        self.verify_price(price)
        self.__price = price

    def print_info(self):
        print('*' * 10, 'Данные автомобиля', '*' * 10)
        print(self.model, self.year, self.production, self.power, self.color, self.price, sep='\n')
        print('=' * 40)


a1 = Auto('X7 M50i', 2021, 'BMW', 530, 'white', 10790000)
a1.print_info()

print()
a1.year = 1860  # 2024
print(a1.year)
print()

a1.print_info()
