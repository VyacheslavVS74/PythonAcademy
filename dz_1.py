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

# ------------------------------------------------
class MyClass:
    pass


obj = MyClass()
obj.a = 1
obj.b = 2
obj.i = 3
obj.ireal = 3.5
obj.integer = 4
obj.z = 5


def incIntsI(obj):
    for name in obj.__dict__.keys():
        if name.startswith('i'):
            val = getattr(obj, name)
            if isinstance(val, int):
                setattr(obj, name, val + 1)


print(obj.__dict__)
incIntsI(obj)
print(obj.__dict__)
# -------------------------------------------------------

# class Vehicle:
#     pass
#
#
# class LandVehicle(Vehicle):
#     pass
#
#
# class TrackedVehicle(LandVehicle):
#     pass
#
#
# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls1, cls2), end="\t")
#     print()


# class Vehicle:
#     pass
#
#
# class LandVehicle(Vehicle):
#     pass
#
#
# class TrackedVehicle(LandVehicle):
#     pass
#
#
# myVehicle = Vehicle()
# myLandVehicle = LandVehicle()
# myTrackedVehicle = TrackedVehicle()
# for obj in [myVehicle, myLandVehicle, myTrackedVehicle]:
#     for cls in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(isinstance(obj, cls), end="\t")
#     print()


# class SampleClass:
#     def __init__(self, val):
#         self.val = val
#
#
# ob1 = SampleClass(0)
# ob2 = SampleClass(2)
# ob3 = ob1
# ob3.val += 1
# print(ob1 is ob2)
# print(ob2 is ob3)
# print(ob3 is ob1)
# print(ob1.val, ob2.val, ob3.val)
# str1 = "Mary had a little "
# str2 = "Mary had a little lamb"
# str1 += "lamb"
# print(str1 == str2, str1 is str2)


# # 19 и 20 стр 10 урок напутан код и описанеие --------------------------------------------
# class SuperA:
#     varA = 10
#
#     def funA(self):
#         return 11
#
#
# class SuperB:
#     varB = 20
#
#     def funB(self):
#         return 21
#
#
# class Sub(SuperA, SuperB):
#     pass
#
# obj = Sub()
# print(obj.varA, obj.funA())
# print(obj.varB, obj.funB())

# class Left:
#     var = "L"
#     varLeft = "LL"
#
#     def fun(self):
#         return "Left"
#
#
# class Right:
#     var = "R"
#     varRight = "RR"
#
#     def fun(self):
#         return "Right"
#
#
# class Sub(Left, Right):
#     pass
#
#
# obj = Sub()
# print(obj.var, obj.varLeft, obj.varRight, obj.fun())


def printExcTree(thisclass, nest = 0):
    if nest > 1:
        print(" |" * (nest - 1), end="")
    if nest > 0:
        print(" +---", end="")
        print(thisclass.__name__)
    for subclass in thisclass.__subclasses__():
        printExcTree(subclass, nest + 1)


printExcTree(BaseException)
