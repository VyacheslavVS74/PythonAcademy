# from random import *


# name = "Elena"
# print("Hello!!!", name)
# age = 20
# print(age)
# print(type(name))
# print(type(age))
# a = 4
# b = 5
# print(a)
# a = b
# print(id(a))  # id
# print(id(b))


# a = b = c = 1
# print(a, b, c)
# print(b)

# a, b, c = 5, "Hello", 9.2
# print(a, b ,c)

# name_new = "Bob"
# print(name_new)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = "Hello"
# print(type(a))
# a = 3
# print(type(a))

# name = "Elena"
# age = 20
# print("Меня зовут: " + name + ". Мне " + str(age) + " лет")
# print("Меня зовут: ", name, ". Мне ", age, " лет")

# a = 1
# b = 2
# print("a: ", a)
# print("b: ", b)
# # c = a
# # a = b
# # b = c
# a, b = b, a
# print("a: ", a)  # 2
# print("b: ", b)  # 1

# print("строка "
#       "символов")
# print('строка '
#       'символов')
# print("строка \
# символов")

# print("Документ \"script\" находится \rпо заданному пути \n\tD:\\\Python\\prog")

# s1 = 'Hello'
# s2 = 'Python'
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3 * 3)  # только на целые умножать
# print("*" * 40)

# print(23453425243542365264654)
# print(2.3453425243542365264654)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)  # 3.0
# print(7 / 2)  # 3.5
# print(6 // 2)  # 3.0
# print(7 // 2)  # 3.0
# print(7 % 2)
# print(7 ** 2)

# 08/09/2022====================================================================================================

# number = (6 + 4) * (5 ** 2 + 7)
# print(number)  #113

# num = 10
# num += 5  # num = num + 5
# print(num)

# num = 4321
# a = num % 10
# # print(a)
# num = num // 10
# # print(num)
# b = num % 10
# # print(b)
# num = num // 10
# # print(num)
# c = num % 10
# # print(c)
# num = num // 10
# # print(num)
# d = num % 10
# # print(d)
# e = a*1000 + b*100 + c*10 + d
# print(e)

# num1 = 4321
# print(num1)
# res = (num1 % 10) * 1000
# num1 = num1 // 10
# res += (num1 % 10) * 100
# num1 = num1 // 10
# res += (num1 % 10) * 10
# num1 = num1 // 10
# res += (num1 % 10)
# print(res)

# int() - преобразовывает к целочисленному типу данных
# float() - преобразует к вещественному типу данных
# str() - преобразует к строковому типу данных
# bool() - преобразует к булеву типу данных

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)
#
# print(int(3.8))
# print(round(3.82))
# print(round(3.896, 2))

# a = 5 / 3
# print(round(a, 2))

# a = '5.2'
# b = 10
# c = float(a) + b
# d = round(c)
# print(d)

# a = 1
# b = 2
# print("a: ", a, "\nb: ", b)
# print("a: ", a)
# print("b: ", b)

# name = "Виктор"
# age = 28
# print("Меня зовут ", name, ". Мне ", age, " лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", age, " лет.", sep="---", end="\n\n")
# print("Я учу Python.")

# print("*** Ваши данные ***")
# name = input("Ваше имя: ")
# sity = input("Ваш город: ")
# print(name, sity)

# Число 5 в степени 2 равно: 25
# one = input("Введите число: ")
# two = input("Введите степень: ")
# one = int(one)
# two = int(two)
# sum = one ** two
# free = int(one) ** int(two)
# print("Число ", one, " в степени ", two, " равно ", sum)

# a = input("Введите число: ")
# b = input("Введите степень: ")
# print("Число ", a, " в степени ", b, " равно ", int(a) ** int(b), sep="")

# a = input("Введите первое число: ")
# b = input("Введите второе число: ")
# c = input("Введите третье число: ")
# d = input("Введите четвертое число: ")
# # sum = int(a) + int(b)
# # sum2 = int(c) + int(d)
# print('Результат:', round(((a+b)/(c+d)),2))

# print("Введите четыре числа: ")
# a = int(input("1: "))
# b = int(input("2: "))
# c = int(input("3: "))
# d = int(input("4: "))
# sum1 = a + b
# sum2 = c + d
# del1 = sum1 / sum2
# print("Результат:", round(del1, 2))

# a = True
# b = False
# print(a + 5)  # 1 + 5
# print(b * 5)  # 0 * 5

# # False = "", 0, False, None
# print(bool("python"))  # True
# print(bool(""))  # False
# print(bool(" "))  # True
# print(bool(0))  # False
# print(bool(5))  # True
# print(bool(0.5))  # True
# print(bool(False))  # False
# print(bool(None))  # False

# test = None
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(2 + 5 != 7)
# print(8 > 7)
# print(8 < 7)
# print(8 <= 8)
# print("привет" <= "Привет")
# print("привет" > "Привет")

# print(2 < 4 < 9)
# print(2 * 5 > 7 >= 4 + 3)
# print(3 * 3 <= 7 >= 2)

# a = 10
# b = 5
# c = a == b
# print(a, b, c) # 10, 5, False

# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True : False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False : True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False : False)

# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # False (True : False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False : True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False : False)

# print(not 9 - 7)
# print(not 7 - 7)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

# a = 35
# b = 25
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("b == a")

# print("** Введите стороны треугольника **")
# a = int(input("1: "))
# b = int(input("2: "))
# c = int(input("3: "))
# if a == b and a == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or b == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# m = int(input("Введите номер месяца: "))
# # if (m >= 1) and m < 12:
# if 1 <= m <= 12:
#     if m == 1 or m == 2 or m ==12:
#         print("Зима")
#     if m == 3 or m == 4 or m ==5:
#         print("Весна")
#     if m == 6 or m == 7 or m ==8:
#         print("Лето")
#     if m == 9 or m == 10 or m ==10:
#         print("Осень")
# else:
#     print("Ошибка ввода данных")

# num = int(input('Введите номер месяца: '))
# if num > 0 and num < 13:
#     if 1 <= num <= 2 or num == 12:
#         print('Зима')
#     elif 3 <= num <= 5:
#         print('Весна')
#     elif 6 <= num <= 8:
#         print('Лето')
#     else:
#         print('Осень')
# else:
#     print('Введите корректное число')


# 13.09.22=================================================================================================

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # day >= 1 and day <= 5
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понидельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресение")
# else:
#     print("Такого дня недели не существует!")

# n = int(input("Ведите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ", end="")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "Вороны")
#     else:
#         print(n, "ворон")
#     # if n == 1:
#     #     print(n, "ворона")
#     # if 2 <= n <= 4:
#     #     print(n, "Вороны")
#     # if 5 <= n <= 9 or n == 0:
#     #     print(n, " ворон")
# else:
#     print("Ошибка ввода данных!")

# a = int(input("Введите число от 1 до 99: "))
# kop = a
# # if 11 <= kop <= 14:
# #     print(a, "копеек")
# # else:
# #     kop = kop % 10
# #     if kop == 1:
# #         print(a, "копейка")
# #     elif 2 <= kop <= 4:
# #         print(a, "копейки")
# #     else:
# #         print(a, "копеек")
# if 11 <= kop <= 14:
#     print(a, "копеек")
# elif 1 <= kop <= 10 or 15 <= kop <= 99:
#     kop = kop % 10
#     if kop == 1:
#         print(a, "копейка")
#     elif 2 <= kop <= 4:
#         print(a, "копейки")
#     else:
#         print(a, "копеек")
# else:
#     print("нукорректный ввод данных")

# Тернарное выражение

# a, b = 30, 20
# minim =a if a < b else b
# print(minim)

# a, b = 50, 30
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# if a == b:
#     print("a == b")
# else:
#     if a > b:
#         print("a > b")
#     else:
#         print("b > a")


# a, b = 2, 0
# print("На ноль делить нельзя" if b == 0 else a / b)


# num = int(input('Введите делимое: '))
# num2 = int(input('Введите делитель: '))
# print(num / num2 if num2 != 0 else 'На ноль делить нельзя')

# Исключения

# print("Код далее")
# a = 5
# b = 0
# print(a/b)
# print("Код далее")

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("что то пошло не так")
# print("Код далее")

# try:
#     n = int(input("введите делимое: "))
#     m = int(input("введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("нельзя вводить строки")
# except ZeroDivisionError:
#     print("нельзя делить на ноль")

# try:
#     n = int(input("введите делимое: "))
#     m = int(input("введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("нельзя вводить строки")
#     print("нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключения
#     print("все норм", n, "и", m)
# finally:  # выполняется в любом случае
#     print("конец программы")

# a = input("a:")  # "9"
# b = input("b:")  # "a"
# try:
#     a = int(a)  # 9
#     b = int(b)  # "a" !!!
# except ValueError:
#     a = str(a)
#     # b = str(b)  # можно не указывать
# finally:
#     print(a + b)  # 9 + "a"

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1  # i = i + 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1  # i = i + 1


# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print('i =', i)
#     i += 1

# i = 0  # 1 - нечетные
# while i < 20:
#     i += 2
#     print('i =', i)

# n = int(input("укажите кол-во символов: "))  # 7
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("укажите кол-во символов: "))  # 7
# while n > 0:
#     print("*", end="")
#     n -= 1

# n = int(input('Введите количество символов: '))
# print('*'*n)  # но только в строку

# 15.09.22===================================================================================================

# n = input("введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое")
#         n = input("введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while True:  # i < 10
#     if i == 3:
#         i += 1  # без увеличения на 1 цикл будет по кругу будет сравнивать 3
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     # print(i, end=" ")
#     i += 1
# print("\nЦикл завершен")

# while True:
#     n = int(input("Введите положительное число: "))
#     if n > 0:
#         break

# res = 1
# while True:
#     n = int(input("a"))
#     if n == 0:
#         break
#     res *= n
# print(res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i = ", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i = ", i)
#     j = 1
#     while j < 4:
#         print("\tВложенный цикл: j = ", j)
#         j += 1
#     i += 1


# посмотреть в Debug

# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(i, "*", j, "=", i*j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print('^', end='')
#         j += 1
#     print()
#     i += 1

# i = 1
# while i <= 5:
#     j = 0
#     while j < 20:
#         if i % 2 != 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1

# for element in collection:
#     print(element)

# for i in "Hello!":
#     print(i)

# i = 1
# for color in "red", "orange", "yellow", 2, 0.3:
#     print(i, "color:", color, type(color))
#     i += 1
#
# for i in range(n):
# #  Тело цикла

# range(start, stop, step)

# for i in range(9):
#     print(i, end=" ")

# for i in range(2, 9):
#     print(i, end=" ")

# for i in range(2, 9, 3):
#     print(i, end=" ")
# print()
# j = 2
# while j < 9:
#     print(j, end=" ")
#     j += 3

# for i in range(9, 0, -1):
#     print(i, end=" ")
# print()
# j = 9
# while j > 0:
#     print(j, end=" ")
#     j -= 1

# a = int(input("Введите целое число: "))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")
# print()
# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")


# for i in range(0, 3):
#     print(i)
#     if i == 1:
#         break  # без брейка елс сработает
# else:
#     print("done")

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# a = int(input("Введите длину прямоугольника: "))
# b = int(input("Введите высоту прямоугольника: "))
# for i in range(b):
#     for j in range(a):
#         print('*',end='')
#     print()

# n = int(input("Введите длину прямоугольника"))
# m = int(input("Введите высота прямоугольника"))
# # for i in range(m):
# #     for j in range(n):
# #
# #         print('*', end='')
# #     print()
# for i in range(m):
#     print('*'*n)


# a = int(input("высота прямоугольника"))
# b = int(input("Ширина прямоугольника"))
# for i in range(a):
#     print()
#     for j in range(b):
#         if 0 < i < a - 1 and 0 < j < b - 1:
#             print(" ", end="")
#         else:
#             print("*", end="")

# a = int(input("высота прямоугольника"))
# b = int(input("Ширина прямоугольника"))
# for i in range(a):
#     for j in range(b):
#         if i == 0 or j == 0 or i == a-1 or j == b-1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()


# 20.09.2022 =========================================================================================

# a = 2
# b = 15
# res = 0
# i = a
# while i <= b:
#     if i % 2:
#         print(i, end=" ")
#         res += a
#     i += 1
# print("\n", res)

# a = 2
# b = 15
# res = 0
# # if a > b:
# #     a, b = b, a
# a, b = (a, b) if a < b else (b, a)
# while a <= b:
#     if a % 2:
#         res += a
#     a += 1
# print(res)
# # else:
# #     while b <= a:
# #         if b % 2:
# #             res += b
# #         b += 1
# #     print(res)

# n = int(input('Введите начало диапазона (включительно): '))
# m = int(input('Введите конец диапазона (включительно): '))
# start = n if n < m else m
# finish = m if n < m else n
# count = 0
# while start <= finish:
#     count += start if start % 2 != 0 else 0
#     start += 1
# print('Сумма целых нечетных чисел:', count)

# a = [letter * 2 for letter in "Hello"]
# print(a)
#
# for i in " Hello":
#     print(i * 2, end=" ")

# num = [i for i in range(0, 30) if i % 2 == 0]
# print(num)
#
# print([i for i in range(0, 30) if i % 2 == 0])

# Списки list()-------------------------------------------------------------------------------------------------

