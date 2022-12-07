class Book:
    name = 'название книги'
    age = 'год выпуска'
    publisher = 'издатель'
    genre = 'жанр'
    author = 'автор'
    price = 'цена'

    def print_info(self):
        print(f' Книга: {self.name} '.center(40, '*'))
        print(f'Год выпуска: {self.age}\nИздатель: {self.publisher}\nЖанр: {self.genre}\nАвтор: {self.author}\n'
              f'Цена: {self.price}')
        print('*' * 40)

    def input_info(self, name, age, publisher, genre, author, price):
        self.name = name
        self.age = age
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_name(self, name):
        if isinstance(name, str):
            self.name = name

    def set_age(self, age):
        if isinstance(age, int):
            self.age = age

    def set_publisher(self, publisher):
        if isinstance(publisher, str):
            self.publisher = publisher

    def set_genre(self, genre):
        if isinstance(genre, str):
            self.genre = genre

    def set_author(self, author):
        if isinstance(author, str):
            self.author = author

    def set_price(self, price):
        if isinstance(price, float) or isinstance(price, int):
            self.price = price

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author

    def get_price(self):
        return self.price


h1 = Book()
h1.print_info()
h1.input_info('Приключения Тома Сойера', '1876', 'Альфа-книга', 'Приключения', 'Марк Твен', '446')
h1.print_info()

# h1.set_price(150)  # цена ввод данных
# h1.print_info()

print(h1.get_author())
