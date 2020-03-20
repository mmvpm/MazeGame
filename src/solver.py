# *-* coding: utf-8 *-*

from settings import *
from rendering import *



# Проходит лабиринт зная массив dist
def solve(dist, fin_i, fin_j):
    global a, n, m, dx1, dy1
    
    # Прямой порядок изменения для анимации
    to_change = [(n + 2, m + 1), (n + 3, m + 1)]
    
    i = fin_i
    j = fin_j
    while not (i == 2 and j == 2):
        for k in range(4):
            ii, jj = i + dx1[k], j + dy1[k]
            if dist[ii][jj] + 1 == dist[i][j]:
                to_change.append((i, j))
                i, j = ii, jj
                break
    to_change += [(0, 2), (1, 2), (2, 2)]
    
    # Отрисовка
    for cell in to_change[::-1]:
        i, j = cell[0], cell[1]
        a[i][j] = 3
        if rendering_solve: update_one(i, j) # <<<---


# Находит самую удалённую от входа клетку
def max_cell(dist):
    global n, m
    
    max_i = max_j = 2
    for i in range(n + 4):
        for j in range(m + 4):
            if dist[i][j] > dist[max_i][max_j]:
                max_i, max_j, = i, j
    if max_i == n + 1 and max_j == m + 1:
        max_i = n + 3
    
    return (max_i, max_j)