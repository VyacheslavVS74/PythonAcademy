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

# rows = 3
# cols = 9
# print(rows)
# print(cols)
# for x in range(rows):
#     for y in range(cols):
#         print("*", end='')
#     print()

# class ExampleClass:
#
#     def __init__(self, val=1):
#         self.__first = val
#
#     def setSecond(self, val):
#         self.__second = val
#
#
# exampleObject1 = ExampleClass()
# exampleObject2 = ExampleClass(2)
# exampleObject2.setSecond(3)
# exampleObject3 = ExampleClass(4)
# exampleObject3.__third = 5
# print(exampleObject1.__dict__)
# print(exampleObject2.__dict__)
# print(exampleObject3.__dict__)
#
# print(exampleObject1._ExampleClass__first)

# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.counter += 1
#
#
# exampleObject1 = ExampleClass()
# exampleObject2 = ExampleClass(2)
# exampleObject3 = ExampleClass(4)
# print(exampleObject1.__dict__, exampleObject1.counter)
# print(exampleObject2.__dict__, exampleObject2.counter)
# print(exampleObject3.__dict__, exampleObject3.counter)

# class ExampleClass:
#     __counter = 0
#
#     def __init__(self, val = 1):
#         self.__first = val
#         ExampleClass.__counter += 1
#
#
# exampleObject1 = ExampleClass()
# exampleObject2 = ExampleClass(2)
# exampleObject3 = ExampleClass(4)
# print(exampleObject1.__dict__, exampleObject1._ExampleClass__counter)
# print(exampleObject2.__dict__, exampleObject2._ExampleClass__counter)
# print(exampleObject3.__dict__, exampleObject3._ExampleClass__counter)


# class ExampleClass:
#     varia = 1
#
#     def __init__(self, val):
#         ExampleClass.varia = val
#
#
# print(ExampleClass.__dict__)
# print()
# exampleObject = ExampleClass(2)
# print(ExampleClass.__dict__)
# print(exampleObject.__dict__)

# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 2
#
#
# exampleObject = ExampleClass(1)
# print(exampleObject.a)
# try:
#     print(exampleObject.b)
# except AttributeError:
#     pass

# ----------------------------------------------------------
# class ExampleClass:
#
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 2
#
#
# exampleObject = ExampleClass(2)
# if hasattr(exampleObject, 'b'):
#     print(exampleObject.b)
# else:
#     print(exampleObject.a)


# class My:
#     attr1 = 'yes'
#
#
# my = My()
#
# print(hasattr(my, 'attr1'))

# class ExampleClass:
#     a = 1
#
#     def __init__(self):
#         self.b = 2
#
#
# exampleObject = ExampleClass()
# print(hasattr(exampleObject, 'b'))
# print(hasattr(exampleObject, 'a'))
# print(hasattr(ExampleClass, 'b'))
# print(hasattr(ExampleClass, 'a'))
# -----------------------------------------------------------

# class Classy:
#     varia = 1
#
#     def __init__(self):
#         self.var = 2
#
#     def method(self):
#         pass
#
#     def __hidden(self):
#         pass
#
#
# obj = Classy()
# print(obj.__dict__)
# print(Classy.__dict__)

# class SuperOne:
#     pass
#
#
# class SuperTwo:
#     pass
#
#
# class Sub(SuperOne, SuperTwo):
#     pass
#
#
# def printBases(cls):
#     print('( ', end='')
#
#     for x in cls.__bases__:
#         print(x.__name__, end=' ')
#     print(')')
#
#
# printBases(SuperOne)
# printBases(SuperTwo)
# printBases(Sub)

#------------------------------------------------
# class MyClass:
#     pass
#
#
# obj = MyClass()
# obj.a = 1
# obj.b = 2
# obj.i = 3
# obj.ireal = 3.5
# obj.integer = 4
# obj.z = 5
#
#
# def incIntsI(obj):
#     for name in obj.__dict__.keys():
#         if name.startswith('i'):
#             val = getattr(obj, name)
#             if isinstance(val, int):
#                 setattr(obj, name, val + 1)
#
#
# print(obj.__dict__)
# incIntsI(obj)
# print(obj.__dict__)
#-------------------------------------------------------

