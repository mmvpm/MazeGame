# *-* coding: utf-8 *-*

import time
import pygame
from random import randint

from file_input import input_settings



# Состояние проекта
release = True

# Окно игры, переопределено в main.py
win = pygame.display.set_mode((1, 1))


# Параметры (высота, ширина, размер клетки):
n = 41
m = 71
k = 10

# Количество игроков
players = 1


# Отрисовка в реальном времени
rendering = True
rendering_solve = True
delay = 0.003


# Ввод данных из файла настроек
result = input_settings()
if result != -1:
    n, m, k, players, rendering, rendering_solve, delay = result


# Поле (определяем после ввода)
a = [[0] * (m + 4) for i in range(n + 4)]

# Координаты игроков
x = [0] * players
y = [2] * players


# Если vt_index == -1, то стили меняются по порядку
visual_types = ['Kruskal', 'Eller', 'dfs', 'bfs']
vt_index = -1
vt_count = 0

# Параметры отрисовки лабиринта на экране
extra = 150
height = max(330, k * (n + 4))
width = k * (m + 4) + extra

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 129, 0)
orange = (250, 100, 0)
dark = (130, 130, 130)
yellow = (200, 200, 0)
brown = (110, 50, 20)
grey = (220, 220, 220)
color = [white, black, white, green, red, orange, dark, yellow, brown]


# Режимы игры
end = False
in_game = True

restart_dfs = False
restart_prim = False
restart_kruskal = False

solve_dfs = False
solve_bfs = False
solve_a_star = False

thank_you_auto_move = True


# Смещения
dx1 = [0, 0, -1, +1]
dy1 = [-1, +1, 0, 0]

dx2 = [0, 0, -2, +2]
dy2 = [-2, +2, 0, 0]