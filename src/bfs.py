# *-* coding: utf-8 *-*

from collections import deque

from settings import *
from rendering import *



# Находит расстояния до каждой клетки (bfs)
def bfs(visual = False):
    global a, n, m, dx1, dy1
    
    dist = [i[:] for i in a]
    for i in range(n + 4):
        for j in range(m + 4):
            if a[i][j] != 1:
                dist[i][j] = -1
    # Ставим не 0, чтобы solve() не ушёл в стену, dist которой = 1
    dist[0][2] = dist[1][2] = dist[2][2] = 10
    
    d = deque()
    d.append((2, 2))
    
    # Визуализация
    if visual:
        a[0][2] = a[1][2] = 7
        a[2][2] = 4
        if rendering_solve:
            update_one(0, 2) # <<<---
            update_one(1, 2) # <<<---
            update_one(2, 2) # <<<---
    
    while len(d) > 0:
        i, j = d[0][0], d[0][1]
        
        if visual:
            a[i][j] = 7
            if rendering_solve: update_one(i, j) # <<<---
        
        d.popleft()
        for k in range(4):
            ii, jj = i + dx1[k], j + dy1[k]
            if ii < n + 2 and jj < m + 2 and a[ii][jj] != 1 and dist[ii][jj] == -1:
                dist[ii][jj] = dist[i][j] + 1
                d.append((ii, jj))
                
                if visual:
                    a[ii][jj] = 4
                    if rendering_solve: update_one(ii, jj) # <<<---
    
    if visual:
        a[n + 1][m + 1] = a[n + 2][m + 1] = a[n + 3][m + 1] = 7
                
    return dist