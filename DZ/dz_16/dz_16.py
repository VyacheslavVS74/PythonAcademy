def args_dec(fn):
    def wrap(*args):
        print('Сумма чисел', *args, '=', fn(*args))
        a = ''
        for i in args:
            a += str(i) + ', '
        print('Среднее арифметическое чисел ', a[:-2], '=', fn(*args) / len(args))
    return wrap


@args_dec
def sun_nums(*args):
    s = 0
    for i in args:
        s += i
    return s


sun_nums(2, 3, 3, 4)
