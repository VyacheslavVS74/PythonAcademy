# Задача 1========================================================================================

# a = (input('Введите по порядку, без пробелов, элементы списка: '))
# tpl = tuple(a)
# print(tpl)
# lst = list(tpl)
# col = []
# for i in lst:
#     if i not in col:
#         print('Количество', i, '=', tpl.count(i))
#         col.append(i)


# Задача 2========================================================================================

# a = ('ab', 'abcd', 'cde', 'abc', 'def')
# print(a)
# lst = list(a)
# s = input("Введите искомый элемент: ")
# for i in a:
#     if i == s:
#         print('Yes')


# Задача 3========================================================================================

# print(2, 7, 0, 3, 1, 5, -13)  # ->no,  7 значений
# print(2, 7, 0, 3, 1, 5, -13)  # ->13,  7 значений
# print(26)  # ->26,  1 значений
# print(99, 99, 100, 34, -39)  # ->no,  5 значений
# print(99, 39, 99, 100, 34)  # ->39,  5 значений

# lst = [int(input('->')) for i in range(int(input('Введите кол-во значений: ')))]
#
#
# def t():
#     max1 = 0
#     for i in lst:
#         if i % 13 == 0 and i != 0:
#             if i > max1:
#                 max1 = i
#                 return max1
#             else:
#                 return 'no such numbers'
#
#
# res = t()
# print(res)




# def s_input():  # ВАРИАНТ
#     l = []
#     for i in set(input("Запишите через запятую в строку целые числа.").split(",")):
#         l.append(int(i))
#
#     l.sort()
#     return tuple(l)
#
#
# def s_input2():
#     l = []
#     b, d = 0, 1
#     c = list(input("Запишите через запятую в строку целые числа."))
#     for i in c:
#         if i == '-':
#             d *= -1
#             continue
#         try:
#             b = b * 10 + int(i)
#         except ValueError:
#             l.append(b * d)
#             b, d = 0, 1
#     l.append(b)
#     l.sort()
#     l = set(l)
#     print(l)
#     return tuple(l)
#
#
# def l13_max(sett: set):
#     smax = False
#     for i in sett:
#         smax = (i if i > smax and i % 13 == 0 and i > 0 else smax)
#     if smax == False:
#         smax = "NO NUMS"
#     return (smax)
#
#
# print(l13_max(s_input2()))
# print()
# print()
# print('Задание 2')
# print()
# s = input("Введите искомый элемент")
#
# t = ('ab', 'abcd', 'cde', 'def')
# print("Исходный кортеж", t)
# if s in t:
#     print("Yes")
# else:
#     print("No")
# print()
# print()
#
# print("Задание 3")
# print()
#
# str = input('Введите по порядку, без пробелов,элементы кортежа')
#
#
# def str_to_spis(strr):
#     a = list(strr)
#
#     a1, a2 = [], []  # Знак и количество
#     for i in a:
#         if i in a1:
#
#             for j in range(len(a1)):
#                 if a1[j] == i:
#                     a2[j] += 1
#         else:
#             a1.append(i)
#             a2.append(1)
#     return (a1, a2)
#
#
# def print_spis(bb):
#     bb1, bb2 = bb
#     print("Статистика частотности символов")
#     for i in range(len(bb1)):
#         print("Количество ", bb1[i], " = ", bb2[i])
#
#
# print_spis(str_to_spis(str))

# def find_max(lst):
#     max_elem = 0
#     for i in lst:
#         if i % 13 == 0:
#             max_elem = i
#     if max_elem > 0:
#         return max_elem
#     else:
#         return 'No Such number'
# lst = [int(input('->')) for i in range(int(input('введите количество символов')))]
# print(find_max(lst))


# def find_max(lst):
#     max_elem = 0
#     for i in lst:
#         if i % 13 == 0:
#             max_elem = i
#     if max_elem > 0:
#         return max_elem
#     else:
#         return 'No Such number'
#
#
# lst = [int(input('->')) for i in range(int(input('введите количество символов')))]
# print(find_max(lst))