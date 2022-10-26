# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# DONE Создай список из случайных чисел и оттренируй форму for el in range(1, len(my_list), 2). И декомпозируй.

from random import randint

def Task011():
    step = 2
    shuffle_list = list_creation()
    odd_list = odd_index_list(shuffle_list, step)
    odd_sum = odd_index_sum(odd_list)
    print(f'{shuffle_list} -> нечётные {odd_list}, ответ: {odd_sum}')


def list_creation():
    length = int(input('Введите длину списка: '))
    my_list = []
    for _ in range(length):
        my_list.append(randint(1, 9))
    return my_list


def odd_index_list(my_list, one_step):
    new_list = []
    for i in range (1, len(my_list), one_step):
        new_list.append(my_list[i])
    return new_list


def odd_index_sum(new_odd_list):
    sum = 0
    for el in new_odd_list:
        sum += el
    return sum


Task011()