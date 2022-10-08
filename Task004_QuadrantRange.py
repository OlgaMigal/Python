# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).

def Task004():
    x = int(input('Введите квадрант: '))
    QuadrantRange(x)


def QuadrantRange(g):
    if g == 1: print ('(x; y) = (+; +)')
    elif g == 2: print('(x; y) = (-; +)')
    elif g == 3: print('(x; y) = (-; -)')
    elif g == 4: print('(x; y) = (+; -)')
    else: print(f'Квадранта {g} не существует')

Task004()