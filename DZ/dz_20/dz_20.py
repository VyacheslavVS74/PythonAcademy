import re

# 1я Задача ---------------------------------------------------------------

# s = "my-p@ssw0rd"


# def log(a):
#     return re.findall(r'^[A-z0-9@-]{6,18}$', a)
#
#
# print(log('my-p@ssw0rd'))
#
# # 2я Задача, вроде получилось -----------------------------------------------
#
n = "MMDCCLXXIII"
n1 = "CCCMMVIIVV"


def num(a):
    # return re.findall(r'(M|C|X|I|)*', a)
    # reg = re.findall(r'^M{0,3}(C{0,3}D?|CM|DC)?(X{0,3}L?|XC|LX)?(I{0,3}V?|IX|IV)?$', a)
    reg = re.findall(r'^M{0,3}(CM|CD|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$', a)
    # print(reg)
    if reg:
        print(a, '- это римское число')
    else:
        print(a, '- это не римское число')


num(n)
num(n1)

