# сделать функцию которая будет принимать число  и будет считать количество уножений цифр этого числа,
# если в результате умножения получилась больше чем одна цифра условие повторяется а счетчик увеличивается на 1
#
# Пример:
#
# persistence(39)  # вернется 3, потому что было три действия 3*9=27, 2*7=14, 1*4=4
# # а 4 это одна цифра
#
# persistence(999)  # вернется 4, потому что было четыре действия 9*9*9=729, 7*2*9=126,
# # 1*2*6=12, и в конце 1*2=2
#
# persistence(4)  # вернется 0, потому что и так одна цифра
# def persistance(num):
#     stop = 9
#     multi = 1
#     counter = 1
#     str_new = str(num)
#     for i in str_new:
#         multi = multi * int(i)
#         counter += 1
#     if multi <= stop:
#         counter -= 2
#     print(counter)
#
#
# persistance(999)
# сделать функцию которая будет возвращать сумму разрядов числа в виде строки
#
# Пример:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'
def expanded_form(num):
    new_list = str(num)

    for i in new_list:
        print(i)


expanded_form(312)
