import pygame

screen = pygame.display.set_mode([640, 480])

pygame.display.set_caption('Заливка объекта')

# заливка экрана цветом,указанным параметром фунции fill(),

# в “невидимой” копии поверхности отображения

screen.fill([200, 200, 200])

pygame.display.flip()  # смена поверхностей отображения

pygame.time.delay(1000)

screen.fill([255, 255, 255], [220, 50, 200, 50])

pygame.display.flip()  # смена поверхностей отображения

pygame.time.delay(1000)

screen.fill([0, 0, 255], [220, 100, 200, 50])

pygame.display.flip()  # смена поверхностей отображения

pygame.time.delay(1000)

screen.fill([255, 0, 0], [220, 100, 200, 50])

pygame.display.flip()  # смена поверхностей отображения

pygame.time.delay(3000)

screen.fill([255, 255, 255])

screen.fill([255, 0, 0], [250, 50, 70, 70])

screen.fill([0, 255, 0], [320, 50, 70, 70])

screen.fill([0, 0, 255], [250, 120, 70, 70])

screen.fill([0, 255, 255], [320, 120, 70, 70])

pygame.display.flip()  # смена поверхностей отображения

pygame.time.delay(3000)

pygame.quit()
