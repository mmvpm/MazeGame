# *-* coding: utf-8 *-*

from settings import *
from rendering import *



# Начальное состояние
def new_maze():
    global a, n, m, dx2, dy2
    
    for i in range(n + 4):
        for j in range(m + 4):
            a[i][j] = 0
    if rendering: update() # <<<---
    
    for i in range(1, n + 4, 2):
        for j in range(m + 4):
            a[i][j] = 1
    if rendering: update() # <<<---
    
    for i in range(1, m + 4, 2):
        for j in range(n + 4):
            a[j][i] = 1
    if rendering: update() # <<<---
    
    # Стенки
    for i in range(n + 4):
        a[i][0] = a[i][1] = a[i][m + 2] = a[i][m + 3] = 1
    for i in range(m + 4):
        a[0][i] = a[1][i] = a[n + 2][i] = a[n + 3][i] = 1
    
    # Вход
    a[0][2] = a[1][2] = 0
    if rendering: update() # <<<---