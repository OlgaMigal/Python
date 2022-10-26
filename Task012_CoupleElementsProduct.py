# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний, и т.д:
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

def task012():
    start_list = [2, 3, 4, 5, 6]
    length = len(start_list)
    new_list = couple_elements_product(start_list, length)
    print(f'{start_list} => {new_list}')

def couple_elements_product(my_list, my_length):
    new_my_list = []
    for i in range(int(my_length/2)):
        new_my_list.append(my_list[i]*my_list[my_length-1-i])
    if my_length%2==1:
        new_my_list.append(my_list[int(my_length/2)]**2)
    return new_my_list


task012()
