import json

data = {}


class Country:
    """Хранение, добавление, удаление, поиск, редактирование и просмотр данных стран и столиц.
    Storing, adding, deleting, searching, editing and viewing country and capital data."""
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        data[self.country] = self.capital

    @staticmethod
    def add_data(reg):
        """Добавление данных"""
        global data
        try:
            data = json.load(open("country.json"))
        except FileNotFoundError:
            data = {}
        if reg.country in data:
            print("Указанная страна уже есть в базе данных.")
        else:
            data[reg.country] = reg.capital
        with open("country.json", "w") as f:
            json.dump(data, f)

    @staticmethod
    def load_to_file():
        """Просмотр данных"""
        try:
            with open("country.json", "r") as f:
                print(json.load(f))
        except FileNotFoundError:
            print("Данных нет.")

    @staticmethod
    def delete_data(key):
        """Удаление данных"""
        global data
        with open("country.json", "r") as f:
            data = json.load(f)
            if key in data:
                del data[key]
            else:
                print("Таких данных не существует!")

        with open("country.json", "w") as f:
            json.dump(data, f)

    @staticmethod
    def search_data(key):
        """Поиск данных"""
        global data
        with open("country.json", "r") as f:
            data = json.load(f)
            if key in data:
                print(f"Страна: {key}, Столица: {data[key]}")
            else:
                print("Таких данных не существует!")

    @staticmethod
    def editor_data(key, meaning):
        """Удаление данных"""
        global data
        with open("country.json", "r") as f:
            data = json.load(f)
            if key in data:
                data[key] = meaning
            else:
                print("Таких данных не существует!")

        with open("country.json", "w") as f:
            json.dump(data, f)


while True:
    print(f"{'*' * 30}\nВыбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n4 - "
          f"редактирование данных\n5 - просмотр данных\n6 - завершение работы")
    action = int(input("Ввод: "))
    if action == 1:
        region = input("Введите название страны (с заглавной буквы): ")
        city = input("Введите название столицы страны (с заглавной буквы): ")
        c1 = Country(region, city)
        Country.add_data(c1)
    if action == 2:
        region = input("Введите название страны (с заглавной буквы): ")
        Country.delete_data(region)
    if action == 3:
        region = input("Введите название страны (с заглавной буквы): ")
        Country.search_data(region)
    if action == 4:
        region = input("Введите название страны (с заглавной буквы): ")
        city = input("Введите название столицы страны (с заглавной буквы): ")
        Country.editor_data(region, city)
    if action == 5:
        Country.load_to_file()
    if action == 6:
        print("Bye!")
        break
    if 0 > action > 6:
        print("Не верный выбор действия!!!")