# num = [8, 3, "one", 3.2, (1, 2, 3)]
# print(num)
# print(type(num))
# print(num[1])
# print(num[4][1])
# print(num[-1][1])
# print(num[-2])
# # print(num[-6])
# num[2] = 256
# print(num)
# num[1] += 100
# num[-1] = 2
# print(num)

# num = [8, 3, "one", 3.2, (1, 2, 3)]
# print("Длина списка: ", len(num))

# s = []
# print(type(s))
# b = list("Hello")  # ["Hello", "world"]
# # print(type(b))
# print(b)

# s = [5, 1] * 6
# print(s)

# n = list(range(2, 10, 2))
# print(n)
# n2 = [2, 4, 6, 8]
# print(n2)
# if n is n2:  #  ==
#     print("списки равны")
# else:
#     print("Списки разные")

# [выражение for переменная счетчик in последовательность]

# n = 5
# a = [i ** 2 for i in range(1, n+1)]
# print(a)

# a = [1, 2, 3]
# b = [5, 6]
# c = a + b
# print(c)
# d = c * 2
# print(d)

# a = [0] * int(input("Введите кол-во элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [input("->") for i in range(int(input("Кол-во элементов:")))]
# print(a)

# a = [4, 8, 9, 3, 2]
# for i in range(len(a)):  # i -индексы
#     print(a[i], end=" ")
# print()
# for elem in a:  # elem - элементы списка
#     print(elem, end=" ")

# lst = ["один", "два", "три"]
# for elem in lst:
#     print(elem * 2, end=" ")
# print()
# for i in range(len(lst)):
#     print(lst[i] * 2, end=" ")


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# a = [int(input('-> '))for i in range(int(input('Введите количество элементов: ')))]
# summa = 0
# for i in a:
#     summa += i if i<0 else 0
# print('Сумма отрицательных элементов:', summa)

# sum1 = 0
# a = [0] * int(input("Введите количество элементов списка: "))
# for i in range(len(a)):
#     a[i] = int(input("-> "))
#     if a[i] < 0:
#         sum1 += a[i]
# print(sum1)

# count = 0
# lst = [int(input('=> ')) for _ in range(int(input('Введите количетсов элементов ')))]
# for i in lst:
#     if i < 0:
#         count += i
# print('сумма отрицательных элементов ' + count)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# n = list(range(21,41))
# print(n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 ==0:
#         k += 1
#     else:
#         s += n[i]
# print("Кол-во четных: ", k)
# print("Сумма нечетных: ", s)

# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in n:
#     if i % 2:
#         s += i
#     else:
#         k += 1
# print("количество четных : ", k)
# print("сумма нечетных", s)

# lst = [int(input('=> ')) for _ in range(int(input('n: ')))]
# res = sum1 = 0
# for i in lst:
#     if i != 0:
#         sum1 += i
#         if i !=0:
#             res += 1
#
# print('среднее ', sum1/res)

# a = [int(input('-> '))for i in range(int(input('Введите количество элементов: ')))]
# count = 0
# summa = 0
# for i in a:
#     summa += i
#     count += 1 if i != 0 else 0
# print('Среднее арифметическое: ', summa/count)

# n = 5
# zero_elem = 0
# sum = 0
# lst = [int(input('-Ю')) for _ in range(n)]
# for i in lst:
#     if i == 0:
#         zero_elem += 1
#     sum += i
# print('Среднее арифметическое - ', sum / (n - zero_elem))

# a = [int(input('-> ')) for i in range(int(input('Введите количество элементов: ')))]
# # for i in range(len(a)):
# #     if i % 2 == 0:
# #         print(a[i], end=' ')
#
# for i in range(0, len(a), 2):
#     print(a[i], end=' ')

# a = [7, 8, 2, 1, 17]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)


# 22.09.2022 ========================================================================================================
# size = int(input("Введите размер поля: "))
# symbol = int(input("Введите количество символов: "))
# for i in range(size):
#     for j in range(symbol):
#         for n in range(size):
#             for m in range(symbol):
#                 # print(" " if (i + n) % 2 else "*", end="")
#                 if (i + n) % 2 == 0:
#                     print("*", end="")
#                 else:
#                     print(" ", end="")
#         print()

# for i in range(5):
#     for n in range(5):
#         if (i + n) % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#     print()
# ----------------------------------------------------------------------------------

# Срезы   5я папка

# список [start:stop:step]

# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4])  # до 4го индекса
# print(s[2:])
# print(s[:2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[-2:2:-1])
# print(s[1:4:-1])
# print(s[10:20])

# a = [1, 2, 3, 4, 5, 6, 7]
# print(a[:])
# print(a[::-1])
# print(a[::2])
# print(a[1::2])
# print(a[:1])
# print(a[-1:])
# print(a[3:4])
# print(a[4:])
# print(a[4:1:-1])
# print(a[-3:1:-1])
# print(a[2:5])

# a[1:3] = [0, 0, 0, 0]
# print(a)#
# a[1:2] = [20]
# print(a)#
# a[3] = [30]
# print(a)

# Методы списков
# s = [1, 20, 0, 30, 4, 5, 6, 7]
# print(s)
# s.append(99)  # добавляет один элемент в конец списка
# print(s)
# s.extend([9, 8, 7])  # добавляет множество элементов в конец списка
# print(s)
# s.extend("add")
# print(s)
# s.insert(1, 100)  # добавляет заданное значение (второй параметр) по указанному индексу
# print(s)


# s = []
# for i in range(1, 11):
#     s.extend([i**2])
# print(s)

# lst = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # lst.append(x)
#     # lst.extend([x])
#     lst.insert(-1, x)
#     print(lst)  # [2, 3, 1]

# a = int(input("Кол-во элементов списка: "))
# for i in range(a):
#     if a % 3 !== 0:
#         print(a, "не делится на 3")
#     else:
#         lst

# n = int(input('Введите количество элементов списка: '))
# i = 0
# lst = []
# while i < n:
#     x = int(input('Ввведите число кратное 3: '))
#     if x % 3 != 0:
#         print(x, 'число не делится на 3 без остатка')
#     else:
#         lst.append(x)
#     i += 1
# print(lst)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [5, 9, 4, 5, 6, 5, 4]
# b = [5, 6, 78, 45, 2, 4]
# c = []
# for i in a:
#     for j in b:
#         if i == j:
#             if not i in c:
#                 c.append(i)
# print(c)

# a = [1, 2, 3, 4, 2]
# b = [11, 22, 33]
# c = []
# print("a =", a)
# print("b =", b)
# if len(b) > len(a):
#     for i in range(int(len(a))):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # range(3, 5)
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(b[i])
#         c.append(a[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print("c =", c)

# s = [1, 20, 0, 30, 4, 5, 6, 7, 0, 2]
# # s[4:] = []
# # s[2:6] = []
# # print(s)
# if 0 in s:
#     s.remove(0)  # удаляет элемент по Значению, первое совпадение
# print(s)
# last = s.pop()  # удаляет последний элемент из списка, и возвращает удаляемый элемент
# print(last)
# print(s)
# second = s.pop(0)  # Удаляет элемент по индексу
# print(second)
# print(s)
# # s.clear()  # очищает список
# # del s[:]
# del s[2]
# print(s)

# s = []
# [s.append(int(input('-> '))) for i in range(int(input('Введите количество элементов: ')))]
# # s = [(int(input('-> '))) for i in range(int(input('Введите количество элементов: ')))]
# k = int(input("Введите индекс: "))
# # del s[k]
# s.pop(k)
# print(s)

# n = int(input("Кол элементов списка"))
# s = []
# for i in range(n):
#     x = int(input("-->"))
#     s.append(x)
# c = int(input("ВВЕДИТЕ иддекс"))
# s.pop(c)
# print(s)

# DZ ??????????????????????????????????????????????????????????????????????????????
# 23:25


# 27.09.2022======================================================================================

# Задача № 3
# sp = [int(input('=>')) for i in range(int(input('Введите кол-во значений: ')))]
# x = int(input('Введите число:'))
# for i in range(len(sp)):
#     if x == sp[i]:
#         print('Это число есть в списке')
#         break
# else:
#     print("No")

# print(dir(list))

# s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 0, 2]
# num = s.count(5)  # считает количество заданных значений (5) в списке
# print(num)
# ind = s.index(0, 6, -1)  # возвращает положение первого индекса с заданным значением
# print(ind)

# a = [1, 2, 3]
# b = a
# s_copy = a.copy()  # возвращает копию списка расположенную по другому адресу
# a.append(20)
# b.append(4)
# s_copy.append(444)
# print("a", a)
# print("b", b)
# print("s_copy", s_copy)
# print(id(a))
# print(id(b))
# print(id(s_copy))

# s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 0, 2]
# s1 = ["b", "a", "c"]
# s.reverse()  # возвращает None, переставляет элементы списка в обратном порядке
# print(s)
# s.sort(reverse=True)  # reverse=True - используется для сортировки по убыванию
# # s1.sort()
# # print(s1)
# print(s)
# s2 = ["Виталий", "Сергей", "Александр", "Анна"]
# s2.sort(key=len)
# print(s2)
# srt = sorted(s)  # создает дубликат списка и сортирует именно дубликат
# print(sorted(s))
# print(srt)
# print(s)
# print(id(s))
# print(id(srt))

# Генерация случайных данных--------------------------------------------------------------------------------

# import random as r  # первый способ вызова модуля
# from random import randint, randrange  # второй способ  # * после import будет доставать все модули из random
# print(r.random())
# print(randint(2, 9))  # от 2 по 9 включительно
# print(randrange(0, 10, 2))  # от 0 до 10, 10 не считается, можно поставить 11 либо 10+1


# from random import *
# print(randint(2, 9))  # от 2 по 9 включительно
# print(randrange(1, 10, 3))
# print(round(uniform(10.5, 25.5), 2))  # round округление
#
# s = [55, 66, 77, 88, 99, 20, 30, 80, 90]
# print(choice(s))  # вывод одного элемента рандомно
# print(choices(s, k=3))  # вывод нескольких указанных элементов рандомно
#
# shuffle(s)  # рандомно меняет список, перемешивает
# print(s)

# from random import *
# mas = [randint(-10, 20) for i in range(10)]
# print(mas)

# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(sum(lst))  # только с числовыми значениями
# print(min(lst))  # можно и со строками по алфавиту
# print(max(lst))  # можно и со строками по алфавиту

# задачки 5 папка------------------------------------------------------------------------------------------

# from random import *
# lst = [randint(0,100) for i in range(10)]
# print(lst)
# l = lst.pop(lst.index(max(lst)))
# lst.insert(0, l)
# print(lst)

# from random import *
# lst = [randint(0, 100) for i in range(10)]
# max_ = max(lst)
# print(lst)
# print(max_)
# lst.remove(max_)
# lst.insert(0, max_)
# print(lst)

# from random import *
# lst = [randint(-20, 20) for i in range(10)]
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# from random import *
# lst = [randint(-20, 20) for i in range(10)]
# print(lst)
# m = min(lst)
# print(m)

# from random import *
# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# m = min(lst)
# print('Min:', m)
# l = lst.index(m)
# print('index min:', l)
# # lst[:l] = []
# del lst[:l]
# print(lst)

# x = list('1a3fdsfg')
# print(x)
# print('a' in x)
# print('e' in x)
# print('a' not in x)
# print('e' not in x)

# lst = [1]
# # if len(lst) == 0:
# print(bool(lst))
# if not lst:
#     print('список пустой')

# from random import *
# n1 = int(input('Введите размер первого списка:'))
# n2 = int(input('Введите размер второго списка:'))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print('первый список', a)
# print('второй список', b)
# c = a + b
# print('третий список', c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print('Элементы обоих списков без повторений', c)
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print('общие элементы двух списков', c)
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# from random import *
# n1 = int(input('Введите размер первого списка: '))
# n2 = int(input('Введите размер второго списка: '))
# lst1 = [randint(0, 10) for i in range(n1)]
# lst2 = [randint(0, 10) for j in range(n2)]
# print('Первый список:', lst1)
# print("Второй список:", lst2)
# lst3 = lst1 + lst2
# print("Третий список:", lst3)
# lst4 = []
# for i in lst3:
#     if i not in lst4:
#         lst4.append(i)
# print("Элементы обоих списков без повторений:", lst4)
# lst5 = []
# for i in lst1:
#     for j in lst2:
#         if i == j:
#             lst5.append(i)
# print("Список, содержащий элементы общие для двух списков:", lst5)
# lst6 = [min(lst1), min(lst2), max(lst1), max(lst2)]
# print("Содержащий только минимальное и максимальное значение каждого из списков:", lst6)

# from random import *
# k = int(input("размер списка "))  # 6
# s = []
# while len(s) < k:
#     n = randint(1, k)  # с 1 по 6
#     if n not in s:
#         s.append(n)
# print(s)

# from random import *
# n = int(input('Введите число: '))
# s = [i for i in range(1, n+1)]
# shuffle(s)
# print(s)

# 29.09.2022=================================================================================

# m = [
#     [1, 2, 3, 4],  # 0
#     [5, 6, 7, 8],  # 1
#     [9, 10, 11, 12]  # 2
# ]
# print(m)
# print(m[1][2])
#
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col]**2, end="\t")
#     print()

# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x**2, end="\t")
#     print()

# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
#
# q = [[x**2 for x in row] for row in m]
# for row in q:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# a = 5
# b = 3
# q = [[0 for range(b) in row] for row in range(a)]
# for row in q:
#     for b in row:

# n, m = int(input('Введите высоту матрицы: ')), int(input('Введите ширину матрицы: '))
# matr = [[0 for i in range(m)] for j in range(n)]
# # print(matr)
# for row in matr:
#     for x in row:
#         print(x, end='\t')
#     print()

# a = [1, 2], [3, 4], [5, 6], [7, 8]  # [1,2,3] - x,y,z
# for x, y in a:
#     print(x, "+", y, "=", x + y)

# from random import *
# w, h = 5, 4
# matrix = [[randint(1,30) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# from random import *
# w, h = 3, 4
# matrix = [[randint(-20,10) for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#         if x < 0:
#
#     print()

# from random import *
# w, h = 3, 4
# matrix = [[randint(-20, 10) for i in range(w)] for j in range(h)]
# count = 0
# for row in matrix:
#     for x in row:
#         if x <0:
#             count +=1
#         print(x, end='\t')
#     print()
# print('Количество отрицательных элементов: ', count)

# from random import *
# w, h = 3, 4
# matrix = [[randint(0, 4) for i in range(w)] for j in range(h)]
# pro = 1
# for row in matrix:
#     for x in row:
#         if x != 0:
#             pro *= x
#         print(x, end='\t')
#     print()
# print('Произведение не нулевых элементов: ', pro)

# from random import *
# w, h = 6, 6
# matrix = [[randint(0, 10) for i in range(w)] for j in range(h)]
#
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()
# print()
#
# for row in range(len(matrix)):
#     if row % 2 == 0:
#         for col in range(len(matrix[row])):
#             print(matrix[row+1][col], end="\t")
#         print()
#         for col in range(len(matrix[row])):
#             print(matrix[row][col], end="\t")
#         print()

# from random import *
# w, h = 6, 6  # int(input("Число значений в строке"))
# matrix = [[random.randint(0, 10) for i in range(w)] for j in range(h)]
# print(matrix)
# for i in range(0, 6, 2):
#     print(i)
#     matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]
# print(matrix)

# import math
# # print(dir(math))
# num1 = math.sqrt(2)
# print(num1)
# num2 = math.ceil(3.2)
# print(num2)
# num3 = math.floor(3.8)
# print(num3)
# print(math.pi)
# print(math.tau)  # два Пи
#
# radius = 2
# print('Площадь окружности с радиусом', radius, '->', math.pi * (radius ** 2))
# radius = 9
# print(round(2 * math.pi * radius, 2))

# import time

# second = time.time()
# print('секунды с начала эпохи:', second)
# localtime = time.ctime()
# print(localtime)
# res = time.localtime(second)
# print(res)
# print(res.tm_year)
# print(time.strftime('Today is %B %d, %Y'))
# print(time.strftime('%m/%d/%Y, %H:%M:%S', time.localtime(756565654)))

# pause = 5
# print('program started...')
# time.sleep(pause)
# print(pause, 'seconds.')

# text = input('название напоминания: ')
# local_time = float(input('через сколько минут напомнить: '))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.time()
# time.sleep(4)
# finish = time.time()
# res = finish - start
# print(res)

# start = time.monotonic()
# time.sleep()
# finish = time.monotonic()
# res = finish - start
# print(res)

# import locale
# locale.setlocale(locale.LC_ALL, 'ru')
# print(time.strftime('Сегодня: %B %d, %Y'))


# def hello(name, world):
#     print('Hello', name, 'Say', world)
#
#
# hello('Irina', 'hi')
# hello('Ivan', 'hello')


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# n = 7
# m = 9
# get_sum(n, m)
# get_sum('abc', 'def')
# get_sum(2.5, 4.3)


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2:
#             print(a, end='')
#         else:
#             print(b, end='')
#
#
# symbol(9, '+', '-')
# print()
# symbol(7, 'X', '0')


# def get_sum(a, b):
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)
# print(get_sum(1, 8))


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 6))


# def sum(x, y):
#     if x > y:
#         return x - y
#     if x < b:
#         return x + y
#
#
# a, b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
# print(sum(a, b))


# 02.10.2022==================================================================================================


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
# print(is_greater(10, 5))
# print(is_greater(5, 10))


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input('Введите пароль:')
# if check_password(p):
#     print('Надежный пароль')
# else:
#     print('Ненадежный пароль')


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5))
# q = 2
# print(get_sum(1, 5, d=2))
# print(get_sum(1, 5, d=q))


# def sum_s(a, b=20):
#     print(a * b)
#
#
# sum_s('-', 5)


# def line(a=20, b='-'):
#     print(b * a)
#
#
# line(10, '*')
# line()


# def get_str(n=20,symbol='-'):
#     return symbol*n
#
#
# print(get_str())
# num = int(input('Введите число: '))
# sym = input('Введите символ: ')
# print(get_str(num, sym))


# def digit_sum(n, even=True):  # 123
#     s = 0
#     while n > 0:
#         cur_digit = n % 10  # 3 2 1
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2:
#             s += cur_digit
#         n //= 10  # 12 1
#     return s
#
#
# print('Сумма четных цифр:')
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print('Сумма нечетных цифр:')
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print('Name:', name, '\nAge:', age)
#
#
# # display_info('Ira', 23)
# display_info(23, 'Ira')
# display_info(age=23, name='Ira')
# # display_info('Igor', age=23, name='Ira')

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# a = 'Hello'
# b = 'Hello'
# print(a == b)
# print(a is b)

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# print(id(lt1))
# lt1.pop(1)
# print(lt1)
# lt1[1] = 'Hello'
# print(lt1)
# print(id(lt1[1]))
# print(id(lt1))

# s = 'Hello'
# print(id(s))
# # s += 'World'
# s = s + 'World'
# print(s)
# print(id(s))

# a = 5
# print(id(a))
# a += 1
# print(a)
# print(id(a))

# s = 'Hello'
# # s[1] = 'a'
# print(id(s))
# s = s[1:-1]
# print(s)
# print(id(s))

# lt1 = [1, 2, 3]
# print(id(lt1))
# # lt1 = lt1[1:-1]
# # lt1 = lt1 + [4, 5]
# lt1 += [4, 5]
# print(lt1)
# print(id(lt1))

# # Кортеж (tuple) +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# # a = (1, 2, 3, 4, 5)
# a = 1, 2, 3, 4, 5
# print(type(a))
# print(a)
#
# b = tuple((1, 2, 3, 4, 5))
# print(type(b))
# print(b)
#
# c = tuple('Hello')
# print(c)

# t = (1,)
# print(t)
# print(type(t))

# b = tuple((1, 2, 3, 4, 5))
# print(b)
# print(b[3])
# print(b[1:3])
# # b[1] = 3  # кортеж нельзя изменить

# s = tuple(int(input('->')) for i in range(3))
# print(s)

# s = input("Строка: ")
# a = tuple(s)
# print(a)

# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# tpl = tuple(mas)
# print(tpl)
#
# print(tuple(randint(0, 100) for _ in range(10)))
#
# mas = tuple(randint(0, 100) for _ in range(10))
# print(mas)

# print(tuple(2 ** i for i in range(1, 13)))

# t1 = tuple('hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index('l'))
# print(t3.index('l', 4))
# for i in t3:
#     print(i, end=' ')
# print(t3[2:5])


# 06.10.2022 =====================================================================================================

# DZ----------------------------------------------
# lst = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# row = 0
# for row in lst:
#     for col in row:
#         print(col, end='\t')
#     print()
#
# print('--------------')
# i = 0
# for col in row:  # row = 4 итерации
#     # print('********')
#     # print(col)
#     # print('********')
#     for row in lst:  # [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]
#         # print('==========')
#         # print(row)
#         # print('==========')
#         print(row[i], end='\t')
#     i += 1
#     print()

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             # first = tpl.index(el)
#             # second = tpl.index(el, first + 1)  # + 1
#             # return tpl[first: second + 1]
#             return tpl[tpl.index(el): tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def krt(x, y):
#     num = x.count(y)
#     if num == 1:
#         i = x.index(y)
#         print(x[i:])
#
#     if num > 1:
#         i = x.index(y)
#         j = x.index(y, i + 1, -1)
#         print(x[i:j + 1])
#
#     if num < 1:
#         print(())
# --------------------------------------------------

# def ran(a, b):
#     return tuple(randint(a, b) for _ in range(10))
#
#
# tpl1 = ran(0, 5)
# tpl2 = ran(-5, 0)
# print(tpl1)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print('0 =', tpl3.count(0))

# a = 123456
# s = str(a)
# # lst = list(map(int, list(s)))
# lst = list(s)
# print(lst)
#
# # lst1 = []
# # for i in lst:
# #     lst1.append(int(i))
# # print(lst1)
#
# print(''.join(lst))

# t = (10, 11, [1, 2, 3], (4, 5, 6), ['hello', 'world'])
# print(t, id(t))
# t[-1][0] = 'new'
# print(t, id(t))
# t[4].append('hi')
# print(t, id(t))


# def set_elements(lst):
#     s = []
#     # for i in lst[::-1]:
#     #     if i not in s:
#     #         s.append(i)
#     [s.append(i) for i in reversed(lst) if i not in s]
#     return tuple(s)
#
#
# print(set_elements([1, 2, 3, 3, 2]))
# print(set_elements([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = 'tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# print(user[0])
# name, age, is_married = user
# print(name)

# a = (1, 2, 3)
# # del a
# print(a)
# lst = list(a)
# lst.append(4)
# print(lst)
# tpl = tuple(lst)
# print(tpl)

# countries = (
#     ('Германия', 80.2, (('Берлин', 3.326), ('Гамбург', 1.718))),
#     ('Франция', 66, (('Париж', 2.2), ('Марсель', 1.6)))
# )
# print(countries, end='\n\n')
#
# for country in countries:
#     # print(country)
#     countryName, countryPopulation, sities = country
#     print('\nСтрана:', countryName, 'население =', countryPopulation)
#     for city in sities:
#         # print(city)
#         cityName, cityPopulation = city
#         print('\tГород:', cityName, 'население =', cityPopulation)


# Множество (set)-----------------------------------------------------------------------------

# # s = {'banana', 'apple', 'orange', 'apple', 'banana'}
# # print(type(s))
# # print(s)
# # print(len(s))
# c = ['hello', 'world']
# a = set(c)
# print(a)

# s = {x * x for x in range(10)}
# print(s)

# num = [1, 2, 2, 3, 3, 4, 4, 5, 6]
# # print(num)
# # num = set(num)
# # print(num)
# # num = list(num)
# num = list(set(num))
# print(num)


# def to_set(elem):
#     # return set(elem), len(set(elem))
#     st = set(elem)
#     return st, len(st)
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))


# t = {'red', 'green', 'blue'}
# # print('green' in t)
# # print('green1' in t)
# # print('green' not in t)
# for i in t:
#     print(i)


# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {i for i in r if 'a' not in i}
# # a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)
#
# for i in r:
#     if i[1] == 'c':
#         if i[0] == 'a':
#             print('A' + i[1:])
#         else:
#             print('B' + i[1:])

# 11.10.2022=============================================================================================


# a = {'Tom', 'Bob', 'Alice'}
# a.add('Ann')
# print(a)
# # a.remove('Tom')
# # print(a)
# # user = 'Tom'
# # if user in a:
# #     a.remove('Tom')
# # print(a)
# # a.discard('Bob')
# # print(a)
# a.pop()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # # c = a.union(b)
# # c = a | b
# # print(c)  #--
# # # a.update(b)
# # a |= b
# # print(a)  #--
# # # c = a & b
# # a &= b
# # print(a)
# # print(c)  #--
# # c = a - b
# c = a ^ b
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 5}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))
# print(sum(s))

# s1 = 'Hello'
# s2 = 'How are you'
# s = set(s1) & set(s2)
# print(s)

# s1 = 'Python'
# s2 = 'Programing language'
# s = set(s1) - set(s2)
# print(s)

# a = set(input('->'))
# print(a)

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
#
# only = drawing ^ music
# print('Одно хобби', only)
#
# both = drawing & music
# print('Два кружка: ', both)
#
# drawing = drawing - both
# print(drawing)
# b = [1, 2, 3, 4, 5]
# s = frozenset([1, 2, 3, 4, 5])  # b
# print(s)
# c = [0, 1, 2]
# s1 = frozenset(c)
# print(s1)
# s -= s1
# print(s.)
# # a = frozenset({'Hello', 'world'})
# # print(a)

# Словари (dict)----------------------------------------------------------------------------------------

# s = ['one', 'two']
# print(s[0])
# d = {"1": 'one', 2: 'two', 3: 'one'}
# print(d)
# print(d["1"])
# print(d[2])

# d = {'one': 1, 'two': 2}
# print(d)
# print(type(d))
#
# d1 = dict(one=1, two=2)
# print(d1)
# print(type(d1))

# a = [  # либо кортеж
#     ('Igor@gmail.com', 'igor'),
#     ('irina@gmail.com', 'irina'),
#     ('anna@gmail.com', 'anna')
# ]
# d = dict(a)
# print(d)

# d = {a: a ** 2 for a in range(1, 7)}
# print(d)
# print(d[2])
# d[2] = 15
# print(d)
# d[6] = 4 ** 2
# print(d)

