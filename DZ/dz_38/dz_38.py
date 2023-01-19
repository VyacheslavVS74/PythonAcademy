

class Integer:
    @staticmethod
    def verify(number):
        if not isinstance(number, int) or number < 0:
            raise ValueError(f'Сторона {number} должна быть положительным целым числом')

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        # return getattr(instance, owner)  # таким способом выдает ошибку: maximum recursion depth exceeded
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.verify(value)
        # setattr(instance, self.name, value)  # таким способом выдает ошибку: maximum recursion depth exceeded
        instance.__dict__[self.name] = value


class Triangle:
    a = Integer()
    b = Integer()
    c = Integer()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def existence(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return f'Треугольник со сторонами ({self.a}, {self.b}, {self.c}) существует.'
        else:
            return f'Треугольник со сторонами ({self.a}, {self.b}, {self.c}) не существует.'


t1 = Triangle(2, 5, 6)
t2 = Triangle(5, 2, 8)
t3 = Triangle(7, 3, 6)

# print(t1.existence())

shape = [t1, t2, t3]

for i in shape:
    print(i.existence())
