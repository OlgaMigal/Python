# Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01, 12.00] => 0.19

from random import randint, uniform

def task013():
    my_list = [round(uniform(1, 20), 2) for i in range(randint(4, 8))]
    print(my_list)
    my_new_list = [round(i%1, 2) for i in my_list]
    answer_list = []
    for el in my_new_list:
        if el!=0: answer_list.append(el)
    print(answer_list)
    difference = round(max(answer_list)-min(answer_list), 2)
    print(f'\n{my_list}   =>   {difference}')

task013()