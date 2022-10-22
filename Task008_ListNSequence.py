# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n=4 [2, 2.25, 2.37, 2.44]
# Сумма 9.06

number = int(input(f'Введите число: '))
def task008():
    summa_list = list_n_sequence(number)
    print(f'Для n = {number}   {summa_list}')
    sum(summa_list)

def list_n_sequence(num):
    list_n = []
    for i in range(1, num+1):
        round_num = round((1+1/i)**i, 2)
        list_n.append(round_num)
    return(list_n)

def sum(list_num):
    sum = 0
    for el in list_num:
        sum+=el
    print(f'Сумма {sum}')

task008()