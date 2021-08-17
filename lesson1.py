# 1)Дан лист:
#  - найти min число в листе
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]

# list.sort()
# print(list[0])


#  - удалить все дубликаты в листе

# print(set(list))


#  - заменить каждое четвертое значение на "Х"
# for i in range(len(list)):
#     if list[i] % 4 == 0:
#         list[i] = 'x'
#
#
# print(list)
# 2)вывести на экран пустой квадрат из "*" сторона которого указана в переменой:

# width = 10
# height = 10
#
# print('*' * width)
# for i in range(height - 2):
#     print('*' + ' ' * (width-2) + '*')
# print('*' * height)


# 3) вывести табличку умножения с помощью цикла while
# table = 9
# # for i in range(1, table+1):
# #     print(*range(i,i*table+1 ,i),sep='\t')

# 4) переделать первое задание под меню с помощью цикла
while True:
    print('1) Знайти мін. число')
    print('2) удалить все дубликаты в листе')
    print('3) заменить каждое четвертое значение на "Х"')
    print('4) вывести элемент листа, значение которого ближе всего к среднему арифметическому всеx эл. этого листа')
    print('5) exit')
    choise = input('make your choise ')
    if choise == '1':
        print(list)
        list.sort()
        print(list[0])
        pass
    if choise == '2':
        for i in range(len(list)):
            if list[i] % 4 == 0:
                list[i] = 'x'
    if choise == '3':
        for i in range(len(list)):
            if list[i] % 4 == 0:
                list[i] = 'x'
                pass




# '''***  - вывести элемент листа, значение которого ближе всего к среднему арифметическому всех элементов этого же листа
# пример:
# [1, 2, 3, 4, 5, 6, 7, 8, 9] => 5
# [-1, -2, 3, 4, 555] => 4
# [5, 5, 5, 5] => 5
# [-10, 5, 5] => 5
