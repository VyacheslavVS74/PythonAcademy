#   # Первое задание
# while True:
#     print("*** 97531 ***")
#     num = int(input("Введите пятизначное число: "))
#     # if num <= 99999 and num >= 10000:
#     if 99999 >= num >= 10000:
#         a = num % 10
#         # print(a)
#         num = num // 10
#         b = num % 10
#         num = num // 10
#         # print(b)
#         c = num % 10
#         num = num // 10
#         # print(c)
#         d = num % 10
#         num = num // 10
#         # print(d)
#         e = num % 10
#         num = num // 10
#         # print(e)
#         f = a * b * c * d * e
#         g = (a + b + c + d + e) / 5
#         print("Произведение цифр введенного числа: ", f)
#         print("Среднее арифметическое: ", g)
#     else:
#         print("Введите корректное число")


#  # Второе задание
# while True:
#     print("*** пусть будет ***")
#     num1 = int(input("Введите целое число: "))
#     if num1 % 2 == 0:
#         print("Число ", num1, " - четное")
#     else:
#         print("Число ", num1, " - нечетное")


#  # Третье задание
# while True:
#     what = input("Выберите операцию (r, +, -, /, *, %, <, >)")
#     if what == "+":
#         a = float(input("Введите первое число: "))
#         b = float(input("Введите второе число: "))
#         d = a + b
#         print("Ответ: ", d)
#     elif what == "-":
#         a = float(input("Введите первое число: "))
#         b = float(input("Введите второе число: "))
#         d = a - b
#         print("Ответ: ", d)
#     elif what == "/":
#         a = float(input("Введите первое число: "))
#         b = float(input("Введите второе число: "))
#         if b == 0:
#             print("На ноль делить нельзя!")
#         else:
#             d = a / b
#             print("Ответ: ", d)
#     elif what == "*":
#         a = float(input("Введите первое число: "))
#         b = float(input("Введите второе число: "))
#         d = a * b
#         print("Ответ: ", d)
#     elif what == "%":
#         a = float(input("Введите первое число: "))
#         b = float(input("Введите второе число: "))
#         d = a % b
#         print("Ответ: ", d)
#     elif what == "<":
#         a = float(input("Введите первое число: "))
#         b = float(input("Введите второе число: "))
#         if a < b:
#             d = a
#             print("Ответ: ", d)
#         else:
#             d = b
#             print("Ответ: ", d)
#     elif what == ">":
#         a = float(input("Введите первое число: "))
#         b = float(input("Введите второе число: "))
#         if a > b:
#             d = a
#             print("Ответ: ", d)
#         else:
#             d = b
#             print("Ответ: ", d)
#
#         # d = (a > b) * a + (b > a) * b
#         # print("Ответ: ", d)
#         # # Нашел вот такой вариант поиска наибольшего (наим) значений, хотелось бы разобрать его с вами
#
#     elif what == "r":
#         c = float(input("Введите цифру: "))
#         c = -c
#         print("Ответ: ", c)
#     else:
#         print("Выбрана неверная операция!")


# # Четвертое задание
# while True:
#     a = (input("Введите число от 1 до 99: "))
#     if a[-2:] in ('11', '12', '13', '14'):
#         print(a, 'Копеек')
#     elif a[-1] == '1':
#         print(a, 'копейка')
#     elif a[-1] in ('2', '3', '4'):
#         print(a, 'копейки')
#     else:
#         print(a, 'копеек')

