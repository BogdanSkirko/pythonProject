# # написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
# # - первый записывает в эту переменную запись
# # - второй возвращает все записи
# #
# # запишите 5 тудушек
# # и выведете все
# # 2) протипизировать первое задание
from typing import Callable, List


def notebook() -> Callable:
    todo_list: List = []

    def inner(todo: str) -> list:
        todo_list.append(todo)
        return todo_list

    return inner
    # второй
    # возвращает
    # все
    # записи

    # def get_all():


todos = notebook()
print(todos('wake up'))
print(todos('brush your teeth'))
print(todos('go breakfast'))
print(todos('type text'))
print(todos('do homework'))
#
# # 3) С помощью lambda функции извлеките из списка числа, делимые на 15 без остатка.
#
#
list_numbers: List = [1, 352, 52, 65, 546, 7546, 15, 34, 30, 40, 45]
print(list(filter(lambda x: x % 15 != 0, list_numbers)))


#
#
# # 4) написать функцию которая будет принимать целое число n и посчитайте n + nn + nnn.
# # Пример:
# # summ(7) -> 7+77+777=861
def fun(n: int) -> int:
    sum = n + n * 11 + n * 111
    return sum


print(fun(3))
