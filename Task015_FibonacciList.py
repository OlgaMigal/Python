# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Примечание:
# Алгоритм смотрим тут: https://ru.wikipedia.org/wiki/Негафибоначчи
# Вам понадобится рекурсивный вызов функции или сделайте в виде списка.


def task015():
    fib_number = int(input('Введите число: '))
    answer = [0]
    for i in range(1, fib_number+1):
        answer.append(fibonacci(i))
        answer.insert(0, nega_fibonacci(i))
    print(f'Для k = {fib_number} список будет выглядеть так: \n{answer}')


def fibonacci(n):
    if n in [1, 2]: return 1
    else: return(fibonacci(n-1)+fibonacci(n-2))


def nega_fibonacci(n):
    if -n==-1: return 1
    if -n==-2: return -1
    else: return(nega_fibonacci(n - 2) - nega_fibonacci(n - 1))

task015()