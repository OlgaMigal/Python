# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Что-то не вышло у меня нормально вывести последовательное умножение.
# Пробовала строкой и join, но какая-то фигня получается.
# Здесь тоже фигня, список в списке, но хотя бы логика прослеживается.

number = int(input(f'Введите число: '))
product_numbers = 1
for i in range(1, number+1):
    product_numbers*=i
    print(product_numbers, end = "  ")

print()
finish = [1]
second = [1]
for i in range(2, number+1):
    finish.append(f'{second}*{i}')
    second.append(f'*{i}')

print(finish)
