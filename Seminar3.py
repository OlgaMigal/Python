# # Задайте список из нескольких чисел. Напишите программу, которая
# # найдёт сумму элементов списка, стоящих на нечётной позиции.
# # Пример:
# # [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
#
# my_list = [5, 7, 2, 1, 35, 8, 40]
# answer_sum = 0
# i = 1
# for i in range(1, len(my_list), 2):
#     answer_sum+=my_list[i]
# print(answer_sum)
#
#
#
#
#
# my_list = [2, 3,  5, 6]
# n= len(my_list)
#
# if n % 2 == 1:
#     len_n = n // 2 + 1
# else:
#     len_n = n // 2
#
# new_list = []
# for i in range(len_n):
#     new_list.append(my_list[i] * my_list[-(i + 1)])
# print("Произведение пар чисел списка: ")
# print(new_list)
#
#
#
# numbers_list = [0.324, 0.2, 12.0, 3.54, 11, 7.96, 5, 4.943]
# fract_list = []
#
# for i in range(0, len(numbers_list)):
#     if numbers_list[i] - int(numbers_list[i]) > 0:
#         fract_list.append(numbers_list[i] - int(numbers_list[i]))
#
# print('Разница между максимальной дробной частью и минимальной, не равной нулю, будет:', max(fract_list) - min(fract_list))
#
#

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> '101101'
# 3 -> '11'
# 2 -> '10'
# Примечание: Результат вернуть в виде строки. Не использовать функции преобразования типов: bin

# 27. Задайте строку из набора чисел.
#
# Напишите программу, которая покажет большее и меньшее число.
#
# В качестве символа-разделителя используйте пробел.
#
# Пример: Строка " 12 34 78 9894 4373 123"
#
# Усложнение: создайте строку чисел через случайные числа. Подсказка: используйте метод строки
# join для создания строки.
#

# my_str = " 12  34  78  9894  4373  123"
# my_list = my_str.split()
# print(my_list)
#
# other_one = [int(i) for i in my_list]
# print(other_one)
#
# print(f"{min(other_one)} {max(other_one)}")




# my_list = [12, 34, 78, 9894, 4373, 1230]
# second = ""
# third = ""
# for i in range (len(my_list)):
#     second += str(my_list[i])+" "
# third+=(f"{min(my_list)} {max(my_list)}")
# print(my_list)
# print(second)
# print(third)






# 28. Найдите корни квадратного уравнения Ax² + Bx + C = 0
# Для обоих вариантов:
# - действительные корни
# - комплексные корни
# Примечание:
# - проверить нужное условие перед вычислением корней
# - найти нужные пакеты стандартной библиотеки и функции в них для вычисления кв. корня.

# from math import sqrt as sq1
# from cmath import sqrt as sq2
# n_a = 3
# n_b = 6
# n_c = 3
# D = n_b ** 2 - 4 * n_a * n_c
# if D > 0:
#     x1 = (-n_b + sq1(D)) / 2 * n_a
#     x2 = (-n_b - sq1(D)) / 2 * n_a
# elif D == 0:
#     x1 = -n_b / 2 * n_a
#     x2 = None
# else:
#     x1 = (-n_b + sq2(D)) / 2 * n_a
#     x2 = (-n_b - sq2(D)) / 2 * n_a
# print(x1, x2)
#
#
# # от Кирилла Пичугина
#
# from math import sqrt as sq
# from cmath import sqrt as csq
#
# a = 2
# b = 3
# c = -4
#
# dis = b**2 - 4 * a * c
# # Присваивание в лоб
# # if dis > 0:
# #     sqrt = sq
# # else:
# #     sqrt = csq
#
# # Тернарный оператор
# sqrt = sq if dis>0 else csq
# x1 = (-b + sqrt(dis))/(2*a)
# x2 = (-b - sqrt(dis))/(2*a)
# print(f"Корни уравнения: {x1:.2f} и {x2:.2f}")
#
#
# # 29. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.
#
# num_1 = int(input("Введите первое число: "))
# num_2 = int(input("Введите второе число: "))
#
# i = max(num_1, num_2)
#
# while ((i % num_1 != 0) or (i % num_2 != 0)):
#     i += 1
# print(i)
#
#
# # Добрый день. Если хочется послушать курс, то stepik, coursera и другие сайты обучения. Там можно найти бесплатный курс по основам языка.
# # Если речь про книги, то
# # Лутц М.  - Изучаем Python (5-е издание). А может уже и более позлние издания.
# # Доусон М. Программируем на Python. Какое издание не помню. Поищите самое свежее.
# # Литературы полно и на русском тоже. Скорее надо ориентироваться на стиль подачи автора. Насколько вам он близок.
#
# def read_data(filename: str) -> list:
#     with open(filename, "r", encoding = "utf-8") as data:
#         a = data.read().split()
#         a = list(map(int,a)) #  или  a = [int(elem) for elem in a]
#     return a
# a = read_data("file1.txt")
#
# def check_data(my_list: list) -> int:
#     for i in range(1,len(a)):
#         if a[i] - 1 != a[i-1]:
#             return a[i] - 1
# print(check_data(a))
#
#
#
#
#
# from random import randint
#
# def create_coeffs(num: int) -> list:
#     return [randint(1, 100) for _ in range(num + 1)]


def create_str(list_coeff: list) -> str:
    lenght = len(list_coeff)
    lst_str = [f"{el}*x^{lenght - idx - 1}" for idx, el in enumerate(list_coeff)]
    return " + ".join(lst_str)


def write_to_file(polynom_string: str, filename: str) -> None:
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(polynom_string)

def write_to_db(....):
    pass

write_to_file(create_str(create_coeffs(10)), "test.txt")

