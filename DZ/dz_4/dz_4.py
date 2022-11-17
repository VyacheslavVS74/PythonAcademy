# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# for i in range(a, b):
#     if i % 2 != 0:
#         print(i, end=" ")



i = 0
while True:

    a = int(input("Введите число от 1 до 100: "))
    c = 50
    if c < a and a > 0:
        i += 1
        print("Загаданное число меньше")
    if c > a and a > 0:
        i += 1
        print("Загаданное число больше")
    if a == 0:
        print("Вы сдались")
        break
    if c == a:
        print("Вы угадали загаданное число с", i, "раза")
        break
