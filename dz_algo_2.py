"""Сложность O(n)"""
"""Похожа на егэшную и предыдущую задачу"""
class Solution:
    def getDecimalValue(self, head):
        stroka = ""# создаём строку для добавления всех елементов 
        while head: #пока цикл не пустой, бежим по всем элементам 
            strocka += str(head.val)  #добавляем его значения
            head = head.next #идем к следующему
        return int(stroka, 2) #переводим  из десятичной в двоичную сс