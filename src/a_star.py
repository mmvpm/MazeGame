# *-* coding: utf-8 *-*

import heapq

from settings import *
from rendering import *



# Эвристическая функция
def f(x, y):
    global n, m
    return (n + 1 - x) ** 2 + (m + 1 - y) ** 2

# Проходит лабиринт, используя алгоритм А*
def a_star(visual = False):
    global a, n, m, dx1, dy1
    
    dist = [i[:] for i in a]
    for i in range(n + 4):
        for j in range(m + 4):
            if a[i][j] != 1:
                dist[i][j] = -1
    # Ставим не 0, чтобы solve() не ушёл в стену, dist которой = 1
    dist[0][2] = dist[1][2] = dist[2][2] = 10
    
    # Визуализация
    if visual:
        a[0][2] = a[1][2] = 8
        a[2][2] = 4
        if rendering_solve:
            update_one(0, 2) # <<<---
            update_one(1, 2) # <<<---
            update_one(2, 2) # <<<---
    
    # Куча
    h = []
    heapq.heappush(h, (f(2, 2), 2, 2))
    while len(h) > 0:
        tmp_f, i, j = heapq.heappop(h)
        
        if visual:
            a[i][j] = 8
            if rendering_solve: update_one(i, j) # <<<---
        
        # Путь найден
        if i == n + 1 and j == m + 1:
            break
        
        for q in range(4):
            ii, jj = i + dx1[q], j + dy1[q]
            if ii < n + 2 and jj < m + 2 and a[ii][jj] != 1 and dist[ii][jj] == -1:
                dist[ii][jj] = dist[i][j] + 1
                heapq.heappush(h, (f(ii, jj), ii, jj))
                
                if visual:
                    a[ii][jj] = 4
                    if rendering_solve: update_one(ii, jj) # <<<---
    
    if visual:
        a[n + 1][m + 1] = a[n + 2][m + 1] = a[n + 3][m + 1] = 8
    
    return dist