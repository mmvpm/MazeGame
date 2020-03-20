# *-* coding: utf-8 *-*

from settings import *
from rendering import *



# Более автоматизированное перемещение игрока
def auto_move(prev = (0, 2), player_num = 0):
    global x, y, n, m, dx1, dy1
    
    no_variants = True
    while no_variants:
        # Сколько вариантов выбора пути в данной клетке
        count_directions = 0
        next_x, next_y = x[player_num], y[player_num]
        for q in range(4):
            i, j = x[player_num] + dx1[q], y[player_num] + dy1[q]
            if i <= n + 3 and j <= m + 3 and a[i][j] != 1 and prev != (i, j):
                count_directions += 1
                next_x, next_y = i, j
        
        if count_directions == 1:
            draw_player(next_x - x[player_num], next_y - y[player_num], player_num)
            pygame.display.update()
            time.sleep(0.05)
            prev = (x[player_num], y[player_num])
            x[player_num], y[player_num] = next_x, next_y
        else:
            no_variants = False