# d = {0: 'text', 'one': 45, (1, 2.3): 'кортеж', 42: [2, 3, 6, 7], True: 1}  # [2,3,6,7] список нельзя ставить ключом
# print(d)
# print(d[(1, 2.3)])
# print(d[True])
# print(d[42][1])
# print('one' in d)
# print('two' in d)
#
# print(d.keys())
# if 'one' in d:
#     print('TRUE')
# if 'one' in d.keys():
#     print('TRUE')
# key = 2
# # if key in d:
# #     del d[key]
# try:
#     del d[key]
# except KeyError:
#     print('Элемента с ключом ' + str(key) + ' нет в словаре')
# print(d)

# d = {0: 'text', 'one': 45, (1, 2.3): 'кортеж', 42: [2, 3, 6, 7], True: 1}
# print(d)
# for key in d:
#     print(key, '->', d[key])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# sum1 = 1
# for i in d:
#     sum1 *= d[i]
# print(sum1)

# d = dict()
# d[1] = input('->')
# d[2] = input('->')
# d[3] = input('->')
# d[4] = input('->')
# print(d)

# d = {a: input("-> ") for a in range(1, 5)}
# print(d)
# a = int(input("Какой элемент исключить: "))
# if a in d:
#     del d[a]
#     print(d)
# else:
#     print('Такого элемента нет')

# capitals = dict()
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals['Испания'] = 'Мадрид'
# countries = ['Россия', 'Италия', 'Франция', 'Испания']
# for country in countries:
#     if country in capitals:
#         print('Столица страны '+ country + ': ' + capitals[country])
#     else:
#         print('В базе нет страны с названием ' + country)

# Задача на базу --------------------------------------------------------------------------------------
# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 4600]
# }
#
# for i in goods:
#     print(i, ')', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб', sep='')
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         cnt = int(input('Кол-во: '))
#         goods[n][1] = cnt
#     else:
#         break
#
# for i in goods:
#     print(i, ')', goods[i][0], ' - ', goods[i][1], ' шт. по ', goods[i][2], 'руб', sep='')
# ---------------------------------------------------------------------------------------------------------


# 13.10.2022===============================================================================================

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['b'])
# value = d.get('b', 'False')
# print(value)
# print(d)

# print(d)
# item = d.items()
# print(item)
# key = d.keys()
# print(key)
# value = d.values()
# print(value)
#
# for i, j in d.items():
#     print(i, '->', j)

# print(d)
# d.clear()
# print(d)

# print(d)
# # # # item = d.pop('b', 5)
# # # # print(item)
# # # it = d.popitem()
# # # print(it)
# # item = d.setdefault('e', 5)
# # print(item)
# d.update({'a': 7, 'q': 9})  # [('a', 7), ('q', 9)]
# print(d)

# # d2 = d
# d2 = d.copy()
# print('D =', d)
# print('D2 = ', d2)
# d['e'] = 7
# d['b'] = 5
# print()
#
# print('D =', d)
# print('D2 = ', d2)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # z = x.copy()
# # z.update(y)
# z = y | x
# print(z)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# print(d)
# print(new_d)

# d1 = {'name': 'Kelly', 'age':25 , 'salary': 8000, 'city': 'New York'}
# d2 = {}
# name = d1.pop('name')
# salary = d1.pop('salary')
#
# d2['name'] = name
# d2['salary'] = salary
# print(d1)
# print(d2)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# print(d)
# d['location'] = d.pop('city')
# print(d)

# a = {
#     'First': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, a[x][y],  sep='')

# d = {'один': 1, "два": 2, 'три': 3, 'Четыре': 4}
# a = {key for key, value in d.items() if value <= 2}
# print(a)

# a = {i: i * 5 for i in [10, 20, 30, 40]}
# print(a)

# a = {i: i * 5 for i in 'Hello'}
# print(a)

# value = int(input('-> '))
# # lt = [1, 2, 3, 4, 5]
# a = {i: value for i in range(1, 9)}
# print(a)

# d = dict.fromkeys(['a', 'b'], 100)
# print(d)

# list()------------------------------------------------
# figures = {1: 'rectangle', 2: 'triangle', 3: 'circle'}
# # value = list(figures.keys())
# # value = list(figures)
# # value = list(figures.values())
# value = list(figures.items())
# print(value)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i  # 'one' 'two' 'three' 'four'
#     else:
#         d[s].append(i)
# print(d)

# zip()---------------------------------------------------------------------------------------

# d = dict(zip([12, 1, 2], ['Dec', ' Jan', 'Feb']))
# print(d)

# a = [12, 1, 2]
# b = ['Dec', ' Jan', 'Feb']
# f = {k: v for k, v in zip(a, b)}
# print(f)

# a = [1, 2, 3]
# b = [5, 9, 7, 4]
# print(list(zip(a, b)))
#
# print(list(zip(range(5), range(100))))

# a = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# b = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
# c = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2), (k3, v3) in zip(a.items(), b.items(), c.items()):
#     # print(k1, '->', v1)
#     # print(k2, '->', v2)
#     # print(k1, '->', v1, ',', v2)
#     print(k1, '->', v1, ',', v2, ', ', v3, sep='')

# a = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# x, y = zip(*a)  # * распаковывает zip
# print(list(x))  # можно в список
# print(y)  # можно в кортеж
#
# lt1 = [1, 2, 3, 4]
# lt2 = ['a', 'b', 'c', 'd']
# a1 = list(zip(lt1, lt2))
# print(a1)

# lt1 = [2, 21, 3, 32]
# lt2 = ['b', 'a', 'd', 'c']
# a1 = list(zip(lt2, lt1))
# # print(a1)
# # a1.sort()
# a = sorted(zip(lt1, lt2))
# # print(a1)
# print(a)

# month = ['January', 'February', 'March']
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
# for sales, cost, m in zip(total_sales, prod_cost, month):
#     res = sales - cost
#     print('Общая прибыль в', m, '=', res)

# one = {'apple': 0.4, 'orange': 0.35, 'banana': 0.6}
# two = {'pepper': 0.2, 'onion': 0.55}
# # print({one, two})  # {{'apple': 0.4, 'orange': 0.35}, {'pepper': 0.2, 'onion': 0.55}}  # Ошибка {}
# # print([one, two])
# print({**one, **two})  # {'apple': 0.4, 'orange': 0.35, 'pepper': 0.2, 'onion': 0.55}
#
# for k, v in {**one, **two}.items():
#     print(k, '->', v)


# 18.10.2022=================================================================================================

# n = int(input("Кол-во студентов: "))
# stud = {}
# s = 0
# for i in range(n):
#     name = input(str(i+1) + "-й студент: ")
#     point = int(input("Балл: "))
#     stud[name] = point
#     s += point
# avrq = round(s / n)
# print("средний балл", avrq)
# print("Студенты с баллом выше среднего: ")
# for i in stud:
#     if stud[i] > avrq:
#         print(i)


# en = ["red", "green", "blue"]
# j = 1
# for i in en:
#     print(j, '-й цвет: ', i, sep="")
#     j += 1

# en = ["red", "green", "blue"]
# for j, i in enumerate(en, 1):
#     print(j, '-й цвет: ', i, sep="")

# en = {0: 1, 1: 2, 2: 3}
# for i, j in enumerate(en):
#     print(i, ': ', j, '->', en[j], sep='')

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))
# print(func())

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# num1 = summa(1, 2, 3, 4, 5, 6, 7, 8)
# num2 = summa(6, 7, 8)
# print(num1)
# print(num2)


# def to_dict(*args):
#     # return {i: i for i in args}
#     dic = {}
#     for i in args:
#         dic[i] = i
#     return dic
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('gray', (2,17), 3.11, -4))


# def nums(*args):
#     lst = []
#     a = sum(args) / len(args)
#     print(a)
#     for i in args:
#         if i < a:
#             lst.append(i)
#     return lst
#
#
# print(nums(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(nums(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))


# def print_scores(stud, *scores):
#     print('Student name:', stud)
#     for score in scores:
#         print(score, end=" ")
#     print()
#
#
# print_scores('Jonatan', 100, 95, 88, 92, 99)
# print_scores('Rick', 96, 20, 33)


# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_odd=False):
#     res = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2):  # 1й True or False  2й False or True and i % 2
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))


# def func(*args):
#     res = []
#     for i in args:
#         res.append(int(str(i)[::-1]))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))


# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a='Python'))


# def info(**data):
#     for k, v in data.items():
#         print(k, '->', v)
#     print('*' * 20)
#
#
# info(firs_name="Irina", last_name='Petrova', age=22, phone=1234567890)
# info(firs_name="Igor", last_name='Ivanov', age=36,email='igor@gmail.com', country='Russia', phone=6234564820)


# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyas_color='gray')
# print('my_dict =', my_dict)


# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
#
# func1(1, 2, 3, 4, 5)
# func2(one=123, two=456)


# def func1(a, *args, one=True, **kwargs):  # только такая последовательность
#     return args, kwargs, a, one
#
#
# print(func1(5, 9, 7, 8, 6, one=False, b=2, c=3, d=4))


# Область видимости (scope)----------------------------------------------------------------------------------

# for i in range(5):
#     a = 5
#     print(i)
#
# print('i за пределами цикла', i)
# print('i за пределами цикла', a)

# if True:
#     a = 5
# print('a =', a)

# name = 'Tom'  # глобальная переменная
#
#
# def hi():
#     print('Hello', name)
#
#
# def bye():
#     global name
#     name = 'Bob'  # локальная
#     print('Good bye', name)
#
#
# def func():
#     global surname
#     surname = 'Ivanov'
#
#
# hi()
# bye()
# print(name)
# func()
# print(surname)

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()


# def add_two(a):
#     x = 2
#     return a + x
#
#
# print(add_two(3))
# # print(x)

# x = 3
# def func(a):
#     # x = 2
#
#     def inner():
#
#         print('x =', x)
#         return a + x
#     return inner()
#
#
# print(func(5))  # 7


# max = [1, 2, 3, 4, 5]
# print(min(max))

# import builtins
#
# print(dir(builtins))


# 20.10.2022 ===========================================================================================

# Вложенные функции

# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#     inner_func()
#
#
# outer_func('world!')


# def func1():
#     a = 6  # 2
#
#     def func2(b):
#         a = 4  # 5
#         print('Сумма', a + b)  # 6
#
#     print('a:', a)  # 3
#     func2(4)  # 4
#
#
# func1()  # 1


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#     # t = a
#     print('global:', x)  # 25
#
#     def inner():
#         nonlocal a
#         a = 35
#         print('nonlocal:', a)  # 35
#
#     inner()
#     print(a)
#     t = a
#
#
# fn()
# z = x + t  # 25 + 30 = 55 | 25 + 35 = 60
# print('results', z)

# x = 5
#
#
# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)
#
#     fn2()
#     print('fn1.x = ', x)
#
#
# fn1()
# print('x = ', x)


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)


# def increment(number):
#     def inner():
#         return number + 1
#     return inner()
#
#
# res = increment(10)
# print(res)
# # print(increment(10))

# Замыкания------------------------------------------------------------------------------

# def outer(n):
#     def inner(x):
#         return n + x
#     return inner
#
#
# # print(outer(5)(10)) # не используется но работать будет
# res = outer(5)
# print(type(res))
# q = res(10)
# print(q)
# print(res(2))
# print('---')  # ---
# res2 = outer(7)
# print(res2(5))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + 'new'
#         # a = 20
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res2()
#
# res1()


# students = {
#     'Alice': 100,
#     'Bob': 67,
#     'Nick': 85,
#     'David': 75,
#     'Elise': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make_classifier(lover, upper):
#     def classify_student(exam):
#         return {k: v for k, v in exam.items() if lover <= v < upper}
#
#     return classify_student
#
#
# a = make_classifier(80, 101)
# b = make_classifier(70, 80)
# c = make_classifier(50, 70)
# d = make_classifier(0, 50)
# print(a(students))
# print(b(students))
# print(c(students))
# print(d(students))


# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def nul():
#         return a * b
#
#     def replace():
#         print()  # pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.nul = nul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.nul())


# 25.10.2022===================================================================================================

# Анонимные функции, Lambda- выражения -------------------
# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func('a', 'b'))

# print((lambda x, y: x**2 + y**2)(2, 5))

# summ = lambda a=1, b=2, c=3: a + b + c
# print(summ())
# print(summ(10))
# print(summ(10,20))

# func1 = lambda *args: args
# print(func1('a', 'b'))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
# for i in c:
#     print(i('abc_'))

# # 1
# def inc1(n):
#     def wrap(x):
#         return x + n
#
#     return wrap
#
#
# f1 = inc1(42)
# print(f1(3))
#
#
# # 2
# def inc(n):
#     return lambda x: x + n
#
#
# f = inc(42)
# print(f(3))
#
# # 3
# inc2 = (lambda n: (lambda x: x + n))
# # f2 = inc2(42)
# # print(f2(3))
# print(inc2(42)(3))
#
# # 4
# print((lambda n: (lambda x: x + n))(42)(3))

# print((lambda n: (lambda x: (lambda c: n + x + c)))(2)(4)(6))


# def func(i):
#     return i[1]


