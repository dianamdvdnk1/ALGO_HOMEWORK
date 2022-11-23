"""Сложность алгоритма == O(n)^2"""

def uniquePathsWithObstacles(obstacleGrid):
    dp = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]# Создаем матрицу по размеру входных данных
    dp[0][0] = 1# Первый элемент = 1
    for i in range(len(obstacleGrid)): # Проход по списку
        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[i][j] == 1: # Если найден камень
                dp[i][j] = 0 # Отмечаем камень
            elif i > 0 or j > 0: # Если индекс больше 0
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]# То прибавляем кол-во путей в матрицу
    return dp[-1][-1] # Выводим последний элемент матрицы