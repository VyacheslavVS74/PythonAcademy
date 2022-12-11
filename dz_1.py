# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# a = list(enumerate(seasons))
# print(a)

# a = 2
# b = 2
# c = '-'
# # print(eval(f'a + {c} + b'))
# print(eval(f'a + {c} + b'))

# a, b, c = 'Москва', 'Санкт-Петербург', 'Екатеринбург'
# print(min(a, b, c, key=len ))
# print(max(a, b, c, key=len ))

# a = 3
# b = 9
# c = round((a ** 2 + b ** 2) ** 0.5, 2)
# print(c)

rows = 3
cols = 9
print(rows)
print(cols)
for x in range(rows):
    for y in range(cols):
        print("*", end='')
    print()