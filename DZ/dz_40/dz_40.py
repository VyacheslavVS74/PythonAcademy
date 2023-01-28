import json
from random import choice


def get_person():
    name = ""
    tel = ""
    id_persons = ""

    letter = ["a", "b", "c", "d", "e", "f", "g", "h"]
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    while len(name) != 7:
        name += choice(letter)
    # print(name)

    while len(tel) != 10:
        tel += choice(nums)
    # print(tel)
    while len(id_persons) != 5:
        id_persons += choice(nums)

    person = {
        id_persons: {
            "name": name,
            "tel": tel
        }
    }

    return person


def write_json(person_dict):

    try:
        data = json.load(open("persons.json"))  # [{}]
    except FileNotFoundError:
        data = {}

    data.update(person_dict)
    # data.append(person_dict)  # [{}, {}]
    with open("persons.json", "w") as f:
        json.dump(data, f, indent=2)  # [{}, {}]


for i in range(5):
    write_json(get_person())


# n = ''
#     n1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
#     while len(n) != 10:
#         n += choice(n1)
#     choice(n):

# data1 = {
#     '123': person_dict
# }
# data |= data1
#
# data1 = {
#     '123': person_dict
# }
# data.update(data1)
