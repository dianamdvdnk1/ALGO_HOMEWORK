"""
The first Homework for Algo.
Сложность алгоритма O(n).
"""

def function1(number: int):
    count = 0
    while number != 0: #пока число не равно нулю -- "бежим" по циклу
        if number % 2 == 0: #если число четное -- делим нацело на 2
            number //= 2
        else: #иначе -- число -1
            number -= 1
        count += 1 #увеличиваем счетчик
    return count

