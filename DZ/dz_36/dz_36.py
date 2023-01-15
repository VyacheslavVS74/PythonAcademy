from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def picture(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def area(self):
        sq = self.side ** 2
        return f"Площадь: {sq}"

    def perimeter(self):
        p = self.side * 4
        return f"Периметр: {p}"

    # def picture(self):  # С помощью цикла for --------------
    #     for i in range(self.side - 1):
    #         print("*" * self.side)
    #     print("*" * self.side)

    def picture(self):  # через метод map
        list(map(print, ["*" * self.side] * self.side))

    def info(self):
        return f"===Квадрат===\nСторона: {self.side}\n" \
               f"Цвет: {self.color}\n{self.area()}\n{self.perimeter()}"


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        sq = self.length * self.width
        return f"Площадь: {sq}"

    def perimeter(self):
        p = (self.length * 2) + (self.width * 2)
        return f"Периметр: {p}"

    # def picture(self):  # С помощью цикла for --------------
    #     for i in range(self.length):
    #         for j in range(self.width):
    #             print("*", end="")
    #         print()

    def picture(self):
        list(map(print, ["*" * self.width] * self.length))

    def info(self):
        return f"===прямоугольник===\nДлина: {self.length}\n" \
               f"Ширина: {self.width}\nЦвет: {self.color}\n{self.area()}\n{self.perimeter()}"


class Triangle(Shape):
    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        sq = round((p * (p - self.side1) * (p - self.side2) * (p - self.side3)) ** 0.5, 2)
        return f"Площадь: {sq}"

    def perimeter(self):
        p = self.side1 + self.side2 + self.side3
        return f"Периметр: {p}"

    def picture(self):
        for i in range(self.side2):
            print(" " * (self.side2 - 1 - i) + "*" * (1 + i * 2))

    def info(self):
        return f"===Треугольник===\nСторона: {self.side1}\nСторона: {self.side2}\nСторона: {self.side3}\n" \
               f"Цвет: {self.color}\n{self.area()}\n{self.perimeter()}"


square = Square("red", 3)
rectangle = Rectangle("green", 3, 7)
triangle = Triangle("yellow", 11, 6, 6)
# print(square.info())
# print()
# print(rectangle.info())
# print()
# print(triangle.info())

shape = [square, rectangle, triangle]
for s in shape:
    print(s.info())
    s.picture()  # picture внести в info() не получается, возвращает None из-за print() и фигура сверху отображается
    print()


# s = Square("red", 3)
# s.picture()

# r = Rectangle("green", 3, 7)
# r.picture()

# t = Triangle("yellow", 11, 6, 6)
# print(t.picture())
