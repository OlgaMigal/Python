# Реализуйте алгоритм перемешивания элементов списка.
# Без функции shuffle из модуля random, другие методы использовать можно.

from random import sample

def task010():
    my_list = [4, 5, 6, 7, 8, 9, 10, 11]
    length = len(my_list)
    index_list = create_index_list(length)
    print(index_list)
    new_original_list = original_list(index_list, my_list)
    print(new_original_list)

def create_index_list(long):
    list_2 = []
    for el in range(long):
        list_2.append(el)
    return sample(list_2, long)

def original_list(new_idx_list, one_list):
    answer_list = []
    for el in new_idx_list:
        answer_list.append(one_list[el])
    return answer_list

task010()