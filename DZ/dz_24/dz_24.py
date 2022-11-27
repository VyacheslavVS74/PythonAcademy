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