# d = {'b': 15, 'a': 10, 'c': 24}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1], reverse=True)
# # lst.sort(key=func, reverse=True)  # если делать через функцию выше
# print(lst)
# dict1 = dict(lst)
# print(dict1)

# players = [{'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#            {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#            {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#            {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}
#            ]
# res = sorted(players, key=lambda i: i['last name'])
# print(res)
# # print(players)
#
# # players.sort(key=lambda i: i['last name'])
# # print(players)
#
# res = sorted(players, key=lambda i: i['raiting'])
# print(res)
#
# res = sorted(players, key=lambda i: i['raiting'], reverse=True)
# print(res)
#
# # print(sorted(players, key=lambda i: i['last name']))
# # print(players)
#
# # players1 = ['Наталья', "Виктор", "Саша"]
# # players1.sort(key=len)
# # print(players1)
#
# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[2](12, 5)
# print(b)

# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 2]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# d = {
#     1: (lambda: print('Понедельник')),
#     2: (lambda: print('Вторник')),
#     3: (lambda: print('Среда')),
#     4: (lambda: print('Четверг')),
#     5: (lambda: print('пятница')),
#     6: (lambda: print('Суббота')),
#     7: (lambda: print('Воскресение')),
# }
#
# d[4]()

# maximum = (lambda a, b: a if a > b else b)  # Тернарные выражения
# print(maximum(15, 13))

# minimum = (lambda a, b, c: a if a < b else b if b < c else c)
# print(minimum(9, 8, 5))

# Функция map()---------------------------------------------------------------------------------

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
# print(list(map(mult, lst)))
# print(list(map(lambda t: t * 2, lst)))
# print(list(map(lambda t: t * 2, range(10))))

# t = 2.88, -1.75, 100.55
# print(tuple(map(lambda x: int(x), t)))
# print(list(map(lambda x: str(x), t)))
# # print(list(map(str, t)))
#
# a = ['2.88', '-1.75', '100.55']
# # b = list(map(float, a))
# # print(b)
# # print(list(map(int, b)))
# print(list(map(int, map(float,a))))

# areas = [3.345673, 7.4890603032, 56.237689456, 9.08342437846, 32.567548754, 3.563454435]
# # print(list(map(round, areas, range(1, 7))))
# print(list(map(round, areas, [2, 6, 4, 3])))  # (2, 6, 4, 3)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# lst = list(map(lambda x, y: (x, y), st, num))  # dict(словарь) можно сразу указать вместо list
# # lst = list(map(lambda x, y: {x, y}, st, num))
# print(lst)
# tp = dict(lst)
# print(tp)

# a = [1, 2, 3]
# b = [4, 5, 6]
# slt = list(map(lambda x, y: x + y, a, b))
# print(slt)

# 27.10.2022 ===========================================================================================

# filter(func, iterable)

# t = ('abc', 'abcd', 'sdfdsf', 'def', 'qhie')
# t2 = tuple(filter(lambda i: len(i) == 3, t))
# print(t2)

# b = [66, 90, 68, 33, 64, 18, 84]
# res = list(filter(lambda i: 45 < i < 75, b))
# print(res)

# from random import *
#
# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# res = list(filter(lambda s: 10 <= s <= 20, lst))
# print(res)

# sp = [45, 55, 60, 37, 100, 105, 220]
# t = tuple(filter(lambda i: i % 15 == 0, sp))
# print(t)

# Декораторы -------------------------------------------------------------------------------------------

# def hello():
#     return 'Hello, i am func "hello"'
#
#
# def super_func(func):
#     print('Hello, i am func "super_func"')
#     print(func())
#
#
# super_func(hello)

# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
#
# def func_test():
#     print('Hello, i am func "hello"')
#
#
# test = my_decorator(func_test)
# test()

# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('Hello, i am func "hello"')
#
#
# # @my_decorator
# # def hello():
# #     print('Hello, i am func "hello"')
#
#
# func_test()
# # print()
# # hello()


# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return 'text'
#
#
# print(hello())


# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print('вызов функции ', count)
#     return wrap
#
#
# @cnt
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print('*' * 50)
#         fn(arg1, arg2)
#         print('*' * 50)
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print('Меня зовут', first, last)
#
#
# print_full_name('Ирина', "Лаврова")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         fn(*args, **kwargs)
#         print('*' * 50)
#         print('args:', args)
#         print('kwargs:', kwargs)
#         print('*' * 50)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study='Python'):
#     print(a, b, c, ' изучают', study)
#
#
# print_full_name('Ирина', "Борис", "Светлана", study='Javascript')
# print()
# print_full_name('Владимир', "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=' ')
#             fn(x, y)
#         return wrap
#     return args_dec
#
#
# @decor('Сумма:', '+')
# def summa(a, b):
#     print(a + b)
#
#
# @decor('разность:', '-')
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def multiply(n):
#     def return_mult(fn):
#         def wrap(num):
#             return 'Результат:' + str(fn(num) * n)
#         return wrap
#
#     return return_mult
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))


# def typed_fn(x, y, z):
#     return x * y * z
#
#
# def typed_fn2(x, y, z):
#     return x * y + z
#
#
# def typed_fn3(x, y, z='Hello!'):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, 'Doge'))
# # print(typed_fn2('Hello', 'World', '!'))
# # print(typed_fn3('Hello', 'World', z=5))


# def typed(*args, **kwargs):
#     def wrapper(func):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError('не корректный тип данных')
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError('не корректный тип данных')
#             return func(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello! "):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Doge"))
# print(typed_fn2("Hello_", "World", "!"))
# print(typed_fn3("Hello_", "World", z=5))
# # print(typed_fn3("Hello, ", "World", z='!!!'))


# 01.11.2022 =============================================================================================

# def decor(tx=None, decor_text=''):
#     def wrapper(fn):
#         def wrap(*args):
#             print(decor_text, end='')
#             fn(*args)
#
#         return wrap
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
#
# @decor
# def hello_world2(text):
#     print(text)
#
#
# @decor(decor_text='Hello, ')
# def hello_world(text):
#     print(text)
#
#
# hello_world2('Hi!')
# hello_world('world')

# строки--------------------------------------
# print(01)  # ошибка

# print(int('19'))
# # print(int('19.5'))
# print(int(19.5))

# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 16))
# print(int('100', 10))
# print(int('100'))
# # print(int('18', 8))

# print(bin(53))  # 0b10010  # 0B
# print(oct(18))  # 0o22  # 0O
# print(hex(18))  # 0x12  # 0X
#
# # print(0b100 + 2)
# # print(0o20 + 4)
# # print(0x11 + 3)
#
# print(0b100 + 0o20)  # 4
# print(0o20)  # 16
# print(0x11 + 3)

# FF0000  # 16ая система счисления
# rgb(255,0,0)  # 10ая система счисления

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# # print(e * 3)
# # print('e' in e)
# # print(e[-1])  #---
# # print(e[2:-1])
# # print(e[::-1])
# # print(e[-1:0:-1])
# # e = e[0:3] + 't' + e[4:]  #---
# # print(e)


# def chabgeChar(s, c_old, c_new):
#     s2 = ''
#     for i in s:
#         if i != c_old:
#             s2 += i
#         else:
#             s2 += c_new
#     return s2
#
#
# st = 'Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования.'
# st2 = chabgeChar(st, 'N', 'P')
# print('st = ', st)
# print('st2 = ', st2)

# print(u'Привет')  # --------------------------------------------

# print(r'C:\file.text')  # сырые строки, игнорирует спец символы
# print('C:\\file.text')
# # print(r'C:\\file.text\')  # ошибка будет
# print(r'C:\file.text\\'[:-1])
# print(r'C:\file.text' + '\\')
# print('C:\\file.text\\')

# name = 'Дмитрий'
# age = 25
# print('Меня зовут ' + name + '. Мне ' + str(age) + ' лет')
# print('Меня зовут ', name, '. Мне ', age, ' лет', sep='')
# print(f'Меня зовут {name}. Мне {age} лет')

# print(f'{2.324323245}')
# print(f'{round(2.324323245, 2)}')
# print(f'{2.324323245:.2f}')

# x = 10
# y = 5
# print(f'{x} x {y} / 2 = {int(x * y / 2)}'
#       f'- выражение')

# d = 74
# print(f'{{{{d}}}}')

# dir_name = 'doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print('home\\' + dir_name + '\\' + file_name)

# s = '''<div>
#     <a href="#">content</a>
# </div>
# '''
# print(s)
# s1 = """<div>
#     <a href="#">content</a>
# </div>
# """
# print(s1)

# "Привет"
# 'привет'
# "привет"

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     a = 5
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(min.__doc__)

