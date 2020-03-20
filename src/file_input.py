# *-* coding: utf-8 *-*



# Возвращает последнее значение в строке
def get(file):
    return list(file.readline().rstrip().split())[-1]


# Ввод данных из файла настроек
def input_settings():
    fail = False
    
    try:
        file = open('settings.txt', 'r')
        
        n = int(get(file))
        m = int(get(file))
        players = int(get(file))

        rendering = int(get(file))
        rendering_solve = int(get(file))
        delay = float(get(file))
        
        file.close()
        
        n -= 1 - n % 2
        m -= 1 - m % 2
        # Оптимальный размер клетки
        k = max(1, min(10, 600 // n, 1000 // m))
        
        if n < 1 or \
           m < 1 or \
           not 1 <= players <= 2 or \
           not 0 <= rendering <= 1 or \
           not 0 <= rendering_solve <= 1 or \
           not 0 <= delay <= 100:
            
            fail = True
    
    except:
        # Если settings.txt повреждён, то оставляем всё как есть
        fail = True
    
    if fail:
        return -1
    
    return (n, m, k, players, rendering, rendering_solve, delay)