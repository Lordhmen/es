import random

import pygame

pygame.init()

screen = pygame.display.set_mode([640, 480])

pygame.display.set_caption('Цветные точки')

for i in range(10000):  # рисуем в цикле 1000 точек

    x = random.randint(0, 639)  # случайное значения координаты X

    y = random.randint(0, 479)  # случайное значения координаты Y

    R = random.randint(0, 254)  # случайное значение красного цвета

    G = random.randint(0, 254)  # случайное значение зеленого цвета

    B = random.randint(0, 254)  # случайное значение синего цвета

    screen.set_at([x, y], [R, G, B])  # рисуем точку - меняем цвет пикселя

    pygame.display.flip()

pygame.time.delay(3000)

pygame.quit()
