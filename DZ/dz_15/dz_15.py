# Первая задача =========================================================

print((lambda a, b, c: a * b * c)(2, 5, 5))

# второй вариант ------------------------------------------------
# col = int(input('введите количество элементов: '))
# comp = 1
# for i in range(col):
#     n = int(input(str(i + 1) + '-й элемент: '))
#     comp *= n
# print(comp)

# Вторая задача ==========================================================

# stud = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
#
# n = sorted(stud, key=lambda s: s['name'])
# print(n)
# # print('stud = ', stud)
# f = sorted(stud, key=lambda s: s['final'], reverse=True)
# print(f)

# Третья задача ==========================================================

# stud = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
#
# maximum = max(stud, key=lambda i: i['final'])
# print(maximum)
# minimum = min(stud, key=lambda i: i['final'])
# print(minimum)

# По ТЗ -------------------------------------------------------------------

# stud = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98}
# ]
# maximum = sorted(stud, key=lambda i: i['final'], reverse=True)
# print(maximum[0])
# minimum = sorted(stud, key=lambda i: i['final'])
# print(minimum[0])

# Четвертая задача ========================================================

# num = [3, 5, 7, 3, 9, 5, 7, 2]
#
# print(list(map(lambda i: i ** 2, num)))
# print(list(map(lambda i: i ** 3, num)))
