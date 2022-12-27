
# from math import pi
#
#
# class Table:
#     def __init__(self, width, length, radius):
#         self.__width = width
#         self.__length = length
#         self.__radius = radius
#
#     def __str__(self):
#         return f'{self.__width}, {self.__length}, {self.__radius}'
#
#     def is_int(self):
#         if self.__radius is None:
#             return False
#         return True
#
#     def rectangle(self):
#         pass
#
#
# class SquareRectangle:
#     def __init__(self, w: Table, lens: Table, r: Table):
#         self._w = w
#         self._lens = lens
#         self._r = r
#
#     def rectangle(self, w, lens, r=None):
#         if r.is_int():
#             self._w = w
#             self._lens = lens
#         else:
#
# # class SquareCircle(Table):
# #     def __init__(self, radius):
# #         self.__radius = radius
# #
# #     def rectangle(self):
# #         return pi * self.__radius ** 2
#
#
# rect = Table(20, 10, 20)
# print(rect.__dict__)
#
# # circle = SquareCircle(20)
# # print(circle.rectangle())

#  # Только без перегрузки вышло(------------------------------------------------------------------
from math import pi


class Table:
    def rectangle(self):
        raise NotImplementedError('В дочернем классе должен быть определен метод rectangle()')


class SquareRectangle(Table):
    def __init__(self, width, length):
        self.__width = width
        self.__length = length

    def rectangle(self):
        return self.__width * self.__length


class SquareCircle(Table):
    def __init__(self, radius):
        self.__radius = radius

    def rectangle(self):
        return pi * self.__radius ** 2


rect = SquareRectangle(20, 10)
print(rect.rectangle())
circle = SquareCircle(20)
print(circle.rectangle())


# # Не вышло--------------------------------------------------------------------------
# class Table:
#     def __init__(self, width, length, radius):
#         self.__width = width
#         self.__length = length
#         self.__radius = radius
#
#     def __str__(self):
#         return f'{self.__width}, {self.__length}'
#
#     def rectangle(self):
#         raise NotImplementedError('В дочернем классе должен быть определен метод rectangle()')
#
#
# class SquareRectangle(Table):
#
#     def rectangle(self, width, length, radius):
#         if self.__radius is None:
#             return self.__width
#
#
# square_rectangle = SquareRectangle(20, 10, 20)
# square_rectangle.rectangle()
# print(Table.__dict__)

#  # Не вышло----------------------------------------------------------------------------------------
# class Table:
#     def __init__(self, width, length, radius):
#         self._width = width
#         self._length = length
#         self._radius = radius
#
#     def __str__(self):
#         return f'{self._width}, {self._length}'
#
#     def rectangle(self):
#         raise NotImplementedError('В дочернем классе должен быть определен метод rectangle()')
#
#
# class SquareRectangle:
#     def __init__(self, rect: Table, radius: int = 1):
#         self._rect = rect
#         self._radius = radius
#
#     def rectangle(self):
#         print(f'{self._rect}, {self._radius}')
