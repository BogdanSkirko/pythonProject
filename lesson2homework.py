# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

st = 'as 23 fdfdg544'
new = []
for i in st:
    if i.isdigit():
        new.append(i)
print(new)

# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
sti = 'as 23 fdfdg544 34'
# # # #   23, 544, 34              #вивело в консолі
new_st = ''
for i in sti:
    if i.isdigit():
        new_st += i
    else:
        new_st += ' '
new_st = ', '.join(new_st.split())
print(new_st)
# #################################################################################
#
# list comprehension
#
# 1)есть строка:
# # записать каждый символ в лист поменяв его на верхний регистр
# # пример:
# # ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'
new_list = [i.upper() for i in greeting if i.lower()]
print(new_list)

# 2) с диапазона от 0-50 записать в лист только не парные числа, при этом возвести их в квадрат
# пример:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]


list_range = [i ** 2 for i in range(50) if i % 2 != 0]
print(list_range)


# function
#
# - створити функцію яка виводить ліст
def get_list(list):
    print(list)


get_list([])


# - створити функцію яка приймає три числа та виводить та повертає найменьше.

def minimum(a, b, c):
    return (min(a, b, c))


print(minimum(1, 3, 654))


# - створити функцію яка приймає три числа та виводить та повертає найбільше.
def maximum(a, b, c):
    return (max(a, b, c))


print(maximum(1, 3, 654))


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше
def any(*args):
    print(max(*args))
    return (min(*args))


any(1, 4, 5, 6, 2, 5, 254)


# - створити функцію яка виводить ліст
def free_list(list):
    print(list)


free_list([])


# - створити функцію яка повертає найбільше число з ліста
def max_num(list):
    print(max(list))


max_num([1, 3, 4, 5, 6, 44444])


# - створити функцію яка повертає найменьше число з ліста
def min_num(list):
    print(min(list))


min_num([1, -122, 3, 4, 5, 6, 44444])


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def list_num(lists):
    suma = []
    for i in lists:
        suma.append(i)
    print(sum(suma))


list_num([1, 3, 4, 5, 6, 33333])


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
def list_avg(lists):
    avg_list = 0
    for i in lists:
        avg_list = (avg_list + i) / len(lists)
    print(avg_list)
    return avg_list


list_avg([10, 10, 10, 10, 10, 1000, 31231])


# decorators
# - є функція:
#  написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення




def decor(a):
    change = a().replace('_', ' ')
    return change

@decor
def pr():
    return 'Hello_boss_!!!'


print(pr)