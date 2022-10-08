# 3. Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
# *Пример:*
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


def Task003():
    x = int(input("x: "))
    y = int(input("y: "))
    QuadrantPoint(x, y)


def QuadrantPoint(a, b):
    if a > 0 and b > 0: print (f"x={a}; y={b} -> 1")
    elif a < 0 and b > 0: print (f"x={a}; y={b} -> 2")
    elif a < 0 and b < 0: print (f"x={a}; y={b} -> 3")
    elif a > 0 and b < 0: print (f"x={a}; y={b} -> 4")
    else: print("Оба значения должны быть отличны от 0")

Task003()
