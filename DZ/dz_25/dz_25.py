f = open('text2.txt', 'w')
f.write('Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать в список файл')
f.close()

f = open('text2.txt', 'r')
read_line = f.readlines()
print(read_line)
n = int(input("pos1: "))
n1 = int(input("pos2: "))
if 0 <= n < len(read_line):
    res = read_line[n]
    read_line[n] = read_line[n1]
    read_line[2] = res
else:
    print('Такой строки нет')
print(read_line)
f.close()

f = open('text2.txt', 'w')
f.writelines(read_line)
f.close()
