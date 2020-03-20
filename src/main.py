# *-* coding: utf-8 *-*

from settings import *
from rendering import *
from save_image import *

from dfs import *
from bfs import *
from prim import *
from a_star import *
from solver import *
from kruskal import *
from auto_move import *
from start_position import *



# start pygame
pygame.init()
win = pygame.display.set_mode((width, height))
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Maze')
win.fill(white)
pygame.display.update()


# Рисуем лабиринт
new_maze()
kruskal()
# Выход
a[n + 2][m + 1] = a[n + 3][m + 1] = 0

# Максимальный путь
max_i, max_j = max_cell(bfs())
a[max_i][max_j] = 5
update() # <<<---


# Рисуем кнопки + Получаем список всех кнопок
bs = draw_buttons()


# Рисуем игроков
for i in range(players):
    draw_player(0, 0, i)


while not end:
    pygame.time.delay(75)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
        
        if not (solve_dfs or solve_bfs or solve_a_star) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # click_x, click_y
            cx, cy = event.pos
            if bs[0][0] <= cx <= bs[0][2] and bs[0][1] <= cy <= bs[0][3]:
                restart_dfs = True
                in_game = False
                highlight_button(0)
            if bs[1][0] <= cx <= bs[1][2] and bs[1][1] <= cy <= bs[1][3]:
                restart_prim = True
                in_game = False
                highlight_button(1)
            if bs[2][0] <= cx <= bs[2][2] and bs[2][1] <= cy <= bs[2][3]:
                restart_kruskal = True
                in_game = False
                highlight_button(2)
            if bs[3][0] <= cx <= bs[3][2] and bs[3][1] <= cy <= bs[3][3]:
                solve_dfs = True
                in_game = False
                highlight_button(3)
            if bs[4][0] <= cx <= bs[4][2] and bs[4][1] <= cy <= bs[4][3]:
                solve_bfs = True
                in_game = False
                highlight_button(4)
            if bs[5][0] <= cx <= bs[5][2] and bs[5][1] <= cy <= bs[5][3]:
                solve_a_star = True
                in_game = False
                highlight_button(5)
            if bs[6][0] <= cx <= bs[6][2] and bs[6][1] <= cy <= bs[6][3]:
                create_image()
                highlight_button(6)
    
    
    if in_game:
        # Обработка нажатий + обновление положения игрока
        keys = pygame.key.get_pressed()
        
        # Первый игрок
        if keys[pygame.K_LEFT] and a[x[0]][y[0] - 1] != 1:
            draw_player(0, -1, 0)
            y[0] -= 1
            if thank_you_auto_move: auto_move((x[0], y[0] + 1), 0)
        if keys[pygame.K_RIGHT] and a[x[0]][y[0] + 1] != 1:
            draw_player(0, 1, 0)
            y[0] += 1
            if thank_you_auto_move: auto_move((x[0], y[0] - 1), 0)
        if keys[pygame.K_DOWN] and a[(x[0] + 1) % (n + 4)][y[0]] != 1:
            draw_player(1, 0, 0)
            x[0] += 1
            if thank_you_auto_move: auto_move((x[0] - 1, y[0]), 0)
        if keys[pygame.K_UP] and a[x[0] - 1][y[0]] != 1:
            draw_player(-1, 0, 0)
            x[0] -= 1
            if thank_you_auto_move: auto_move((x[0] + 1, y[0]), 0)
        
        # Второй игрок
        # Переключение ввода, если 2 игрока
        p = min(1, players - 1)
        if keys[pygame.K_a] and a[x[p]][y[p] - 1] != 1:
            draw_player(0, -1, p)
            y[p] -= 1
            if thank_you_auto_move: auto_move((x[p], y[p] + 1), p)
        if keys[pygame.K_d] and a[x[p]][y[p] + 1] != 1:
            draw_player(0, 1, p)
            y[p] += 1
            if thank_you_auto_move: auto_move((x[p], y[p] - 1), p)
        if keys[pygame.K_s] and a[(x[p] + 1) % (n + 4)][y[p]] != 1:
            draw_player(1, 0, p)
            x[p] += 1
            if thank_you_auto_move: auto_move((x[p] - 1, y[p]), p)
        if keys[pygame.K_w] and a[x[p] - 1][y[p]] != 1:
            draw_player(-1, 0, p)
            x[p] -= 1
            if thank_you_auto_move: auto_move((x[p] + 1, y[p]), p)
                
        # Условие прохождения лабиринта
        for i in range(players):
            if x[i] == n + 3 and y[i] == m + 1:
                in_game = False
        
    
    if restart_dfs or restart_prim or restart_kruskal:
        new_maze()
        
        if restart_dfs:
            dfs()
        elif restart_prim:
            prim()
        else:
            if vt_index == -1:
                vt = visual_types[vt_count]
                vt_count = (vt_count + 1) % len(visual_types)
            else:
                vt = visual_types[vt_index]
            kruskal(vt)
        
        # Выход
        a[n + 2][m + 1] = a[n + 3][m + 1] = 0
        
        # Максимальный путь
        max_i, max_j = max_cell(bfs())
        a[max_i][max_j] = 5
        
        update() # <<<---

        for i in range(players):
            x[i], y[i] = 0, 2
            draw_player(0, 0, i)
        
        in_game = True
        restart_dfs = False
        restart_prim = False
        restart_kruskal = False
    
    if solve_dfs:
        solve(dfs_walk(True), n + 1, m + 1)
        update() # <<<---
        solve_dfs = False
        
    if solve_bfs:
        solve(bfs(True), n + 1, m + 1)
        update() # <<<---
        solve_bfs = False
    
    if solve_a_star:
        solve(a_star(True), n + 1, m + 1)
        update() # <<<---
        solve_a_star = False
    
    pygame.display.update()


pygame.quit()