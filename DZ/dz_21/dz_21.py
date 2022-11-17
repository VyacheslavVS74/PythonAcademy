import re

d = input('Введите дату в формате dd-mm-yyyy: ')
# s = '28-08-2021'
reg = r'^([0-2][0-9]|[3][01])\-([0][0-9]|[1][0-2])\-(19[0-9][0-9]|20[0-9][0-9])$'
# print(re.findall(reg, d))
if re.findall(reg, d):
    print(re.findall(reg, d))
else:
    print('не верно введена дата!')
