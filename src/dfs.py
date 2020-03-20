# *-* coding: utf-8 *-*

from settings import *
from rendering import *



def dfs():
    global a, n, m
    
    # Смещения
    dx = [0, 0, -2, +2]
    dy = [-2, +2, 0, 0]
    
    st = []
    st.append((n + 1, m + 1))
    while len(st) > 0:
        i, j = st[-1][0], st[-1][1]
        a[i][j] = 2
        
        # Есть ли непосещённые соседи у клетки (i, j)
        free_cells = False
        for k in range(4):
            if a[i + dx[k]][j + dy[k]] == 0:
                free_cells = True    
        
        if free_cells:
            # Случайный непосещённый сосед клетки (i, j)
            while True:
                idx = randint(0, 3)
                if a[i + dx[idx]][j + dy[idx]] == 0:
                    next_i, next_j = (i + dx[idx], j + dy[idx])
                    break
            
            a[(i + next_i) // 2][(j + next_j) // 2] = 2
            st.append((next_i, next_j))
            if rendering: update_one((i + next_i) // 2, (j + next_j) // 2) # <<<---
            
        else:
            st.pop()
    
    # Для удобства
    for i in range(n + 4):
        for j in range(m + 4):
            if a[i][j] == 2:
                a[i][j] = 0


# Просто гуляет по лабиринту
def dfs_walk(visual = False):
    global a, n, m, dx1, dy1
    
    dist = [i[:] for i in a]
    for i in range(n + 4):
        for j in range(m + 4):
            if a[i][j] != 1:
                dist[i][j] = -1
    # Ставим не 0, чтобы solve() не ушёл в стену, dist которой = 1
    dist[0][2] = dist[1][2] = dist[2][2] = 10
    
    i, j = 0, 2
    st = [(i, j)]
    while len(st) > 0 and (i, j) != (n + 1, m + 1):
        i, j = st.pop()
        a[i][j] = 6
        if visual and rendering_solve: update_one(i, j) # <<<---
        for q in range(4):
            ii, jj = i + dx1[q], j + dy1[q]
            if (1 <= ii <= n + 1) and (1 <= jj <= m + 1) and not a[ii][jj] in [1, 6]:
                st.append((ii, jj))
                a[ii][jj] = 4
                dist[ii][jj] = dist[i][j] + 1
                if visual and rendering_solve: update_one(ii, jj) # <<<---
    
    a[n + 2][m + 1] = a[n + 3][m + 1] = 6
    if visual and rendering_solve: 
        update_one(n + 2, m + 1) # <<<---
        update_one(n + 3, m + 1) # <<<---
    
    return dist