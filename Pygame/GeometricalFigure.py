import pygame
import math

pygame.init()


def run_game():
    clock = pygame.time.Clock()
    FPS = 60

    # Цикл игры
    running = True
    while running:
        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # проверяет закрытие окна
            if event.type == pygame.QUIT:
                running = False

        # Обновление
        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()


screan = pygame.display.set_mode([600, 600])
screan.fill([255, 255, 255])

# Значения
plotPoints = [[0, 0], [30, 30], [60, 0], [90, 30], [120, 0]]
plotPointsSin = []
R = 100
s = 10
d = 20

for i in range(360):
    t = 6.28 * i / 360
    x = 300 + ((R + s) * math.cos(t) - d * math.cos((R + s) / s * t))
    y = 300 + ((R + s) * math.sin(t) - d * math.sin((R + s) / s * t))
    plotPointsSin.append([x, y])
fontObj = pygame.font.SysFont("arial", 30)

# Фигуры
pygame.draw.circle(screan, [255, 0, 0], [100, 100], 30, 0)
pygame.draw.rect(screan, [0, 255, 0], [30, 130, 100, 50], 0)
pygame.draw.lines(screan, [0, 0, 255], False, plotPoints, 4)
pygame.draw.lines(screan, [255, 0, 255], False, plotPointsSin, 2)

# Текст
text = fontObj.render("Как жизнь?", True, (255, 255, 0), (0, 0, 255))
screan.blit(text, [160, 180])


run_game()
