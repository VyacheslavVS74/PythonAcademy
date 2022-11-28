# 1я Задача =================================================================

# def func(lst):
#     res = 0
#     for i in lst:
#         if i < 0:
#             res += 1
#     return res
#
#
# print(func([-2, 3, 8, -11, -4, 6]))


def func(n):
    if len(n) == 0:  # n == [] подчеркивает , но можно поставить - not n (наведя на подчеркивание)
        return 0  # len(n)
    elif n[0] < 0:
        return 1 + func(n[1:])
    else:
        return func(n[1:])


print('n =', func([-2, 3, 8, -11, -4, 6]))


# def func(n):
#     if len(n) == 0:
#         return 0  # len(n)
#     else:
#         res = func(n[1:])
#         if n[0] < 0:
#             res += 1  # return func(n[1:]) + 1 - не работает вместо второстепенной переменной
#         return res
#
#
# print('n =', func([-2, 3, 8, -11, -4, 6]))

# # Не работает, нет проверки на положительное число
# def func(n):
#     if len(n) == 0:
#         return 0  # len(n)
#
#     elif n[0] < 0:
#         return 1 + func(n[1:])
#
#
# print('n =', func([-2, 3, 8, -11, -4, 6]))

# 2я Задача =================================================================

# lst = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], 'Ann']
# res = 0
# for i in lst:
#     if isinstance(i, list):
#         for j in i:
#             if isinstance(j, list):
#                 for k in j:
#                     res += 1
#             else:
#                 res += 1
#     else:
#         res += 1
# print(res)


# # Добавлен еще один for, результат тот же
#
# lst = ['Adam', ["Bob", ["Chet", "Cat"], "Bard", "Bert"], 'Alex', ["Bea", "Bill"], 'Ann']
# res = 0
# for i in lst:
#     if isinstance(i, list):
#         for j in i:
#             if isinstance(j, list):
#                 for k in j:
#                     if isinstance(k, list):
#                         for d in k:
#                             res +=1
#                     else:
#                         res += 1
#             else:
#                 res += 1
#     else:
#         res += 1
# print(res)