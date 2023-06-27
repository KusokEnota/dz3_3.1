"""Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не
должно быть дубликатов."""


def double_list(array):
    res = set()
    for el in array:
        counter = array.count(el)
        if counter > 1:
            res.add(el)
    return list(res)


print(double_list([1, 2, 3, 1, 2, 4, 5, 5, 7, 4, 3]))
