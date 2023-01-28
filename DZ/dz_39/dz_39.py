import json

# 1 вариант --------------------------------------


# class File:
#     def __init__(self):
#         self.a = 35
#         self.b = "test"
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"
#
#
# item1 = File()
# item2 = json.dumps(item1.__str__())
# item3 = json.loads(item2)
# print(item1)

# 2 вариант -----------------------------------------


# class File:
#     def __init__(self, a, b, d):
#         self.a = a
#         self.b = b
#         self.d = d
#         # self.c = lambda x: x * x
#
#     def json_info(self):
#         obj_json = {
#             "a": self.a,
#             "b": self.b,
#             "d": self.d
#         }
#         return obj_json
#
#
# data = File(35, "test", 100)
# data1 = data.json_info()
# with open("file_obj.json", "w") as fw:
#     json.dump(data1, fw, indent=4)
#
# with open("file_obj.json", "r") as fw:
#     data1 = json.load(fw)
#     print(data1)

# 3 вариант ------------------------------------------------------


class File:
    def __init__(self):
        self.a = 35
        self.b = "test"
        self.d = 100
        # self.c = lambda x: x * x

    def __str__(self):
        return f"{self.a}, {self.b}, {self.d}"  # {self.c(2)}


data = File()

with open("file.json", "w") as fw:
    json.dump(data.__dict__, fw, indent=4)  # data.__str__()

with open("file.json", "r") as fw:
    data = json.load(fw)
    print(data)