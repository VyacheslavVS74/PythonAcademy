# 1 Задача-----------------------------------------------------------------------------------------
mas = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
# print(mas)
for i in range(len(mas)):
    for j in range(len(mas[i])):
        print(mas[i][j], end='\t')
    print()
print()

n, m = len(mas), len(mas[0])
matr = [[0] * n for a in range(m)]
# print(matr)
for i in range(n):
    for j in range(m):
        matr[j][i] = mas[i][j]

for row in matr:
    # print(row)
    for x in row:
        print(x, end='\t')
    print()


# 2 Задача -----------------------------------------------------------------------------------------------

# from random import *
#
# w, h = 6, 6
# matrix = [[randint(0, 10) for i in range(w)] for j in range(h)]
# # print(matrix)
# for row in matrix:
#     for x in row:
#         # sum += x
#         print(x, end='\t\t')
#     print()
# sp = [randint(0, 10) for j in range(h)]
# print(sp)
# print()
# # sum = 0
#
# for row in range(len(matrix)):
#     # if sum % 2:
#     #     matrix = sp
#     if row % 2 != 0:
#         for col in range(len(matrix[row])):
#             matrix[row] = sp
#             print(matrix[row-1][col], end='\t\t')
#         print()
#         for col in range(len(matrix[row])):
#             print(matrix[row][col], end='\t\t')
#         print()
# # print(sum)

