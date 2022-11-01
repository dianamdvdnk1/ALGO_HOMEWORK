"""
The second Homework for Algo.
Cложность алгоритма О(n).
"""

def function2(num: int):
    num_itog = 0
    if num == 1: #проверка кол-ва команд
        return 0
    while num > 1: #пока кол-во команд больше 1 -- бежим по циклу
        if num % 2 == 0: #четность
            num = num // 2 #из условия задачи
            num_itog += num #увеличиваем кол-во матчей
        else:
            num_itog += (num - 1) / 2 #иначе -- увеличиваем по-другому
            num = ((num - 1) / 2 )+ 1 #уменьшаем кол-во команд после сыгранных матчей
    return num_itog #сюдааааа
