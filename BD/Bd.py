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


import sqlite3 as sq

with sq.connect("db_3.db") as con:
    cur = con.cursor()
    cur.execute("""
    SELECT *
    FROM T1
    ORDER BY Fname
    LIMIT 2, 5
    """)

    # res = cur.fetchone()
    res2 = cur.fetchmany(3)
    res1 = cur.fetchall()
    # print(res)
    print(res2)
    print(res1)

    # res = cur.fetchall()
    # print(res)

    # for res in cur:
    #     print(res)

# разработчики логической базы данных
# разработчики физической базы данных
