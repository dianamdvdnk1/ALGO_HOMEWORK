""""Сложность O(n)"""


def getDescentPeriods(prices):
    n = len(prices) #новая переменная == длине прайсис
    dp = [1] * n #создаем список с единицами из-за того, что цены известны сначала
    for i in range(1, n): #бежим по индексам
        if prices[i] == prices[i - 1] - 1: #если совпадает, то -1 
            dp[i] += dp[i - 1] #увеличиваем счетчик
    return sum(dp) #возвращаем сумму элементов