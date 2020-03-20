# *-* coding: utf-8 *-*

from collections import deque

from settings import *
from rendering import *



# DSU
def find(i, p):
    if i != p[i]:
        p[i] = find(p[i], p)
    return p[i]

def union(i, j, p, r):
    i = find(i, p)
    j = find(j, p)
    if i == j:
        return
    if r[i] > r[j]:
        p[j] = i
    else:
        p[i] = j
        if r[i] == r[j]:
            r[j] += 1

def kruskal(visual_type = 'Kruskal'):
    global a, dx1, dy1
    # Список рёбер (случайный вес, вершина1, вершина2)
    edges = []
    for i in range(n + 4):
        for j in range(m + 4):
            if a[i][j] != 1:
                # Смещения
                dx, dy = [0, 2], [2, 0]
                for k in range(2):
                    ii, jj = i + dx[k], j + dy[k]
                    if a[ii][jj] == 0:
                        w = randint(0, 10 ** 9)
                        v = i * (m + 4) + j
                        u = ii * (m + 4) + jj
                        edges.append([w, v, u])
    
    edges.sort()
    
    # DSU
    p = [i for i in range((n + 4) * (m + 4))]
    r = [0 for i in range((n + 4) * (m + 4))]
    
    # Алгоритм Крускала
    for edge in edges:
        w, v, u = edge[0], edge[1], edge[2]
        if find(v, p) != find(u, p):
            union(v, u, p, r)
            # Удаляем стенку
            i, j = v // (m + 4), v % (m + 4)
            ii, jj = u // (m + 4), u % (m + 4)
            a[(i + ii) // 2][(j + jj) // 2] = 0
            
            if rendering and visual_type == 'Kruskal':
                update_one((i + ii) // 2, (j + jj) // 2) # <<<---
    
    # Отрисовка лабиринта разными методами
    if rendering and visual_type == 'Eller':
        for i in range(n + 4):
            for j in range(m + 4):
                if a[i][j] != 1:
                    update_one(i, j) # <<<---
        
    if rendering and visual_type == 'dfs':
        st = [(2, 2, 0, 2)]
        while len(st) > 0:
            i, j, iii, jjj = st[-1][0], st[-1][1], st[-1][2], st[-1][3]
            st.pop()
            for q in range(4):
                ii, jj = i + dx1[q], j + dy1[q]
                if a[ii][jj] != 1 and (ii, jj) != (iii, jjj):
                    st.append((ii, jj, i, j))
                    update_one(ii, jj) # <<<---
    
    if rendering and visual_type == 'bfs':
        u = deque()
        u.append((2, 2, 0, 2))
        while len(u) > 0:
            i, j, iii, jjj = u[0][0], u[0][1], u[0][2], u[0][3]
            u.popleft()
            for q in range(4):
                ii, jj = i + dx1[q], j + dy1[q]
                if a[ii][jj] != 1 and (ii, jj) != (iii, jjj):
                    u.append((ii, jj, i, j))
                    update_one(ii, jj) # <<<---
    
    '''
    # Оставлю это здесь на всякий случай ^_^
    if rendering and visual_type == 'helix':
        i = j = 2
        for q in range(2, n // 2 + 3):
            for j in range(q, m + 4 - q):
                update_one(q, j) # <<<---
            for i in range(q, n + 4 - 1):
                update_one(i, m + 4 - q - 1) # <<<---
            for j in range(m + 4 - q - 1, q - 1, -1):
                update_one(n + 4 - q - 1, j) # <<<---
            for i in range(n + 4 - q - 1, q - 1, -1):
                update_one(i, q) # <<<---  
    '''