# import math
#
#
# def cylinder(r, h):
#     '''
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     '''
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# документируются либо функции либо классы ----------------------------------------------

# print(dir(list))

# dz 15 папка

# 03.11.2022 ====================================================================================================

# print(ord('a'))
# print(ord('а'))  # русские буквы, юникод

# while True:
#     n = input('->')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break

# my_str = "Test string for me"
# arr = [ord(x) for x in my_str]
# print(arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print(arr)
# arr += [x for x in [ord(x) for x in input('-> ')[:3]] if x not in arr]  # [:6:2] - с пробелами
# print(arr)
# if arr[-1] in arr[:-1]:
#     print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))

# a = 122
# b = 97
# while b <= a:
#     print(chr(b), "", end="")
#     b += 1
# while a <= b:
#     print(chr(b), "", end="")
#     b -= 1


# a = 122
# b = 197
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=' ')
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=' ')


# a, b = 197, 122
# if b < a:
#     a, b = b, a
# while a <= b:
#     print(chr(a) + " ", end="")
#     a += 1

# print('apple' == 'Apple')
# print('apple' > 'Apple')  # 97 > 65
# print(ord('a'))  # 97
# print(ord('A'))  # 65

# from random import randint
#
# SHORTEST = 6
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     res = ''
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
#
# print('Ваш случайный пароль: ', random_password())

# print(dir(str))

# s = 'hello, WORLD! I am learning Python'
# print(s.capitalize())  # Hello, world! i am learning python
# print(s.lower())  # hello, world! i am learning python
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON
# print(s.title())  # Hello, World! I Am Learning Python
#
# print(s.count('l', 3))  # подсчитывает кол-во вхождений подстроки (L) в строку (s)
# print(s.find('Python'))
# print(s.find('Python1'))  # ищет в строке заданную подстроку, если она найдена, то возвращает индекс первого
# # вхождения подстроки, если нет - то возвращает "-1"
# print(s.find('l', 4))

# a = 'один два '
# b = a[:a.find(' ')]
# c = a[a.find(' ') + 1:]
# print(c + '' + b)

# s1 = 'ab12c59p7dq'
# digits = []
#
# # for i in s1:
# #     if i in '1234567890':
# #         digits.append(int(i))
# # print(digits)
#
# for i in s:
#     if '1234567890'.find(i) != -1:
#         digits.append(int(i))
# print(digits)

# s1 = 'ab12c59ptdq'
# s2 = []
# for i in s1:
#     try:
#         s2.append(int(i))
#     except ValueError:
#         continue
# print(s2)

# s = 'hello, WORLD! I am learning Python'
# print(s)
# # print(s.index('Python1'))  # ищет в строке заданную подстроку, если она найдена, то возвращает индекс первого
# # # вхождения подстроки, если нет - то возвращает исключение ValueError
# print(s.index('Python'))
# print(s.rfind('l'))  # с правой стороны
# print(s.rindex('l'))  # с правой стороны

# s = ' I am learning Python. hello, WORLD!'
# res = s.find('h')
# res1 = s.rfind('h')+1
# # print(s[:res]+ s[res1:])
# print(s[:s.find('h')] + s[s.rfind('h')+1:])

# print('abc123'.isalnum())  # определяет состоит ли строка из цифр и букв
# # print('123"'.isalnum())
# # print(''.isalnum())
# print('ABCabc'.isalpha())  # определяет состоит ли строка из букв
# # print('ABCabc1'.isalpha())
# print('123'.isdigit())  # определяет состоит ли строка из цифр
# print('abc'.islower())  # определяет состоит ли строка из строчных букв
# # print('abcA'.islower())  # определяет состоит ли строка из строчных букв
# print('abc2'.islower())
# print('ABC3;'.isupper())  # определяет состоит ли строка из заглавных букв

# print('py'.center(10, '-'))  # выравнивание строки по центру
# print('py'.center(30, '*'))

# print('    py'. lstrip())  # удаляют пробельные символы слева
# print('py    '. rstrip())  # удаляют пробельные символы справа
# print('   py    '. strip())  # удаляют пробельные символы и слева и справа
# print('   py   e '. strip())
#
# print('https://www.python.org'.lstrip('/:pths'))
# print('py.$$$;'.rstrip(';$.'))
# print('https://www.python.org'.lstrip('https://').rstrip('.org'))


# 08.11.2022 ====================================================================================

# s = '11 23 44 55 23 22'
#
# s_old = input('заменяемая: ')
# s_new = input('новая: ')
# i = s.find(s_old)
# # print(i)
# while i != -1:
#     l = len(s_old)
#     s = s[0:i] + s_new + s[i+l:]
#     i = s.find(s_old)
# print(s)

# st = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(st)
# print(st.replace("Nython", "Python", 2))  # заменяет вхождение подстроки в строке

# s = '-'
# seq = ('a', 'b', 'c')
# print(s.join(seq))  # a-b-c

# print('..'.join(['1', '2']))  # объединяет итерируемую последовательность (список, кортеж, другая строка) в одну
# # строку через заданный символ разделитель
# # print('..'.join([1, 2]))  # только строковый тип данных
# print(":".join("Hello"))

# print('Строка разделенная пробелами'.split())  # делит строку на список из подстрок
# # print('Строка_разделенная_пробелами'.split('_'))
# # print('Строка разделенная пробелами'.split('а'))
#
# print('www.python.org.ru.'.split('.'))
# print('www.python.org.ru.'.split('.', 2))

# a = list(map(int, input('->').split()))
# print(a)
# print(type(a[0]))

# a = input('Введите ФИО: ').split()
# print(a)
# print(a[0], ' ', a[1][0], '.', a[2][0], '.', sep='')
#
# print(f'{a[0]} {a[1][0:1]}.{a[2][0:1]}.')

# print('www.python.org.ru.'.split('.', 2))
# print('www.python.org.ru.'.rsplit('.', 2))
#
# print('www...python...org'.split('...'))

# a = input("Введите строку: ").split()
# print(a)
# print('*'.join(a))

# регулярные выражения ---------------------------------------------------------------------------

# import re
#
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9875 1945"  # ----------------------

# reg = 'я'
# print(s.find(reg))
# print(re.findall(reg, s))  # ['я', 'я'] возвращает список, содержащий все совпадения
# print(re.findall('12', s))  # []
#
# reg1 = 'совпадения'
# print(re.search(reg1, s))  # <re.Match object; span=(6, 16), match='совпадения'> находит местоположение первого
# #совпадения обьекта
# print(re.search(reg1, s).span())
# print(re.search(reg1, s).start())
# print(re.search(reg1, s).end())
# print(re.search(reg1, s).group())
#
# reg2 = 'Я ищу'
# print(re.match(reg2, s))  # поиск по заданному шаблону в начале строки
#
# print(re.split(reg, s))  # возвращает список в котором строка разбита по шаблону
#
# reg3 = r'\.'
# print(re.split(reg3, s, 1))
#
# reg3 = r'\.'
# print(re.sub(reg3, '!', s, 1))  # поиск и замена текущего элемента  # -------------------------------

# import re
#
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9875 19_45"

# # reg = r'[203]'
# # reg = r'[0-3]'
# # reg = r'[12][09][0-9][0-9]'
# # reg = r'[А-яё.]'  # [а-яА-Яё]
# # reg = r'[^039]'
# # reg = r'\d'
# # reg = r'\w'
# # reg = r'\W'
# reg = r'\s'
# print(re.findall(reg, s))

# s1 = 'ели[-ели].'
# pattern = r'[А-яё.\[\]-]'
# # pattern = r'-'
# print(re.findall(pattern, s1))

# txt = 'Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапозоне от 00 до 59. 2021-06-15T01:09'
# pattern = '[0-2][0-9]:[0-5][0-9]'
# print(re.findall(pattern, txt))

# 10.11.2022 =====================================================================================

# Повторения---------------------------------
# + - от 1го до бесконечности
# * - от 0 до бесконечности
# ? - 0 или 1

# import re

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9875 19_4 5"
# # reg = r'\A\w\s\w+\s\w+'  # w - Я
# # reg = r'\w\s\w\Z'
# # reg = r'\w\s\w\b'  # r'\b\w\s\w'
# # reg = r'сов\B'  # сов вначале, и ищем в конце
# # reg = r'\w+'
# # reg = r'\d+'
# reg = r'20*'
# print(re.findall(reg, s))


# s1 = 'Цифры: 7, +17, -42, 0013, 0.3677.657'
# # pattern = r'[+-]?\d+[.\d]*'
# pattern = r'[+-]?\d+\.?\d*'
# print(re.findall(pattern, s1))

# s1 = '05-3-1987 # Дата рождения'
# # print(re.sub(r'#.*', '', s1))
# print('Дата рождения', re.sub(r'#.*', '', s1))
# # Дата рождения: 05.3.1987
# print('Дата рождения:', re.sub(r'-', '.', re.sub(r'#.*', '', s1)))  # 05-3-1987
#
# # print('Дата рождения:', re.sub(r'-?#.*', '.', s1)[:-1])  # не работает, с чата

# s1 = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# pattern = r'\w+\s*=[^;]+'
# print(re.findall(pattern, s1))

# s1 = '12 сентября 2021 года'
# reg1 = r'\d{2,}'
# # reg1 = r'[А-я]{2,}'
# print(re.findall(reg1, s1))

# s1 = '+7 499 256-45-78, +74994566478, 7 (499) 456 45 78, 74994564578'
# reg = r'\+?7\d{10}'
# print(re.findall(reg, s1))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9875 19_4 5"
# # reg = r'^\w+\s\w+'
# reg = r'\w+\s\w+$'
# print(re.findall(reg, s))

# def login(a):
#     return re.findall(r'^[\w!@#$]{8,25}$', a)
#
#
# print(login('admin_admin'))
# print(login('admin_admin&&'))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# print(re.findall(r'[я]', 'Я я', re.IGNORECASE))

# text = '''
# one
# two
# '''
# print(re.findall(r'^one$', text))
# print(re.findall(r'^one$', text, re.MULTILINE))

# text = '''
# one
# two
# '''
# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))


# 15.11.2022 ====================================================================================

# print(re.findall("""
# [A-z.-]+  # part 1
# @         # поиск символа @
# [a-z_.-]+ # part 2
# """, "test@mail.ru", re.VERBOSE))

# text = 'hello world'
# print(re.findall(r'\w\+', text, re.DEBUG))

# text = """Python,
# python,
# PYTHON
# """
# reg = "(?im)^python"
# print(re.findall(reg, text))  # , flags=re.IGNORECASE | re.MULTILINE

# s = "123456@.ru&, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru."
# reg = r'[\w.-]+@[\w.]+[a-z]{2,3}'
# print(re.findall(reg, s))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.+?>', text))

# greedy (жадный)
# lazy (ленивый)

# *?, +?, ??
# {m,n}?, {,n}?, {m,}?

# t = "2324 786 22 4569"
# # reg = r'\d{1,3}'  # жадное регулярное выражение
# reg = r'\d{1,3}?'  # ленивое регулярное выражение
# print(re.findall(reg, t))

# s = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img[^>]*>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))  # <img stc='bg.jpg'>

# s = "Python (в русском языке встречаются названия питон[16] или пайтон[17]) - высокоуровненый язык " \
#         "программирования " \
#     "общего назначения с динамической строгой типизацией и автоматическим управлением памятью[18][19]."
# reg = r'\[\d+]'
# print(re.findall(reg, s))

# s = 'Петр и Ольга отлично учатся!'
# reg = 'Петр|Виталий|Ольга'
# print(re.findall(reg, s))

# () - группирующая скобка
# (?:) - группирующая скобка, не сохраняющая

# s = 'int = 4, float = 4.0, double = 8.0f'
# # reg = r'int\s*=\s*\d[.\w+]*|double\s*=\s*\d[.\w+]*'
# # reg = r'(?:int|double)\s*=\s*\d[.\w+]*'
# reg = r'(?:int|double)\s*=\s*(?:\d[.\w+]*)'
# print(re.findall(reg, s))

# # 192.168.255.255
# s = '127.0.0.1'
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s))

# s = 'Word2016, PS6, AI5'
# # reg = r'([A-z]+)(\d*)'
# reg = r'(([A-z]+)(\d*))'
# print(re.findall(reg, s))

# s = '5 + 7*2 - 4'
# # reg = r'\s*[+*-]\s*'  # ['5', '7', '2', '4']
# reg = r'\s*([+*-])\s*'  # ['5', '+', '7', '*', '2', '-', '4']
# # reg = r'\s*(?:[+*-])\s*'  # ['5', '7', '2', '4']
# # reg = r'(\s*[+*-]\s*)'
# print(re.split(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9875 19_4 5"
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print('[1]', m[1])
# print('[2]', m[2])
# print('[0]', m[0])


# 17.11.2022 ==================================================================================

# print('Hello')

# 22.11.2022 ===================================================================================

# print('hello')

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print('[1]', m[1])
# print('[2]', m[2])
# print('[0]', m[0])
# print(re.search(reg, s).group(1))

# text = '''
# Самара
# Москва
# Тверь
# Уфа
# Казань
# '''
#
# count = 0
#
#
# def replace_find(m):
#     global count
#     count += 1
#     return f'<option value="{count}">{m.group(1)}</option>\n'
#
#
# print(re.sub(r'\s*(\w+)\s*', replace_find, text))

# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# reg = r'<img\s+[^>]*src=([\'"])(.+)\1>'
# print(re.findall(reg, s))

# (?P<name>...)  (?P=name)  назначение имени для круглой скобки

# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# reg = r'<img\s+[^>]*src=(?P<q>[\'"])(.+)(?P=q)>'
# print(re.findall(reg, s))

# s = "Самолет прилетает 10/23/2023. Будем ради вас видеть после 10/24/2023."
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.findall(reg, s))
# print(re.sub(reg, r'\2.\1.\3', s))

# s = 'google.com and google.ru and yandex.ru'
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))

# 24.11.2022 =============================================================================================

# Рекурсия --------

# def elevator(n):
#     if n == 0:
#         print('Вы в подвале')
#         return
#     print('=>', n)
#     elevator(n - 1)  # 5 4 3 2 1
#     print(n, end=' ')  # 1 2 3 4 5
#
#
# n1 = int(input('На каком Вы этаже: '))  # 5
# elevator(n1)

# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res = res + i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def sum_list(lst):
#     if len(lst) == 1:
#         print(lst, '=> lst[0]:', lst[0])
#         return lst[0]  # 9
#     else:
#         print(lst, '=> lst[0]:', lst[0])
#         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# def to_str(n, base):
#     convert = '0123456789'
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]  # 9 6 7
#
#
# print(to_str(769, 10))  # 769 // 10 = 76 // 10 = 7


# def to_str(n, base):
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return convert[n]  # 15 (15)
#     else:
#         return to_str(n // base, base) + convert[n % base]  # 15 (f)
#
#
# print(to_str(255, 16))  # 769 // 16 = 15

# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], 'Ann']
# print(type(names[0]) == str)
# print(type(names[0]) == list)
# print(names[0])
# print(isinstance(names[1], list))
# print(names[1][0])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))

# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], 'Ann']
#
#
# def count(lst):
#     cnt = 0
#     for i in lst:
#         if isinstance(i, list):
#             cnt += count(i)
#         else:
#             cnt += 1
#     return cnt
#
#
# print(count(names))

# names = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], 'Ann']
#
#
# def union(s):
#     if not s:  # s == []:
#         return s
#     if isinstance(s[0],  list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
#
# print('Выпрямленый список:', union(names))
# print(names)


# def remove(text):
#     if not text:
#         return ''
#     if text[0] == '\t' or text[0] == ' ':
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove("  Hello\tWorld   "))

# 29.11.2022 =========================================================================================
# Файлы-----------

# # f = open('D:\\PythonAcademy\\txt.txt', 'r')
# f = open('txt.txt', 'r')  # открыть файл
# # print(f)
# # print(*f)
# f.close()  # закрыть файл
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)

# f = open('txt.txt', 'r')
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('txt.txt', 'r')
# try:
#     print(f.read())
# finally:
#     f.close()

# f = open('test.txt', 'r')
# print(f.readline())  # построчно считывает
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open('test.txt', 'r')
# # print(f.readlines())
# print(f.readlines(15))
# f.close()

# f = open('test.txt', 'r')
# for line in f:
#     print(line)  # line, end='\r'
# f.close()

# f = open('test.txt', 'r')
# count = 0
# for line in f:
#     count += 1
# f.close()
# print(count)

# f = open('test.txt', 'r')
# print(len(f.readlines()))
# f.close()

# f = open('xyz.txt', 'w')
# f.write('hello\nWorld')
# # f.write('привет\nмир')  # кириллица тоже можно
# #  # f.write(5)  # будет ошибка
# f.close()

# f = open('xyz.txt', 'a')
# f.write('\nновый текст')
# f.close()

# f = open('xyz.txt', 'a')
# # print(f.write('\nновый текст'))
# lines = ['\nЛиния 1', '\nЛиния 2']
# f.writelines(lines)
# f.close()

# f = open('xyz.txt', 'w')
# lst = [str(i) + str(i-1) for i in range(1, 20)]  # str(i) + str(i-1) + '\t'
# print(lst)
# # f.writelines(lst)
# for index in lst:
#     f.write(index + '\t')
# f.close()
# -------------------------------------------------------

# f = open('text2.txt', 'w')
# f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать в список файл')
# f.close()
#
# f = open('text2.txt', 'r')
# read_file = f.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == 'изменить строку в списке;\n':
#         read_file[i] = 'Hello world\n'
# print(read_file)
# f.close()
#
# f = open('text2.txt', 'w')
# f.writelines(read_file)
# f.close()

# f = open('text2.txt', 'w')
# f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать в список файл')
# f.close()
#
# f = open('text2.txt', 'r')
# read_line = f.readlines()
# print(read_line)
# n = int(input("Введите индекс: "))
# if 0 <= n < len(read_line):
#     read_line.pop(n)
# else:
#     print('Такой строки нет')
# print(read_line)
# f.close()
#
# f = open('text2.txt', 'w')
# f.writelines(read_line)
# f.close()

