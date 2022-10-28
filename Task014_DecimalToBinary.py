# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> '101101'
# 3 -> '11'
# 2 -> '10'
# Примечание: Результат вернуть в виде строки. Не использовать функции преобразования типов: bin

def task014():
    decimal_number = int(input("Введите число: "))
    binary_string = ""
    temp_number = decimal_number
    while temp_number!=0:
        binary_string = str(temp_number%2)+binary_string
        temp_number //=2
    print(f'{decimal_number} -> {binary_string}')


task014()