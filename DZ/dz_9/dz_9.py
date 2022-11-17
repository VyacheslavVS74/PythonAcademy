print(1, 2, 3)
print(1, 8, 3, 4, 8, 8, 9, 2)
print(1, 2, 8, 5, 1, 2, 9)
el = int(input("введите искомый элемент: "))


def slicer(tpl, elem):
    if elem in tpl:
        if tpl.count(elem) > 1:
            a = tpl.index(elem)
            b = tpl.index(elem, a + 1)
            return tpl[a:b + 1]
        else:
            return tpl[tpl.index(elem):]
    else:
        return ()


print(slicer((1, 2, 3), el))
print(slicer((1, 8, 3, 4, 8, 8, 9, 2), el))
print(slicer((1, 2, 8, 5, 1, 2, 9), el))
