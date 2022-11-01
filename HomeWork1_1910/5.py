"""The fifth homework for algo.
Сложность алгоритма O(n), 3 переменные.
"""
import random

def function5(nums: int, c: int): # Проверяем пустоту в nums 
    if not nums:
        return # рандомим число
    random_1 = random.choice(nums) # список из чисел меньше рана
    levo = [x for x in nums if x > random_1] # список из чисел равных рану
    center = [x for x in nums if x == random_1] # список из чисел больше рана
    pravo = [x for x in nums if x < random_1]
    L, M = len(levo), len(center)
    if c <= L:
        return function5(levo, c)
    elif c > L + M: # Запускаем рекурсию с k меньшим, чем L + m
        return function5(pravo, c - L - M)
    else:
        return center[0] # Возвращем центральное значение