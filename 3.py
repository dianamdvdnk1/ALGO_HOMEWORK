"""The third Homework for Algo.
Сложность алгоритма = O(n). 
"""


def function3(ukrash:str, kamen: str): #принммает 2 строчки
    count = 0 #счетчик
    for kamen_1 in kamen: #ищем в камнях переменную
        if kamen_1 in ukrash: #ищем в украшениях переменную
            count += 1 #увеличиваем счетчик
    return count #сюдааааааааааааааа
