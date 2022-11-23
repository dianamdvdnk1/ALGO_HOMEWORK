"""Сложность алгоритма = O(n)"""


def maxProfit(prices):
        profit = 0
        cnt = 0
        for i in range(1, len(prices)): #бежим по длине
            if cnt == 2: #провекрка
                return profit
            if prices[i] - prices[i - 1] > 0: #разность соседейи больше нуля
                profit += prices[i] - prices[i-1] #прибавлчяем разность 
                cnt += 1 #увеличиваем счетчик
        return profit