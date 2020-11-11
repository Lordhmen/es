import math
import pygame


def f_graph(xl):
    yl = math.sin(xl+10)  # функцию менять здесь!
    return (yl)

a = -5  # левая граница для вычисления
b = 5  # правая граница для вычисления

grModeX = 800  # ширина окна
grModeY = 600  # высота окна
pygame.init()
screen = pygame.display.set_mode([grModeX, grModeY], pygame.FULLSCREEN)

sx = grModeX / (b - a)  # масштаб по X
h = 1/sx  # шаг изменения аргумента
xmid = grModeX // 2  # середина области построения по X
ymid = grModeY // 2  # середина области построения по Y

x = a
maxF = f_graph(x)
minF = maxF
while x <= b:
    y = f_graph(x)
    if y < minF:
        minF = y  # определяем минимальное значение функции
    if y > maxF:
        maxF = y  # определяем максимальное значение функции
    x = x + h

sy = grModeY / (maxF - minF)  # масштаб по Y

# рисуем ось X
pygame.draw.line(screen, [255, 255, 255], [0, ymid], [grModeX, ymid])

# рисуем ось Y
pygame.draw.line(screen, [255, 255, 255], [xmid, 0], [xmid, grModeY])

# рисуем график функции
x = a
# y=f_graph(x)

while x <= b:
    y = f_graph(x)
    screen.set_at([xmid + round(sx * x), ymid - round(sy * y)], [255, 255, 255])
    x = x + h
    pygame.time.delay(50)
    pygame.display.flip()

pygame.time.delay(2000)

pygame.quit()
