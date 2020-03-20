# *-* coding: utf-8 *-*

from settings import *
from rendering import *



# Нумерация вершин
def num(i, j):
    global n, m
    return (i // 2 - 1) * (m // 2 + 1) + (j // 2 - 1)

def anti_num(num):
    global n, m
    return ((num // (m // 2 + 1) + 1) * 2, (num % (m // 2 + 1) + 1) * 2)

def prim():
    global a, n, m, dx2, dy2
    
    # Всего вершин
    N = (n // 2 + 1) * (m // 2 + 1)
    
    # Список смежности
    g = [[] for i in range(N)]
    for i in range(2, n + 2):
        for j in range(2, m + 2):
            if a[i][j] == 1:
                continue
            for q in range(4):
                ii, jj = i + dx2[q], j + dy2[q]
                if 2 <= ii <= n + 1 and 2 <= jj <= m + 1 and a[ii][jj] != 1:
                    g[num(i, j)].append((ii, jj, randint(1, 10 ** 1)))
    
    # Заведомо больше всех возможных значений
    inf = 10 ** 18
    
    # Минимальное ребро в множество уже взятых вершин
    dist = [inf] * N
    dist[num(2, 2)] = 0
    
    # Рассмотрена вершина или нет
    used = [False] * N
    
    # Номер вершины, в которую ведет минимальное ребро (dist)
    end_v = [inf] * N
    end_v[num(2, 2)] = num(2, 2)
    
    for cnt in range(N):
        # Ищем вершину с минимальным ребром в уже взятые вершины
        min_v = -1
        for j in range(N):
            if not used[j] and (min_v == -1 or dist[j] < dist[min_v]):
                min_v = j
        used[min_v] = True
        
        # Удаляем стенку
        i, j = anti_num(min_v)
        ii, jj = anti_num(end_v[min_v])
        a[(i + ii) // 2][(j + jj) // 2] = 0
        if rendering: update_one((i + ii) // 2, (j + jj) // 2) # <<<---
                
        # Обновление соседей для найденной вершины
        for u in g[min_v]:
            i, j, w = u[0], u[1], u[2]
            if w < dist[num(i, j)]:
                dist[num(i, j)] = w
                end_v[num(i, j)] = min_v