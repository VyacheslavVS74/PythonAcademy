class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_info(self):
        print(f'Длина прямоугольника: {self.a}\nШирина прямоугольника: {self.b}')

    def square(self):
        print('Площадь прямоугольника:', self.a * self.b)

    def perimeter(self):
        print('Периметр прямоугольника:', 2 * (self.a + self.b))

    def hypotenuse(self):
        print('Гипотенуза прямоугольника:', round((self.a ** 2 + self.b ** 2) ** 0.5, 2))

    def picture(self):
        for i in range(self.a):
            for j in range(self.b):
                print('*', end='')
            print()

    def set_a(self, a):
        if isinstance(a, int):
            self.a = a

    def set_b(self, b):
        if isinstance(b, int):
            self.b = b

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b


print('=' * 40)
p1 = Rectangle(3, 24)
p1.print_info()
p1.square()
p1.perimeter()
p1.hypotenuse()
p1.picture()

# print('=' * 40)
# p1.set_a('2')
# p1.print_info()
# p1.square()
# p1.perimeter()
# p1.hypotenuse()
# p1.picture()
