'''Сложность алгоритма O(n)'''


class Solution(object):
    def hasCycle(self, head):
        try: #избежание ошибки
            slow = head #начальной точке равен слоу
            fast = head.next #следующей точке
            while slow is not fast: #пока слоу не в точке с фаст бежим по каждому элементу
                slow = slow.next #переходим дальше на 1
                fast = fast.next.next #переходим дальше на 2
            return True
        except:
            return False