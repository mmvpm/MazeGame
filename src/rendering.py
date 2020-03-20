# *-* coding: utf-8 *-*

from settings import *



# Обновляет положение игрока (i, j - смещения)
def draw_player(i = 0, j = 0, player_num = 0):
    global color, x, y
    # (x, y) соответствуют (i, j), поэтому при отрисовке меняем их местами
    
    # Закрашиваем старое положение (Если там нет другого игрока)
    in_one_point = False
    for p2 in range(players):
        if player_num != p2 and x[player_num] == x[p2] and y[player_num] == y[p2]:
            in_one_point = True
    if not in_one_point:
        pygame.draw.rect(win, color[3], (y[player_num] * k, x[player_num] * k, k, k))
    
    # Рисуем новое положение
    pygame.draw.rect(win, color[4], ((y[player_num] + j) * k, (x[player_num] + i) * k, k, k))

# Рисует лабиринт на экране
def draw_maze():
    global a, color
    for i in range(n + 4):
        for j in range(m + 4):
            pygame.draw.rect(win, color[a[i][j]], (j * k, i * k, k, k))

# Пишет текст на экране
def draw_text(message, x, y, color = (0, 0, 0)):
    f = pygame.font.Font(font_path, default_font_size)
    text = f.render(message, 1, color)
    place = text.get_rect(center = (x, y))
    win.blit(text, place)

# Рисует кнопки
def draw_buttons():  
    # Список всех кнопок (x1, y1, x2, y2)
    buttons = []
    
    # У всех кнопок одинаковый
    x = (m + 4) * k + extra // 2 - button_w // 2
    
    # Рисуем кнопки
    for i in range(7):
        y = match[i] * interval + i * button_h
        buttons.append((x, y, x + button_w, y + button_h))
        pygame.draw.rect(win, grey, (x, y, button_w, button_h))
        draw_text(button_name[i], x + button_w // 2, y + button_h // 2)
    
    return buttons

# Подсветка нажатия (i - номер кнопки в списке)
def highlight_button(i):
    x = (m + 4) * k + extra // 2 - button_w // 2
    y = match[i] * interval + i * button_h
    pygame.draw.rect(win, red, (x, y, button_w, button_h), 2)
    pygame.display.update()
    time.sleep(highlight_delay)
    pygame.draw.rect(win, grey, (x, y, button_w, button_h), 2)
    pygame.display.update()

# Для анимации на ходу
def update():
    global a, delay
    draw_maze()
    pygame.display.update()
    time.sleep(delay)

# Оптимизированный update
def update_one(i, j):
    global a, delay
    pygame.draw.rect(win, color[a[i][j]], (j * k, i * k, k, k))
    pygame.display.update()
    time.sleep(delay)


# Параметры кнопок
button_w = 120
button_h = 30
interval = 10

highlight_delay = 0.12
default_font_size = 17
font_path = 'C:\\WINDOWS\\Fonts\\times.TTF'

# Интервалы между кнопками
match = [1, 2, 3, 6, 7, 8, 11]

# Надписи на кнопках
button_name = ['DFS (new)', \
               'Prim (new)', \
               'Kruskal (new)', \
               'DFS (solve)', \
               'BFS (solve)', \
               'A star (solve)', \
               'Save as png']