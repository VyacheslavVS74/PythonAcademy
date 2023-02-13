
def add_title(args1):
    def args_dec(fn):
        def wrap(*args, **kwargs):
            print(args1.center(50, "="))
            a = fn(*args, **kwargs)
            print("=" * 50)
            return a
        return wrap
    return args_dec


class UserInterface:

    @add_title("Ввод пользовательских данных")
    def wait_user_answer(self):
        print("Действие со статьями:")
        print("1 - Создание статьи"
              "\n2 - Просмотр статей"
              "\n3 - Просмотр определенной статьи"
              "\n4 - удаление статьи"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        return user_answer

    @add_title("Создание статьи:")
    def add_user_article(self):
        dict_article = {
            "название статьи": None,
            "автор": None,
            "количество страниц": None,
            "описание": None
        }
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} статьи: ")

        return dict_article

    @add_title("Список статей:")
    def show_all_article(self, articles):
        for ind, article in enumerate(articles, start=1):
            print(f"{ind}. {article}")
