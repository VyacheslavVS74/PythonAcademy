
def decor_title(title):
    """Декорирующая функция класса FilmView"""
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(title.center(50, "="))
            fn = func(*args, **kwargs)
            print("=" * 50)
            return fn
        return wrap
    return wrapper


class FilmView:

    @decor_title(" Редактирование данных каталога фильмов ")
    def wait_user_answer(self):
        print("Действия с фильмами:")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия => ")
        return user_answer

    @decor_title(" Добавление фильма в каталог ")
    def add_user_film(self):
        dict_film = {
            "название": None,
            "жанр": None,
            "режиссер": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }
        for key in dict_film:
            dict_film[key] = input(f"{key} фильма => ")
        return dict_film

    @decor_title(" Список фильмов ")
    def show_all_films(self, films):
        for index, film in enumerate(films, start=1):
            print(f"{index}. {film}")

    @decor_title(" Ввод названия фильма ")
    def get_user_film(self):
        user_film = input("Введите название фильма => ")
        return user_film

    @decor_title(" Просмотр статьи ")
    def show_film(self, film):
        for key in film:
            print(f"{key} фильма - {film[key]}.")

    @decor_title(" Сообщение об ошибке ")
    def show_title_error(self, user_title):
        print(f"Фильм с названием {user_title} не существует!")

    @decor_title(" Удаление фильма ")
    def remove_single_film(self, film):
        print(f"Фильм {film} был удален.")

    @decor_title(" Сообщение об ошибке ")
    def show_answer_error(self, answer):
        print(f"Варианта {answer} не существует!")
