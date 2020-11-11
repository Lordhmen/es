import pygame

pygame.init()


def run_game():
    clock = pygame.time.Clock()
    FPS = 60
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()

    pygame.quit()


center = [200, 300]
sizeDisplay = [500, 500]
cellSize = [50, 50]

screan = pygame.display.set_mode(sizeDisplay)
screan.fill([205, 238, 255])

gridX = []  # Двумерный массив сетки X
gridY = []  # Двумерный массив сетки Y
ofsetGrid = [center[0] % cellSize[0], center[1] % cellSize[1]]
for i in range(int(sizeDisplay[0] / cellSize[0]) + 2):
    gridX.append(i * cellSize[0] - ofsetGrid[0])

for i in range(int(sizeDisplay[1] / cellSize[1]) + 2):
    gridY.append(i * cellSize[1] - ofsetGrid[1])

for i in gridX:
    pygame.draw.line(screan, [101, 143, 163], [0, i], [sizeDisplay[0], i])

for i in gridY:
    pygame.draw.line(screan, [101, 143, 163], [i, 0], [i, sizeDisplay[0]])

pygame.draw.line(screan, [101, 143, 163], [0, center[1]], [sizeDisplay[0], center[1]], 3)
pygame.draw.lines(screan, [101, 143, 163], False,
                  [[sizeDisplay[0], center[1]], [sizeDisplay[0] - cellSize[0] / 2, center[1] - cellSize[1] / 3],
                   [sizeDisplay[0], center[1]], [sizeDisplay[0] - cellSize[0] / 2, center[1] + cellSize[1] / 3]]
                  , 4)

pygame.draw.line(screan, [101, 143, 163], [center[0], 0], [center[0], sizeDisplay[1]], 3)
pygame.draw.lines(screan, [101, 143, 163], False,
                  [[center[0], 0], [center[0] + cellSize[0] / 3, 0 + cellSize[1] / 2],
                   [center[0], 0], [center[0] - cellSize[0] / 3, 0 + cellSize[1] / 2]]
                  , 4)

fontObj = pygame.font.SysFont("arial", 20)
ziro = fontObj.render("0", True, (0, 0, 0))
one = fontObj.render("1", True, (0, 0, 0))
x = fontObj.render("x", True, (0, 0, 0))
y = fontObj.render("y", True, (0, 0, 0))
screan.blit(ziro, [center[0] - cellSize[0] / 4, center[1] + cellSize[1] / 8])
screan.blit(one, [center[0] + cellSize[0], center[1]])
screan.blit(one, [center[0] - cellSize[0] / 4, center[1] - cellSize[1] * 1.3])
screan.blit(x, [sizeDisplay[0] - cellSize[0] / 4, center[1]])
screan.blit(y, [center[0], 0])

plotPointsSin = []
for x in range(-200, 200):
    y = - (x ** 2 + x * 110) / 20
    plotPointsSin.append([x + center[0], y + center[1]])

pygame.draw.lines(screan, [185, 83, 94], False, plotPointsSin, 2)

run_game()
