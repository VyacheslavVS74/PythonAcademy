
class Power:
    def __init__(self, degree):
        self.degree = degree

    def __call__(self, fn):
        def wrap(a, b):
            print('Результат: ', fn(a, b) ** self.degree)

        return wrap


@Power(3)
def func(a, b):
    return a * b


func(2, 2)

