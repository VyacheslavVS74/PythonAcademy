import sqlite3
import math


class FdataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения")
        return []

    def add_price(self, title, price, text):
        try:
            self.__cur.execute("INSERT INTO posts VALUES(NULL, ?, ?, ?)", (title, price, text))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления курса в БД" + str(e))
            return False
        return True

    def get_well(self, well_id):
        try:
            self.__cur.execute(f"SELECT title, price, text FROM posts WHERE id = {well_id} LIMIT 1")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса из БД" + str(e))
        return False, False, False

    def get_well_announce(self):
        try:
            self.__cur.execute(f"SELECT id, title, price, text FROM posts ORDER BY id DESC")
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса из БД" + str(e))

        return []

