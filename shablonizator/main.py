# from jinja2 import Template

# Шаблонизатор (Jinja)
# pip install Jinja2

# {{ }} - выражение для вставки конструкции Python в шаблон

# name = "Игорь"
# age = 28

# per = {"name": "Игорь", "age": 28}

# tm = Template("Мне {{ a * 2 }}. Меня зовут {{ n.upper() }}. ")
# msg = tm.render(n=name, a=age)

# tm = Template("Мне {{ p.age }}. Меня зовут {{ p['name'].upper() }}. ")
# msg = tm.render(p=per)
# print(msg)


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#
# per = Person("Игорь", 26)
#
# tm = Template("Мне {{ p.get_age() }}. Меня зовут {{ p.get_name().upper() }}. ")
# msg = tm.render(p=per)
# print(msg)

# {% %} - спецификатор шаблона
# {# #} - блок комментариев
#       # ## - строковый комментарий
# {% for <выражение> %}
#   <тело цикла>
# {% endfor %}

# {% if <условие> %}
# {% elif <условие>%}
# {% else %}
# {% endif %}

# cities = [
#     {"id": 1, "city": "Москва"},
#     {"id": 2, "city": "Смоленск"},
#     {"id": 3, "city": "Минск"},
#     {"id": 4, "city": "Ярославль"},
#     {"id": 5, "city": "Уфа"},
# ]
#
# Link = """<select name="cities">
# {% for c in cities -%}
# {% if c.id > 3 -%}
#     <option value="{{ c['id'] }}">{{ c['city'] }}</option>
# {% elif c.city == 'Москва' %}
#     <option>{{ c['city'] }}</option>
# {% else -%}
#     {{ c['city'] }}
# {% endif -%}
# {% endfor -%}
# </select>
# """
#
# tm = Template(Link)
# msg = tm.render(cities=cities)
# print(msg)


# menu = [
#     {'id': 'index', 'title': 'Главная'},
#     {'id': 'news', 'title': 'Новости'},
#     {'id': 'about', 'title': 'О компании'},
#     {'id': 'shop', 'title': 'Магазин'},
#     {'id': 'contacts', 'title': 'Контакты'},
# ]
# link = """<ul>
# {%for i in menu -%}
# {%if i.title=='Главная'-%}
#     <li><a href="/{{i.id}}" class="active">{{i.title}}</a></li>
# {%else-%}
#     <li><a href="/{{i.id}}">{{i.title}}</a></li>
# {%endif-%}
# {%endfor-%}
# </ul>
# """
# tm = Template(link)
# msg = tm.render(menu=menu)
# print(msg)

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44300},
#     {'model': 'Wolksvagen', 'price': 21300}
# ]
#
# # tp1 = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"
# # tp1 = "Суммарная цена автомобилей {{ (cs | max(attribute='price')).model }}"
# # tp1 = "{{ cs | random }}"
# tp1 = "{{ cs | replace('model', 'brand') }}"
#
# # lst = [1, 2, 3, 4, 5, 6]
# # tp1 = "Суммарная цена автомобилей {{ cs | sum }}"  # msg = tm.render(cs=lst)
#
# tm = Template(tp1)
# msg = tm.render(cs=cars)
#
# print(msg)

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44300},
#     {'model': 'Wolksvagen', 'price': 21300}
# ]
# print(sum(map(lambda x: x['price'], cars)))

# Макроопределение (=функция) ------------------------------------------------

# html = """
# {% macro input(name, value='', type='text', size=20) -%}
#     <input type='{{ type }}' name='{{ name }}' value='{{ value }}' size='{{ size }}'>
# {% endmacro %}
#
# <p>{{ input('username', 'Ann') }}</p>
# <p>{{ input('email') }}</p>
# <p>{{ input('password', type='password') }}</p>
# """
# tm = Template(html)
# msg = tm.render()
# print(msg)


# html = """
# {% macro input(name, type='text', placeholder='') -%}
# <input type='{{ type }}' name='{{ name }}' placeholder='{{ placeholder }}'>
# {% endmacro %}
#
# <p>{{ input('firstname', placeholder="Имя") }}</p>
# <p>{{ input('lastname', placeholder="Фамилия") }}</p>
# <p>{{ input('address', placeholder="Адрес") }}</p>
# <p>{{ input('phone', type='tel', placeholder="Телефон") }}</p>
# <p>{{ input('email', type='email', placeholder="Почта") }}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
# print(msg)

# {% call[(параметры)] <вызов макроса> %}
# <вложенный шаблон>
# {% endcall %}

# persons = [{"name": "Алексей", "year": 18, "weight": 78.5},
#            {"name": "Никита", "year": 28, "weight": 82.3},
#            {"name": "Виталий", "year": 33, "weight": 94.0}
# ]
#
# html = '''
# {% macro list_users(list_of_users) %}
# <ul>
# {% for u in list_of_users -%}
#     <li>{{ u.name }} {{ caller(u) }}</li>
# {% endfor -%}
# </ul>
# {%- endmacro %}
#
# {% call(user) list_users(users) %}
#     <ul>
#         <li>{{ user.year }}</li>
#         <li>{{ user.weight }}</li>
#     </ul>
# {% endcall %}
# '''
#
# tm = Template(html)
# msg = tm.render(users=persons)
# print(msg)

from jinja2 import Environment, FileSystemLoader

persons = [{"name": "Алексей", "year": 18, "weight": 78.5},
           {"name": "Никита", "year": 28, "weight": 82.3},
           {"name": "Виталий", "year": 33, "weight": 94.0}
]

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(users=persons, title='About Jinja')

print(msg)

# {% include <путь> %}