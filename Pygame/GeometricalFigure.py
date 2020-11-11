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


screan = pygame.display.set_mode([300, 300])
screan.fill([255, 255, 255])

# Значения
plotPoints = [[0, 0], [30, 30], [60, 0], [90, 30], [120, 0]]
plotPointsSin = []
for x in range(0, 300):
    y = int(math.sin(x / 300 * 4 * math.pi) * 150 + 150)
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
