# 1 задача-----------------------------------------------------------------------------------------------

# def func(*args):
#     com = 1
#     for i in args:
#         com *= i
#     return com
#
#
# print(func(10, 9))
# print(func(2, 3, 4))
# print(func(3, 5, 10, 6))


# 2 задача--------------------------------------------------------------------------------------------------

# def func(*args):
#     s = 0
#     for i in args:
#         s += i
#         print(s, end=' ')
#     print()
#
#
# func(3, 9, 1)
# func(2, 5, 4, 2)
# func(3, 5, 18, 6, 3)

# не верные-------------------------------
# def func(*args):
#     for i in range(1, len(args)):
#         s = args[i-1] + args[i]
#         return s
#
#
# print(func(3, 9, 1))
# print(func(2, 5, 4, 2))
# print(func(3, 5, 18, 6, 3))


# def print_num(*args):
#     s = 0
#     for i in args:
#         print(args[i - 1] + args[i])
#
#
# print_num(3, 9, 1)
# print_num(2, 5, 4, 2)
# print_num(3, 5, 18, 6, 3)


# 3 задача---------------------------------------------------------------------------------------

# def func(figure_type, **kwargs):
#     if figure_type == 'rhombus':
#         s = (kwargs['d1'] * kwargs['d2']) / 2
#         return s
#     if figure_type == 'square':
#         s = kwargs['a']**2
#         return s
#     if figure_type == 'trapezoid':
#         s = (kwargs['a'] + kwargs['b']) / 2 * 6
#         return s
#     if figure_type == 'circle':
#         import math
#         s = math.pi * (kwargs['r'] ** 2)
#         return s
#     if figure_type == 'unknown':
#         return 'invalid data'
#
#
# print(func(figure_type='rhombus', d1=10, d2=8))
# print(func(figure_type='square', a=5))
# print(func(figure_type='trapezoid', a=12, b=3, h=6))
# print(func(figure_type='circle', r=18))
# print(func(figure_type='unknown', a=1, b=2, c=3))