# f = open('txt.txt', 'r')
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()

# f = open('txt.txt', 'r+')  # файл должен быть уже
# print(f.write('I am learning Python'))  # 20
# print(f.seek(3))  # 3
# print(f.write('--new string--')) # 14
# print(f.tell()) # 17
# f.close()

# 04.12.2022 =======================================================================

# with open('text7.txt', 'w+') as f:
#     print(f.write('0123456789'))

# with open('text2.txt', 'r') as f:
#     for i in f:
#         # print(i)
#         print(i[:6])

# file_name = 'res.txt'
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.77]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     return ' '.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
# # print(get_line(lst))

# file_name = 'res.txt'
# with open(file_name, 'r') as f:
#     nums = f.read()
#
# print(nums)
#
#
# lst = list(map(float, nums.split(' ')))
# print(lst)
# print(len(lst))
# print(sum(lst))

# def longest_worlds(file):
#     with open(file, 'r', encoding='utf-8') as text:
#         w = text.read().split()
#         # max_length = len(max(w, key=len))
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# file_name = 'res.txt'
# print(longest_worlds(file_name))

# # text = 'строка №1\nстрока №2\nстрока №3\nстрока №4\nстрока №5\nстрока №6\nстрока №7\nстрока
# #  №8\nстрока №9\nстрока №10\n'
# #
# # with open('one.txt', 'w') as f:
# #     f.write(text)
# read_file = 'one.txt'
# write_file = 'two.txt'
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace('строка', 'Линия - ')
#         fw.write(line)

# Модуль OS и OS.PATH ------------------------------------------------
# import os


# print('Текущая директория: ', os.getcwd())  # D:\PythonAcademy
#
# print(os.listdir())  # возвращает список директорий и файлов, находящихся в текущей директории
# print(os.listdir('..'))

# os.mkdir('folder')  # создали директорию по указанному пути (папку)

# os.makedirs('nested1/nested2/nested3')  # создает промежуточные директории и конечную, указанную в пути, если они
# # не существуют. Если конечная директория уже существует, то будет сгенерирована ошибка FileExistsError

# os.remove('xyz.txt')  # удаление файла

# # os.rename('nested1', 'test')  # переименовывает файл или директорию
# os.rename('test.txt', 'test/test1.txt')  # переименовывает файл или директорию, перемещая файлы в существующие
# # директории(переместил файл)

# os.renames('text.txt', 'test1/test1.txt')  # переименовывает файл или директорию, создавая промежуточные директории
# # (переместил файл)

# os.rmdir('test1') # удаляет пустую директорию

# for root, dirs, files in os.walk('test'):
#     print('root', root)

# for root, dirs, files in os.walk('test', topdown=True):  # возвращает имена объектов в виде дерева директорий.
# # Для каждой директории возвращает картеж (root - путь к директории, dirs - список директорий, files - список файлов)
#     print('root', root)
#     print('   Subdirs', dirs)
#     print('   files', files)


# def remove_empty_dirs(root_tree):
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f'Директория {root} удалена.')
#
#
# remove_empty_dirs('test')

# print(os.path.split(r'D:\PythonAcademy\test\nested2\nested3'))  # разбивает путь на кортеж ( head, tail), -
# # последний компонет пути, head - все остальное

# print(os.path.split(r'D:\PythonAcademy\test\nested2\nested3\\'))

# print(os.path.split(r'D:\PythonAcademy\test\nested2\nested3')[1])
# print(os.path.dirname(r'D:\PythonAcademy\test\nested2\nested3'))  # возвращает имя директории (+ путь)
# print(os.path.basename(r'D:\PythonAcademy\test\nested2\nested3'))  # возвращает имя файла

# print(os.path.join('files', '\pythonProject1', 'dir', 'three.txt'))

# dirs = ['Work/F1', 'Work/F2/F21']
# for d in dirs:
#     os.makedirs(d)

# files = {'Work': ['w.txt'],
#         'Work/F1': ['F11.txt', 'F12.txt', 'F13.txt'],
#         'Work/F2/F21': ['F211.txt', 'F211.txt', 'F212.txt']
#         }
#
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         open(file_path, 'w').close()
#
# file_text = ['Work/w.txt', 'Work/F1/F12.txt','Work/F2/F21/F211.txt', 'Work/F2/F21/F212.txt']
# for file in file_text:
#     with open(file, 'w') as f:
#         f.write(f'Текст для файла по пути {file}')

# 06.12.2022 =========================================================================================

# решение к коду выше _______________


# def print_tree(root, td):
#     print(f'Обход {root} {"сверху вниз" if td else "снизу вверх"}')
#     for root, dirs, fl in os.walk(root, topdown=td):
#         print(root)
#         print(dirs)
#         print(fl)
#     print('-' * 50)
#
#
# print_tree('Work', td=False)
# print_tree('Work', td=True)

# ---------------------------------------

# print(os.path.exists(r'D:\PythonAcademy\Work'))  # проверяет наличие файла или папки по указанному пути
# print(os.path.getatime(path))  # возвращает время последнего доступа к файлу в секундах
# print(os.path.getctime(path))  # возвращает время создания файла
# print(os.path.getmtime(path))  # возвращает время последнего изменения файла

# print(os.path.getsize(path))  # возвращает размер файла в байтах

# import time
#
# path = 'two.txt'
#
# size = round(os.path.getsize(path) / 1024, 2)
# print(size)
# t = os.path.getctime(path)
# print(time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(t)))

# print(os.path.isfile(r'Work\w.txt'))  # возвращает True, если путь является файлом
# print(os.path.isdir(r'Work'))  # возвращает True, если путь является папкой

# Обьектно-ориентированое програмирование --------------------------------------------------

# свойства (поля: переменные)

# class Point:
#     """Класс для представления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#
# # print(Point.__doc__)
# # print(Point.__name__)
# # print(dir(Point))
#
# p1 = Point()
# p2 = Point()
# print('p1 =', p1.x)
# print('Point =', Point.x)
# # print(type(p1))
# p1.x = 100
# p2.x = 200
# print('p1 =', p1.x)
# print('p2 =', p2.x)
# print('Point =', Point.x)
# # print(id(p1))
# # print(id(p2))
# # print(id(Point))
# Point.y = 300
# print('p1 =', p1.y)
# print('p2 =', p2.y)
# print('Point =', Point.y)

# class Point:
#     x = 1
#     y = 1
#
#
# p1 = Point()
# p1.x = 5
# p1.y = 10
# p1.z = 20
# print(p1.x, p1.y)
# print(p1.__dict__)
# print(Point.__dict__)

# методы (функция)----
# атрибуты = свойства + методы

# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self):
#         print(self.__dict__)
#         # print('Метод set_coord')
#
#
# p1 = Point()
# print(p1.x)
# p1.x = 5
# p1.y = 10
# p1.set_coord()
# # Point.set_coord(p1)  # редко используется
# p2 = Point()
# p2.x = 2
# p2.y = 7
# p2.set_coord()

# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()
# p1.set_coord(5, 10)
# print(p1.__dict__)
# print(p1.x)
# p2 = Point()
# p2.set_coord(2, 7)
# print(p2.__dict__)
# print(p2.x)
# Point.set_coord(p2, 5, 10)
# print(p2.__dict__)

# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     address = 'street, house'
#
#     def print_info(self):
#         print(' Персональные данные '.center(40, '*'))
#         print(f'Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n'
#               f'Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}')
#         print('=' * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # установить имя
#         if isinstance(name, str):
#             self.name = name
#
#     def set_birthday(self, bth):
#         self.birthday = bth
#
#     def get_name(self):  # получить имя
#         return self.name
#
#     def get_birthday(self):
#         return self.birthday
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info('Юля', '23.05.1986', "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name('Алевтина')
# h1.print_info()
#
# # h1.set_birthday('23.01.1987')
# print(h1.get_birthday())

# 08.12.2002 ==========================================================================================

# конструктор (__new__)
# инициализатор (__init__)
# диструктор (__del__)

# class Person:
#     skill = 10
#
#     def __init__(self, name, surname):
#         self.surname = surname
#         self.name = name
#
#     def print_info(self):
#         print('Данные сотрудника: ', self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print('Квалификация сотрудника: ', self.skill, '\n')
#
#
# p1 = Person('Viktor', 'Reznik')
# p1.print_info()
# p1.add_skill(3)
#
# p2 = Person('Anna', 'Dolgih')
# p2.print_info()
# p2.add_skill(2)

# class Point:
#     # def __new__(cls, *args, **kwargs):
#     #     print('Конструктор')
#     #     return super().__new__(cls)
#
#     def __init__(self, x, y):
#         print('Инициализатор')
#         self.x = x
#         self.y = y
#
#     def __del__(self):
#         print('Удаление экземпляра', self.__class__.__name__)
#
#     def print_coord(self):
#         print(f'x: {self.x}, y: {self.y}')
#
#
# p1 = Point(5, 10)
# p1.print_coord()
# print(id(p1))
#
# p2 = Point(2, 7)
# p2.print_coord()
# print(id(p2))

# свойства:
#   - статические
#   - динамические

# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# print(p1.count)
# p2 = Point(2, 7)
# print(p2.count)
# # print('->', Point.count)
# p3 = Point(3, 4)
# # print(p3.count)
#
# print(id(p1.count))
# print(id(p2.count))
# print(id(p3.count))
# print(id(Point.count))

# class Robot:
#     count = 0
#
#     def __init__(self, name):
#         self.name = name
#         print('Инициализация робота: ', self.name)
#         Robot.count += 1
#
#     def __del__(self):
#         print(f'{self.name}, выключается')
#         Robot.count -= 1
#         if Robot.count == 0:
#             print(self.name, 'был последним')
#         else:
#             print('Работающих роботов осталось: ', Robot.count)
#
#     def say_hi(self):
#         print('Приветствую, меня зовут', self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print('Численность роботов:', Robot.count)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print('Численность роботов:', Robot.count)
#
# droid3 = Robot('C-322')
# droid3.say_hi()
# print('Численность роботов:', Robot.count)
#
# print('\nЗдесь роботы могут проделать какую-то работу\n')
# print('Роботы закончили свою работу, давайте их выключим')
# del droid1  # либо droid1 = 0
# del droid2
# del droid3
# print('Работающих роботов осталось: ', Robot.count)

# Модификаторы доступа:
#   public (self.x) - публичное свойство (открытое)
#   protected (self._x) - используется при наследовании
#   private (self.__x) - закрытые свойства

# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x  # _Point__x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print('Координаты должны быть числами')
#
#     def get_cord(self):
#         return self.__x, self.__y
#
#
# p1 = Point('5', 10)
# p1._Point__x = 111
# # print(p1.get_cord())
# # p1.set_coord(1, 2)
# # print(p1.get_cord())
# # print(p1.__dict__)
#
# # p1.__x = 100
# # p1.__y = 'abc'
# # print(p1.__x, p1.__y)
# print(p1.__dict__)

# 13.12.2022 ============================================================================================

# class Point:
#     __slots__ = ['__x', '__y', 'z']
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x  # _Point__x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print('Координаты должны быть числами')
#
#     def get_cord(self):
#         return self.__x, self.__y
#
#
# p1 = Point('5', 10)
# p1.z = 15
# print(p1.z)
# # print(p1.__dict__)

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __set_x(self, x):  # устанавливаем
#         print('Вызов __set.x')
#         self.__x = x
#
#     def __get_x(self):  # получаем
#         print('Вызов __get_x')
#         return self.__x
#
#     def __del_x(self):
#         print('Удаление свойства')
#         del self.__x
#
#     x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x
# print()

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):  # получаем  __get_x
#         print('Вызов __get_x')
#         return self.__x
#
#     @x.setter
#     def x(self, x):  # устанавливаем   __set_x
#         print('Вызов __set.x')
#         self.__x = x
#
#     @x.deleter
#     def x(self):  # __del_x
#         print('Удаление свойства')
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# # print(p1.__dict__)
# print(p1.x)
# # del p1.x

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются только числами')
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, 'кг =>', end=' ')
# print(weight.to_pounds(), 'фунтов')
# weight.kg = 41
# print(weight.kg, 'кг =>', end=' ')
# print(weight.to_pounds(), 'фунтов')
# weight.kg = '41'

# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, new_age):
#         self.__age = new_age
#
#     @age.deleter
#     def age(self):
#         del self.__age
#
#
# p1 = Person('Irina', 26)
# print(p1.name, p1.age)
# p1.name = 'Igor'
# p1.age = 31
# print(p1.name, p1.age)
# del p1.age

# class Point:
#     __count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count)  # старый метод
#
#
# p1 = Point(5, 10)
# p2 = Point(4, 8)
# p3 = Point(2, 7)
# print(Point.get_count())
# print(p1.get_count())

# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))

# class Args:
#     @staticmethod
#     def min(*args):
#         return min(args)
#
#     @staticmethod
#     def max(*args):
#         return max(args)
#
#     @staticmethod
#     def arf(*args):
#         return sum(args) / len(args)
#
#     @staticmethod
#     def f(x):
#         one = 1
#         for i in range(1, x + 1):
#             one *= i
#         return one
#
#
# print(Args.min(3, 5, 7, 9))
# print(Args.max(3, 5, 7, 9))
# print(Args.arf(3, 5, 7, 9))
# print(Args.f(5))

