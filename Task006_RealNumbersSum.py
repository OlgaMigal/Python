# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782     -> 23
# - 0,56     -> 11
# - 187,6778 -> 44
# Примечание: Программа должна работать для любого количества цифр в числе.

number = input(f'Введите вещественное число: ')
real_sum = 0
for el in number:
    if el.isdigit():
        real_sum+=int(el)
print(f'{number}    -> {real_sum}')