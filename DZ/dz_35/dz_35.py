from random import *


# class Cat:
#     def __init__(self, sex, name='No name', age=0):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     # def __add__(self, other):
#     #     a = ''
#     #     s = ['M', 'F']
#     #     for i in range(3):
#     #         a += f"Cat(name='No name', age=0, sex='{choice(s)}')"
#     #     return a
#
#     def __add__(self, other):
#         a = []
#         s = ['M', 'F']
#         for i in range(randint(1, 3)):
#             a.append(f"Cat(name='No name', age=0, sex='{choice(s)}')")
#         return a
#
#
# c1 = Cat('Tom is good boy!!!')
# c2 = Cat('Elsa is good girl!!!')
# c3 = c1 + c2
# print(c3)

# -----------------------------------------------------------------------
class Cat:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        print(self.name, 'is good', self.sex)

    def __add__(self, other):
        a = []
        s = ['M', 'F']
        if self.sex != other.sex:
            for i in range(randint(1, 4)):
                a.append(f"Cat(name='No name', age=0, sex='{choice(s)}')")
            return a
        else:
            return 'Пол животных должен отличаться'


c1 = Cat('Tom', 'boy')
c2 = Cat('Elsa', 'girl')  # girl

c3 = c1 + c2
print(c3)
# -----------------------------------------------------------------------
