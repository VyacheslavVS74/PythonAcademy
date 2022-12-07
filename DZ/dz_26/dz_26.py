import os
# 1 задача

text1 = 'Первый файл1\nПервый файл2\nПервый файл3\n'
text2 = 'Второй файл1\nВторой файл2\nВторой файл3\n'
with open('dz1.txt', 'w') as f:
    f.write(text1)
with open('dz2.txt', 'w') as f:
    f.write(text2)

tree_file = 'dz3.txt'
with open('dz1.txt', 'r') as fr1, open('dz2.txt', 'r') as fr2, open(tree_file, 'w') as fw:
    for i in fr1:
        fw.write(i)
    for j in fr2:
        fw.write(j)


# 2 задача

# dirs = ['Work/F1', 'Work/F2/F21']
# for d in dirs:
#     os.makedirs(d)

# files = {'Work': ['w.txt'],
#          'Work/F1': ['F11.txt', 'F12.txt', 'F13.txt'],
#          'Work/F2/F21': ['F211.txt', 'F211.txt', 'F212.txt']
#          }
#
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         open(file_path, 'w').close()
#
# file_text = ['Work/w.txt', 'Work/F1/F12.txt', 'Work/F2/F21/F211.txt', 'Work/F2/F21/F212.txt']
# for file in file_text:
#     with open(file, 'w') as f:
#         f.write(f'Текст для файла по пути {file}')
#
#
# def print_tree(root, td):
#     print(f'Обход {root} {"сверху вниз" if td else "снизу вверх"}')
#     for root, dirs, fl in os.walk(root, topdown=td):
#         print(root)
#         print(dirs)
#         print(fl)
#     print('-' * 50)
#
#
# print_tree('Work', td=False)
# print_tree('Work', td=True)
