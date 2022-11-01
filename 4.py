"""
The forth Homework for Algo.
Сложность алгоритма n(log(n))
"""


def minimumAbsDifference(arr: list):
        x=arr #берем список
        x.sort() #сортируем список
        ans=[] #создаем список
        min_diff=10**7 #так надо(переменная для сравнения)
        for i in range(len(x)-1): #проходимся по парам в списке
            temp=x[i+1]-x[i] #разность пар(создание новой переменной)
            if temp < min_diff: #сравниваем 
                min_diff=temp #записываем минимум
        for i in range(len(x)-1): #проходимся по парам в списке
            temp=abs(x[i+1]-x[i]) #разность пар по модулю (создание новой переменной)
            if temp==min_diff: #записываем в ответ, если темп == миним разнице
                ans.append([x[i],x[i+1]]) #та самая запись
        return ans 
