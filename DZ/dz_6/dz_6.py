# Первая задача------------------------------------------------------------------------

a = []
b = []
n = int(input("Введите длину  списка: "))
for i in range(n):
    num = int(input("Введите элемент списка: "))
    a.append(num)
print("Список: ", a)


# for i in range(len(a)):
#     if a[i] > 0:
#         b.append(a[i])
# print("Новый список состоящий из положительных элементов: ", b)

for i in a:
    if i > 0:
        b.append(i)
print("Новый список состоящий из положительных элементов: ", b)

max = 0
for i in b:
    if i > max:
        max = i
print("Наибольший элемент списка: ", max)


# Вторая задача------------------------------------------------------------------------------

# a = []
# n = int(input("Введите длину списка:"))
# for i in range(n):
#     num = int(input("Введите элементы списка:"))
#     a.append(num)
# print(a)
# index = int(input("Введите индекс:"))
# num2 = int(input("Введите значение:"))
# a.insert(index, num2)
# print(a)


# Третья задача---------------------------------------------------------------------------------

# a = []
# n = int(input("Введите длину списка:"))
# for i in range(n):
#     num = int(input("Введите элементы списка:"))
#     a.append(num)
# b = int(input("Введите число:"))
# for i in a:
#     if i == b:
#         print("Число присутствует в элементах списка")


sp = [int(input('=>')) for i in range(int(input('Введите кол-во значений: ')))]
x = int(input('Введите число:'))
for i in range(len(sp)):
    if x == sp[i]:
        print('Это число есть в списке')
        break
else:
    print("No")

