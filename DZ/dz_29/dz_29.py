
class Formulas:
    count = 0

    @staticmethod
    def f_Gerona(*args):
        Formulas.count += 1
        return sum(args) / 2

    @staticmethod
    def square_triangle(a, b):
        Formulas.count += 1
        return 1 / 2 * (a * b)

    @staticmethod
    def square(a):
        Formulas.count += 1
        return a ** 2

    @staticmethod
    def rectangle(a, b):
        Formulas.count += 1
        return a * b

    def sum(self):
        return Formulas.count


print('Площадь треугольника по формуле Герона:', Formulas.f_Gerona(3, 4, 5))
print('Площадь треугольника через основание и высоту:', Formulas.square_triangle(6, 7))
print('Площадь квадрата:', Formulas.square(7))
print('Площадь прямоугольника:', Formulas.rectangle(2, 6))
print('Количество подсчетов площади:', Formulas.count)
