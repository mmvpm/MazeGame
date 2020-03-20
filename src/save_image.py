# *-* coding: utf-8 *-*

from PIL import Image, ImageDraw

from settings import *



# Сохраняет нарисованный лабиринт в виде картинки
def create_image():
    global a, n, m, color
    
    # Длина и толщина стенок
    k, kk = 10, 1
    width = kk * (m + 3) // 2 + k * (m + 1) // 2
    height = kk * (n + 3) // 2 + k * (n + 1) // 2
    
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)
        
    for i in range(1, n + 3):
        for j in range(1, m + 3):
            x, y = kk, kk
            if i % 2 == 0:
                x = k
            if j % 2 == 0:
                y = k
            for ii in range(x):
                for jj in range(y):
                    draw.point((((j + 1) // 2 - 1) * k + (j // 2) * kk + jj, \
                                ((i + 1) // 2 - 1) * k + (i // 2) * kk + ii), color[a[i][j]])
    
    image.save('maze' + str(randint(0, 10 ** 9)) + '.png', 'png')