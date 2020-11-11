import math
import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

# рисуем ось X
pygame.draw.line(screen, [255, 255, 255], [0, 300], [800, 300])

# рисуем ось Y
pygame.draw.line(screen, [255, 255, 255], [400, 0], [400, 600])

# рисуем график функции
R = 100
s = 10
d = 20
r= 50
m=2/5
# for t in range(100000):
#     # Эпициклоида 2
#     x = 150 + (r + m * r) * math.cos(m * t) - m * r * math.cos(t + m * t)
#     y = 150 + (r + m * r) * math.sin(m * t) - m * r * math.sin(t + m * t)
#     screen.set_at([int(round(x + 100)), int(round(y))], [255, 255, 255])
#     pygame.time.delay(10)
#     pygame.display.flip()

for i in range(360):
    t = 6.28 * i / 360
    # Эпициклоида
    # x = 300 + ((R + s) * math.cos(t) - d * math.cos((R + s) / s * t))
    # y = 300 + ((R + s) * math.sin(t) - d * math.sin((R + s) / s * t))
    # Гипоциклоида
    x = 300 + ((R - s) * math.cos(t) + d * math.cos((R - s) / s * t))
    y = 300 + ((R - s) * math.sin(t) - d * math.sin((R - s) / s * t))
    screen.set_at([int(round(x + 100)), int(round(y))], [255, 255, 255])
    pygame.time.delay(10)
    pygame.display.flip()

pygame.time.delay(2000)
pygame.quit()