# class Numbers:
#     @staticmethod
#     def max(*args):
#         max1 = 0
#         for i in args:
#             max1 = max1 if i < max1 else i
#         return max1
#
#
# print(Numbers.max(3, 5, 7, 9, 4, 16, 1))

# class Date:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):
#         day, month, year = map(int, date_as_string.split('.'))
#         date1 = cls(day, month, year)
#         return date1
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.day}'
#
#
# string_date = Date.from_string('23.10.2022')
# print(string_date.string_to_db())
# string_date1 = Date.from_string('23.12.2021')
# print(string_date1.string_to_db())

# 15.12.2022 ======================================================================================

# ---------------------------------------------------------------
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счёта: {eur_val} {Account.suffix_eur}')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.value} {Account.suffix}')
#
#     def print_info(self):
#         print('Информация о счете')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
#
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
#
# print()
# acc.edit_owner('Дюма')
# acc.print_info()
#
# print()
# acc.add_percents()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
#
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# -------------------------------------------------------------

# import re
#
#
# class UserData:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         # self.verify_weight(weight)
#         # self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.password = ps
#         self.weight = weight
#
#     @staticmethod
#     def verify_fio(fio):
#         if not isinstance(fio, str):
#             raise TypeError('ФИО должно быть строкой')
#         f = fio.split()  # ['Волков', 'Игорь', 'Николаевич']
#         if len(f) != 3:
#             raise TypeError('Неверный формат ФИО')
#             # ['В', 'о', 'л', 'к', 'о', 'в', 'И', 'г',
#         # 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
#         letters = ''.join(re.findall('[a-zа-яё-]', fio, flags=re.IGNORECASE))  # ВолковИгорьНиколаевич
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError('В ФИО можно использовать только буквы и дефис')
#
#     @staticmethod
#     def verify_old(old):
#         if not isinstance(old, int) or old < 14 or old > 120:
#             raise TypeError('Возраст должен быть числом в диапазоне от 14 до 120 лет')
#
#     @staticmethod
#     def verify_weight(w):
#         if not isinstance(w, float) or w < 20:
#             raise TypeError('Вес должен быть вещественным числом от 20 кг и выше')
#
#     @staticmethod
#     def verify_ps(ps):
#         if not isinstance(ps, str):
#             raise TypeError('Паспорт должен быть строкой')
#         s = ps.split()  # ['1234', '567890']
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError('Не верный формат паспорта')
#         for i in s:
#             if not i.isdigit():
#                 raise TypeError('Серия и номер паспорта должны быть числами')
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#
# p1 = UserData('Волков Игорь Николаевич', 26, '1234 567890', 80.8)
# # p1.fio = 'Сидоров Игорь Николаевич'
# # print(p1.fio)
# # print(p1.__dict__)

# 20.12.2022 ============================================================================================

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f'({self.__x}, {self.__y})'
#
#
# # print(issubclass(Point, object))
# # print(dir(Point))
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1) -> None:
#         print('Инициализатор базового класса')
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):
#     def __init__(self, *args):
#         print('Переопределенный инициализатор Line')
#         # Prop.__init__(self, *args)
#         super().__init__(*args)
#
#     def draw_line(self):
#         # print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.get_width()}')
#
#
# class Rect(Prop):
#     def __init__(self, *args, bg='yellow'):
#         super().__init__(*args)
#         self._background = bg
#
#     def draw_rect(self):
#         print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.get_width()}, {self._background}')
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# Line.draw_line(line)
# # print(line._color)
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()
#
# # DRY (Don`t Repeat Youself) - не повторяйся

# 22.12.2022 ===============================================================================

# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     def __str__(self):
#         return f'{self.__color}'
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return f'{self.__width}, {self.__height}, {self.color}'
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError('Ширина должна быть положительное число')
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError('Высота должна быть положительное число')
#
#     def area(self):
#         return self.__width * self.__height
#
#
# rect = Rectangle(10, 20, 'green')
# print(rect.width)
# print(rect.height)
# print(rect.color)
# rect.color = 'red'
# print(rect)
# rect.width = 5
# print(rect)
# print(rect.area())

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f'===Прямоугольник===\nШирина: {self.width}\nВысота: {self.height}')
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         self.fon = background
#         super().__init__(width, height)
#
#     def show_rect(self):
#         super().show_rect()
#         print('Фон:', self.fon)
#
#
# # class RectBorder(Rect):
# #     def __init__(self, width, height, border):
# #         self.border = border
# #         super().__init__(width, height)
# #
# #     def show_rect(self):
# #         super().show_rect()
# #         print('Рамка:', self.border)
#
# class RectFonBorder(RectFon):
#     def __init__(self, width, height, background, border):
#         super(RectFonBorder, self).__init__(width, height, background)
#         self.border = border
#
#     def show_rect(self):
#         super(RectFonBorder, self).show_rect()
#         print('Рамка:', self.border)
#
#
# shape = Rect(100, 200)
# shape.show_rect()
# print()
# shape1 = RectFon(400, 300, 'yellow')
# shape1.show_rect()
# # shape2 = RectBorder(600, 500, '1px solid red')
# # shape2.show_rect()
# shape3 = RectFonBorder(600, 500, 'yellow', '1px solid red')
# shape3.show_rect()

# class Vector(list):
#     def __str__(self):
#         return ' '.join(map(str, self))
#
#
# v = Vector([1, 2, 3])
# print(v)
# print(type(v))

# перегрузка методов ---------------------------------------------------------

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print('Координаты должны быть целочисленными')
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#
# class Line(Prop):
#
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def set_coord(self, sp, ep=None):
#         if ep is None:
#             if sp.is_int():
#                 self._sp = sp
#         else:
#             if sp.is_int() and ep.is_int():
#                 self._sp = sp
#                 self._ep = ep
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coord(Point(20, 40), Point(50, 60))
# line.draw_line()
# line.set_coord(Point(100, 240))
# line.draw_line()

# Абстрактные методы ------------------------------

# class Point:
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
#     def is_int(self):
#         if not isinstance(self.__x, int) or not isinstance(self.__y, int):
#             print('Координаты должны быть целочисленными')
#             return False
#         return True
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def draw_line(self):
#         raise NotImplementedError('В дочернем классе должен быть определен метод draw()')
#
#
# class Line(Prop):
#     # def draw_line(self):
#     #     print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#     pass
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()

# 27.12.2022 ==========================================================================================

# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):  # 20
#         if radius is None:
#             if length is None:
#                 self._width = self._length = width
#                 # width = self._width = self._length  # не будет работать
#             else:
#                 self._width = width
#                 self._length = length
#         else:
#             self._radius = radius
#
#     def calc_area(self):
#         pass
#
#
# class SqTable(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class RoundTable(Table):
#     def calc_area(self):
#         return round(pi * self._radius ** 2, 2)
#
#
# tt = Table()
#
#
# # t = SqTable(20, 10)
# # print(t.__dict__)
# # print(t.calc_area())
# #
# # t2 = SqTable(20)
# # print(t2.__dict__)
# # print(t2.calc_area())
# #
# # t1 = RoundTable(radius=20)
# # print(t1.__dict__)
# # print(t1.calc_area())

# from abc import ABC, abstractmethod
#
#
# class Chess(ABC):
#     def draw(self):
#         print('Нарисовал шахматную фигуру')
#
#     @abstractmethod
#     def move(self):
#         print('Родитель')
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print('Переместил шахматную фигуру')
#
#
# q = Queen()
# q.draw()
# q.move()


# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     #  @abstractmethod можно поставить, хотя и не обязательно
#     def print_value(self):
#         print(self.value, end=' ')
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = 'USD'
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super(Dollar, self).print_value()
#         print(Dollar.suffix, end=' ')
#
#
# class Eur(Currency):
#     rate_to_rub = 90.14
#     suffix = 'EUR'
#
#     def convert_to_rub(self):
#         rub = self.value * Eur.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Eur.suffix, end=' ')
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# print('*' * 50)
# for i in d:
#     i.print_value()
#     print(f'= {i.convert_to_rub():.2f} RUB')
#
# print('*' * 50)
# e = [Eur(5), Eur(10), Eur(50), Eur(100)]
# for i in e:
#     i.print_value()
#     print(f'= {i.convert_to_rub():.2f} RUB')


# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print('Дочерний класс')
#
#
# class GrandChild(Child):
#     def display2(self):
#         print('Внучатый класс')
#
#
# gc = GrandChild()
# gc.display2()
# gc.display1()


# Вложенные классы ---------------------------------------------------------------------

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @staticmethod
#     def outer_class_method():
#         print('Я - метод внешнего класса')
#
#     def outer_obj_method(self):
#         print('Связующий метод')
#
#     class MyInner:
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print('Я - метод вложенного класса', MyOuter.age)
#             MyOuter.outer_class_method()
#             self.obj.outer_obj_method()
#
#
# out = MyOuter('внешний')
# inner = out.MyInner('внутренний', out)
# print(inner.inner_name)
# inner.inner_method()

# class Color:
#     def __init__(self):
#         self.name = 'Green'
#         self.lg = self.LightGreen()
#
#     def show(self):
#         print('Name', self.name)
#
#     class LightGreen:
#         def __init__(self):
#             self.name = 'Light green'
#             self.code = '024avc'
#
#         def display(self):
#             print('Name:', self.name)
#             print('Name:', self.code)
#
#
# outer = Color()
# outer.show()
#
# g = outer.lg
# g.display()


# 29.12.2022 ============================================================================

# class Employee:
#     def __init__(self):
#         self.name = 'Employee'
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print('Name:', self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = 'Smith'
#             self.id = '657'
#
#         def display(self):
#             print('Name:', self.name)
#             print('Id:', self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = 'Alba'
#             self.id = '007'
#
#         def display(self):
#             print('Name:', self.name)
#             print('Id:', self.id)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# print()
# d1.display()
# print(d1.id)
#
# d2 = outer.head
# print()
# d2.display()

# class Computer:
#     def __init__(self, name, os1, brand):
#         self.name = name
#         self.os = self.OS(os1)
#         self.cpu = self.CPU(brand)
#
#     class OS:
#         def __init__(self, title):
#             self.title = title
#
#         def system(self):
#             return self.title
#
#     class CPU:
#         def __init__(self, brand):
#             self.brand = brand
#
#         def make(self):
#             return self.brand
#
#         def model(self, model):
#             return model
#
#
# comp = Computer('PC001', 'Windows-7', 'Intel')
# my_os = comp.os
# my_cpu = comp.cpu
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model('Core-i7'))

# class Base:
#     def __init__(self):
#         self.db = self.Inner()
#
#     def display(self):
#         print('In Base Class')
#
#     class Inner:
#         def display1(self):
#             print('Inner of Base Class')
#
#
# class SubClass(Base):
#     def __init__(self):
#         print('In SubClass')
#         super().__init__()
#
#     class Inner(Base.Inner):
#         def display2(self):
#             print('Inner of SubClass')
#
#
# a = SubClass()
# a.display()
#
# b = a.db
# # b = SubClass.Inner()
# b.display1()
# b.display2()

# Множественное наследование ---------------------------------------

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + ' is sleeping')
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + ' is playing')
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + ' is barking')
#
#
# beast = Dog('Buddy')
# beast.bark()
# beast.play()
# beast.sleep()

# class A:
#     def __init__(self):
#         print('A')
#
#
# class AA:
#     pass
#
#
# class B(A):
#     # def __init__(self):
#     #     print('B')
#
#     def hi(self):
#         print('B_hi')
#
#
# class C(AA):
#     # def __init__(self):
#     #     print('C')
#
#     def hi(self):
#         print('C_hi')
#
#
# class D(B, C):
#     # def __init__(self):
#     #     B.__init__(self)
#     #     C.__init__(self)
#     #     print('D')
#
#     def hi(self):
#         C.hi(self)
#         print('D_hi')
#
#
# d = D()
# d.hi()
# print(D.mro())
# print(D.__mro__)


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#
# class Style:
#     def __init__(self, color='red', width=1):
#         print('Инициализатор Style')
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point):
#         print('инициализатор Pos')
#         self._sp = sp
#         self._ep = ep
#
#
# class Line(Pos, Style):
#     def __init__(self, sp: Point, ep: Point, color='red', width=1):
#         Pos.__init__(self, sp, ep)
#         Style.__init__(self, color, width)
#
#     def draw(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x}, {self.y})'
#
#
# class Style:
#     def __init__(self, color='red', width=1):
#         print('Инициализатор Style')
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print('инициализатор Pos')
#         self._sp = sp
#         self._ep = ep
#         super().__init__(*args)
#
#
# class Line(Pos, Style):
#     # def __init__(self, sp: Point, ep: Point, color='red', width=1):
#     #     Pos.__init__(self, sp, ep)
#     #     Style.__init__(self, color, width)
#
#     def draw(self):
#         print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}')
#
#
# l1 = Line(Point(10, 10), Point(100, 100), 'green', 5)
# l1.draw()
# print(Line.mro())
# print(Point.mro())


# Миксин (примеси) ----------------------------------------------------------------------

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclass.txt')
#
#
# sub = MySubClass()
# sub.display('Строка будет отображаться и регистрироваться в файле')
# print(MySubClass.mro())

print('hj')
