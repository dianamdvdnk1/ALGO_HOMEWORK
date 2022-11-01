"""
The sixth Homework for Algo.
Сложность алгоритма зависит от входных данных
"""

def function6(num: int):
    p=0
    while(num!=1): #пока не равно 1 -- бежим
        if num%2==0: #четность
            num=num//2 #делим на 2
            
        else:
            num=(3*num)+1 #иначе другое вычисление
        p+=1 #увеличиваем з
        
    return p
            
def function6_1(lo: int, hi: int, k: int):
    
    temp=sorted(range(lo,hi+1),key = lambda x:function6(x)) #темп -- сортированный список в промежутке от lo до hi, а key -- это сортировка по функции6 
    return temp[k-1] #возвращаем катый -1

print(function6_1(7,11,4))