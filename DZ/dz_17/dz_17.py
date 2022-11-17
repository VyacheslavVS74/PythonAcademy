# # 1й вариант ------------------------------------------
def func(fn):
    print(bin(fn)[2:])
    # return bin(fn)[2:]


n = int(input("-> "))
for i in range(int(n)):
    if n != 0:
        func(n)
        n = int(input("-> "))
    else:
        break

# # 2й вариант -----------------------------------------------
# def func(fn):
#     st = ''
#     while fn > 0:
#         st = str(fn % 2) + st
#         fn = fn // 2
#     return st
#
#
# while True:
#     n = int(input('-> '))
#     if n != 0:
#         print(func(n))
#     else:
#         break
