# реализовать записную книжку покупок:
# - каждая запись должна содержать название покупки и ее цену
# -сделать менюшку для работы с записной книжкой:
#     '1) Создать запись'
#     '2) Список все записей'
#     '3) Общая сумма всех покупок'
#     '4) Самая дорогая покупка'
#     '5) Поиск по названию покупки'
#     '9) Выход'
# - можете придумать свои пункты

notebook = [
    {'name': 'egg', 'price': 3},
    {'name': 'meat', 'price': 100},
]

while True:
    print('1)Створити список')
    print('2)Список всіх записів')
    print('3)Загальна сума всіх покупок')
    print('4)Найдорожча покупка')
    print('4)Пошук по назві покупки')
    print('9)Вихід')

    choise = input(print('Зробіть свій вибір:'))
    if choise == '1':
        name = input('Введіть назву покупи : ')
        price = input('Введіть суму покупки : ')
        notebook.append({'name': name, 'price': price})
        pass
    if choise == '2':
        for i in notebook:
            print(i)
        pass
    if choise == '3':
        sum = 0
        for i in notebook:
            sum += i['price']

        print('Сума покупок : ', sum)
        pass
    if choise == '4':
        name = input('Введіть назву покупки - ')
        for i in notebook:
            if i['name'] == name:
                print(i)
                break