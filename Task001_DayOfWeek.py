# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# *Пример:*
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def CheckDayOfWeek(x):
    if x==6 or x ==7:
        print(x, '-> да')
    else: print(x, '-> нет')

day=int(input(f"Введите номер дня недели, и я отвечу, выходной ли это "))
CheckDayOfWeek(day)