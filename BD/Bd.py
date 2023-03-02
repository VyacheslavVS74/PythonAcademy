# 14.02.2023 ====================================================================================

# Базы данных ----------------------

# SQL - язык структурированных запросов

# Реляционная база данных состоит из:
# Столбцы (поля, атрибуты)
# Строки (записи, кортежи)

# SQLite
# *.bd, *.db3, *.sqlite, *.sqlite3

# import sqlite3 as sq
#
# # con = sq.connect("profile.db")
# # cur = con.cursor()
# #
# # cur.execute("""
# # """)
# #
# # con.close()
#
# with sq.connect("profile.db") as con:
#     cur = con.cursor()
#     # cur.execute("""CREATE TABLE IF NOT EXISTS users(
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,
#     # name TEXT NOT NULL,
#     # summa REAL,
#     # data BLOB
#     # )""")
#
#     cur.execute("DROP TABLE users")
#
# # SELECT [ALL|DISTINCT] {*| столбец1[,cстолбец2] }
# # FROM таблица [, таблица2]


# 16.02.2023 =====================================================================

# WHERE условие
#       =, ==, <>, !=, >, >=, <, <=
#       выражение [NOT] BETWEEN начальное значение AND конечное значение
#       выражение [NOT] LIKE шаблон строки
#           % - любое количество символов
#           _ - один символ
#       выражение [NOT] GlOB регулярное выражение
#           * - любое количество символов
#           ? - один символ
#           . - любой одиночный символ
#           [abc] - один из заданных символов
#           [a-z0-9] - диапозон заданнных символов
#           ^ - [^abc] - все кроме заданных симмволов
#       выражение IS [NOT] NULL
#       выражение [NOT] IN (набор значений)
# GROUP BY (группировать по)
# HAVING (условие)
# ORDER BY имя поля [ASC|DESC] - сортировка

# import sqlite3 as sq
#
# with sq.connect("users.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS person(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone BLOB NOT NULL DEFAULT "+79090000000",
#     age INTEGER NOT NULL CHECK(age>15 AND age<70),
#     email TEXT UNIQUE
#     )""")

# переименование таблицы ниже
#     cur.execute("""
#     ALTER TABLE person
#     RENAME TO person_table
#     """)

# добавление столбца ниже
#     cur.execute("""
#     ALTER TABLE person_table
#     ADD COLUMN address TEXT NOT NULL DEFAULT "street"
#     """)

# переименование столбца ниже
#     cur.execute("""
#     ALTER TABLE person_table
#     RENAME COLUMN address TO home_address
#     """)

# удаление столбца ниже
#     cur.execute("""
#     ALTER TABLE person_table
#     DROP COLUMN home_address
#     """)

# удаление самой таблицы ниже
#     cur.execute("""
#     DROP TABLE person_table
#     """)

# Добавление новой строки ----------------
# INSERT INTO имя_таблицы [(столбец1[, столбец_n])]
# VALUES (значение_1[, значение_n])

# 21.02.2023 ======================================================================

# Перенос строки из одной таблицы в другую
# INSERT INTO T1(ID, Fname, Doljnost, Orab, ZP)
# SELECT ID, Fname, D, Orabot, Zp
# From T2
# WHERE ID LIKE 19

# UPDATE имя_таблицы
# SET столбец1=выражэение1, столбец2=выражение2 -- SET установить
# [WHERE условие]

# удаление определенных данных
# DELETE FROM имя_таблицы
# WHERE условие

# очистить записи из таблицы
# DELETE FROM T2;

# LIMIT колличество_строк OFFSET смещение
# limit [смещение,] количество_строк
# SELECT *
# FROM T1
# ORDER BY Fname
# LIMIT 10, 5
# /*LIMIT 5 OFFSET 2*/
# 5 записей со сдвигом на 2 от начала


# import sqlite3 as sq
#
# with sq.connect("db_3.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     SELECT *
#     FROM T1
#     ORDER BY Fname
#     LIMIT 2, 5
#     """)
#
#     # res = cur.fetchone()
#     res2 = cur.fetchmany(3)
#     res1 = cur.fetchall()
#     # print(res)
#     print(res2)
#     print(res1)
#
#     # res = cur.fetchall()
#     # print(res)
#
#     # for res in cur:
#     #     print(res)

# разработчики логической базы данных
# разработчики физической базы данных

# 28.02.2023 ===========================================================================

# Функции агрегирования -----------------

# SUM (только с числами) сумма столбца
# AVG (только с числами) среднее арифметическое столбца
# COUNT (числа и строки) подсчет строк заполненных
# MIN (числа и строки)
# MAX (числа и строки)

# SELECT COUNT(Client) AS [Количество клиентов]
# SELECT COUNT(Client) AS 'Количество клиентов'
# SELECT COUNT(Client) AS Количество
# SELECT COUNT(Client) Количество


# import sqlite3 as sq
#
# cars = [
#     ("BMW", 54000),
#     ("Chevrolet", 56000),
#     ("Daewoo", 38000),
#     ("Citroen", 21000),
#     ("Honda", 33000)
# ]
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)

    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {"Price": 0})
    # cur.execute("UPDATE cars SET price = 0 WHERE model LIKE 'B%'")  # второй вариант

    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

    # cur.execute("INSERT INTO cars VALUES(1, 'Renault', 20000)")
    # cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
    # cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
    # cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
    # cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")

# con.commit()
# con.close()


# import sqlite3 as sq
#
# con = None
# try:
#     con = sq.connect("cars.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#
#     INSERT INTO cars VALUES(NULL, 'Renault', 20000);
#     UPDATE cars2 SET price = price + 100;
#     """)
#     con .commit()
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print(f"Ошибка выполнения запроса {e}")
# finally:
#     if con:
#         con.close()

# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)
#
#     cur.execute("SELECT model, price FROM cars")
#
#     # rows = cur.fetchall()
#     # rows = cur.fetchone()
#     # rows = cur.fetchmany(5)
#     # print(rows)
#     # for res in cur:
#     #     print(res)
#
#     for res in cur:
#         print(res["model"], res["price"])


# import sqlite3 as sq
#
#
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         user_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         ava BLOB
#     );
#     """)
#     img = read_ava(1)
#     if img:
#         binary = sq.Binary(img)
#         cur.execute("INSERT INTO users VALUES (?, ?)", (1, binary))

# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#
#     # with open("sql_dump.sql", "w") as f:
#     #     for sql in con.iterdump():
#     #         f.write(sql)
#
#     with open("sql_dump.sql", "r") as f:
#         sql = f.read()
#         cur.executescript(sql)
