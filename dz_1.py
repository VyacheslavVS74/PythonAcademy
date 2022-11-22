# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# a = list(enumerate(seasons))
# print(a)

# a = 2
# b = 2
# c = '-'
# # print(eval(f'a + {c} + b'))
# print(eval(f'a + {c} + b'))

a, b, c = 'Москва', 'Санкт-Петербург', 'Екатеринбург'
print(min(a, b, c, key=len ))
print(max(a, b, c, key=len ))