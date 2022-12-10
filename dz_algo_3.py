"""Сложность O(n*м)"""


class Solution:
    def averageOfLevels(self, root):
        
        if root == None:
            return []
        
        result = []
        
        #сохранение корневого узла на текущем уровне. (случается только один раз)
        curr_level = [root]
        
        
        while curr_level:
            node_val =  [] #значения узлов на текущем уровне
            next_level = [] #левый и правый узлы каждого узла текущего уровня (если есть)
            
            #обход каждого узла, присутствующего на текущем уровне
            for node in curr_level:
                node_val.append(node.val) 
                
                #добавление левого и правого узлов к next_level, чтобы перемещаться по горизонтали
                if node.left:
                    next_level.append(node.left)
                    
                if node.right:
                    next_level.append(node.right)
                    
            
            #cчитаем среднее значение
            result.append(sum(node_val)/len(node_val))
            
            #изменение уровня на следующий уровень узлов
            curr_level = next_level
        
        return result