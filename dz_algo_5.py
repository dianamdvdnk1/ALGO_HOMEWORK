"""Сложность O(n*м)"""


class Solution(object):
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        perimter = 0

        for r in range(rows): #бежим по рядам
            for c in range(cols): #бежим по коллонам
                if grid[r][c]: # найти стену;
                # проверить 4 направления; 

                    # вверхушка
                    if r == 0 or grid[r - 1][c] == 0:
                        perimter += 1
                    # низ
                    if r == rows - 1 or grid[r + 1][c] == 0:
                        perimter += 1
                    # лево
                    if c == 0 or grid[r][c - 1] == 0:
                        perimter += 1
                    # право
                    if c == cols - 1 or grid[r][c + 1] == 0:
                        perimter += 1

        return perimter
