# Первая задача--------------------------------------------------------------------------

# a, b, c = {1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}
# # s = a.copy()
# # s.update(b)
# # s.update(c)
# s = a | b | c
# print(s)

# Вторая задача---------------------------------------------------------------------------

# s = {'emp1': {'name': 'John', 'salary': 7500},
#      'emp2': {'name': 'Emma', 'salary': 8000},
#      'emp3': {'name': 'Brad', 'salary': 6500}}
# print(s['emp3'], s['emp3']['salary'], sep='\n')
#
# for i in s:
#      print(i)
#      for j in s[i]:
#           if s[i][j] == 6500:
#                s[i][j] = 8500
#           print(j, ':', s[i][j], sep=' ')

# Третья задача---------------------------------------------------------------------

# col = int(input("Кол-во студентов: "))
# d = {}
# s = 0
# for i in range(col):
#     name = input('Студент: ')
#     d[name] = int(input('Балл: '))
# for j in d.values():
#     s += j
# res = round(s / col)
# print('Средний балл: ', res, '. ', 'Студенты с баллом выше среднего:', sep='')
# for key, value in d.items():
#     if value > res:
#         print(key)
# # print(d.values())
# # print(d)


