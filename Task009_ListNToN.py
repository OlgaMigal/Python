# Задайте список из элементов, заполненных числами из промежутка [-N, N].
# Задайте два числа - позиции(индексы) в исходном списке это границы диапазона.
# Найдите произведение элементов списка в указанном диапазоне индексов
# Пример:
# N = 6
# Пример списка чисел: [-2, -5, 4, 1, 4, 1, 2, -5, -3, 0, -6, -6, 5]
# границы диапазона: 2, 5
# Произведение для [4, 1, 4, 1] равно 16
# Примечание: Границы диапазона вводятся пользователем, надо корректно учесть,
# что они могут быть некорректными: больше длины списка, меньше нуля, первый больше второго и т.п.

# 1. Задать N, заполнить список элементами в диапазоне [-N, N]

from random import randint

def task009():
    number = int(input('Введите N: '))
    diapasone = fill_list(number)
    print(diapasone)
    diap_sum(number, diapasone)


def fill_list(num):
    list_diapasone = []

    for i in range(abs(num)*2+1):
        list_diapasone.append(randint(-num, num))

    return list_diapasone


def diap_sum(num, diap):
    start = int(input(f'Введите 2 индекса диапазона в границах от 0 до {num*2}: \n'))
    end = int(input())
    if start>num*2 or start<0 or end>num*2 or end<0:
        print('Число не удовлетворяет условиям, перезапустите')
    else:
        sum = 0
        if start<end:
            i = start
            while i<=end:
                sum+=diap[i]
                i+=1
            print(f'Произведение для {diap[start:end+1]} равно {sum}')
        elif start>end:
            i = end
            while i<= start:
                sum += diap[i]
                i += 1
            print(f'Произведение для {diap[end:start+1]} равно {sum}')
        else:
            print(f'Произведение для {diap[start:end]} равно {start}')


task009()