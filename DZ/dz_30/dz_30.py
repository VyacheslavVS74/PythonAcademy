class Account:
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_eur = 'EUR'
    rate_usd = 0.013
    rate_eur = 0.011

    def __init__(self, num, surname, percent, value=0):
        self.__num = num
        self.__surname = surname
        self.__percent = percent
        self.__value = value
        print(f'Счет #{self.__num} принадлежащий {self.__surname} был открыт.')
        print('*' * 50)

    def print_info(self):
        print('Информация о счете:')
        print('-' * 20)
        print(f'#{self.__num}')
        print(f'Владелец: {self.__surname}')
        self.print_balance()
        print(f'Проценты: {self.__percent:.0%}')
        print('-' * 20)

    def print_balance(self):
        print(f'Текущий баланс {self.__value} {Account.suffix}')

    def set_num(self, num):
        self.__num = num

    def set_surname(self, surname):
        self.__surname = surname

    def set_percent(self, percent):
        self.__percent = percent

    def set_value(self, value):
        self.__value = value

    def get_num(self):
        return self.__num

    def get_surname(self):
        return self.__surname

    def get_percent(self):
        return self.__percent

    def get_value(self):
        return self.__value

    def convert_to_usd(self):
        usd_val = self.__value * Account.rate_usd
        print(f'Состояние счета: {usd_val} {Account.suffix_usd}')

    def convert_to_eur(self):
        eur_val = self.__value * Account.rate_eur
        print(f'Состояние счёта: {eur_val} {Account.suffix_eur}')

    # @classmethod
    # def set_usd_rate(cls, rate):
    #     cls.rate_usd = rate

    # @staticmethod
    # def convert(value, rate):
    #     return value * rate
    #
    # def convert_to_usd(self):
    #     usd_val = Account.convert(self.value, Account.rate_usd)
    #     print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
    #
    # def convert_to_eur(self):
    #     eur_val = Account.convert(self.value, Account.rate_eur)
    #     print(f'Состояние счёта: {eur_val} {Account.suffix_eur}')

    # без слов ----------------------------------------------------------------
    def set_usd(self, rate):
        self.rate_usd = rate * self.__value
        print(f'Состояние счёта: {self.rate_usd} {Account.suffix_usd}')

    def set_get(self, rate):
        self.rate_usd = rate * self.__value
        print(f'Состояние счёта: {self.rate_usd} {Account.suffix_eur}')

    # -------------------------------------------------------------------------

    def add_percents(self):
        self.__value += self.__value * self.__percent
        print('Проценты были успешно начислены!')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f'К сожалению у вас нет {val} {Account.suffix}')
        else:
            self.__value -= val
            print(f'{val} {Account.suffix} было успешно снято!')
        self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f'{val} {Account.suffix} было успешно добавлено!')
        self.print_balance()

    def __del__(self):
        print('*' * 50)
        print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт.')


Acc = Account('12345', 'Долгих', 0.03, 1000)
Acc.print_info()

Acc.convert_to_usd()
Acc.convert_to_eur()
print()
Acc.set_usd(2)
Acc.set_get(3)
# Acc.set_get(10)

print()
Acc.set_surname('Дюма')
Acc.print_info()

print()
Acc.add_percents()

print()
Acc.withdraw_money(3000)
print()
Acc.withdraw_money(100)
print()
Acc.add_money(5000)
print()
Acc.withdraw_money(3000)

# Acc.set_percent(2)
# Acc.convert_to_usd()
# Acc.convert_to_eur()


# class Account:
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#     rate_usd = 0.013
#     rate_eur = 0.011
#
#     def __init__(self, num, surname, percent, value=0):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был открыт.')
#         print('*' * 50)
#
#     def print_info(self):
#         print('Информация о счете:')
#         print('-' * 20)
#         print(f'#{self.__num}')
#         print(f'Владелец: {self.__surname}')
#         self.print_balance()
#         print(f'Проценты: {self.__percent:.0%}')
#         print('-' * 20)
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.__value} {Account.suffix}')
#
#     @property
#     def get_num(self):
#         return self.__num
#
#     @set_num.setter
#     def set_num(self, num):
#         self.__num = num
#
#     def set_surname(self, surname):
#         self.__surname = surname
#
#     def set_percent(self, percent):
#         self.__percent = percent
#
#     def set_value(self, value):
#         self.__value = value
#
#
#
#     def get_surname(self):
#         return self.__surname
#
#     def get_percent(self):
#         return self.__percent
#
#     def get_value(self):
#         return self.__value
#
#     def convert_to_usd(self):
#         usd_val = self.__value * Account.rate_usd
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = self.__value * Account.rate_eur
#         print(f'Состояние счёта: {eur_val} {Account.suffix_eur}')
#
#     # без слов ----------------------------------------------------------------
#     def set_usd(self, rate):
#         self.rate_usd = rate * self.__value
#         print(f'Состояние счёта: {self.rate_usd} {Account.suffix_usd}')
#
#     def set_get(self, rate):
#         self.rate_usd = rate * self.__value
#         print(f'Состояние счёта: {self.rate_usd} {Account.suffix_eur}')
#
#     # -------------------------------------------------------------------------
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.__value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт.')
#
#
# Acc = Account('12345', 'Долгих', 0.03, 1000)
# Acc.print_info()
#
# Acc.convert_to_usd()
# Acc.convert_to_eur()
# print()
# Acc.set_usd(2)
# Acc.set_get(3)
# # Acc.set_get(10)
#
# print()
# Acc.set_surname('Дюма')
# Acc.print_info()
#
# print()
# Acc.add_percents()
#
# print()
# Acc.withdraw_money(3000)
# print()
# Acc.withdraw_money(100)
# print()
# Acc.add_money(5000)
# print()
# Acc.withdraw_money(3000)


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, num, surname, percent, value=0):
#         self.num = num
#         self.surname = surname
#         self.percent = percent
#         self.value = value
#         print(f'Счет #{self.num} принадлежащий {self.surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f'К сожалению у вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счёта: {eur_val} {Account.suffix_eur}')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.value} {Account.suffix}')
#
#     def print_info(self):
#         print('Информация о счете')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#
# acc = Account('12345', 'Долгих', 0.03, 1000)
# acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
#
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
#
# print()
# acc.edit_owner('Дюма')
# acc.print_info()
#
# print()
# acc.add_percents()
# print()
# acc.withdraw_money(3000)
# print()
# acc.withdraw_money(100)
#
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
