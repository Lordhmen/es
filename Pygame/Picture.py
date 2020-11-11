import pygame
import random
import math

pygame.init()

class MyBallClass(pygame.sprite.Sprite):

    def __init__(self, imageFile, location, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imageFile)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > widht:
            coef = -(abs(self.speed[0]) / self.speed[0])
            self.speed[0] = coef * (Clamp(abs(self.speed[0]) * random.uniform(0.5, 2), 1.5, 6))
        if self.rect.top < 0 or self.rect.bottom > height:
            coef = -(abs(self.speed[1]) / self.speed[1])
            self.speed[1] = coef * (Clamp(abs(self.speed[1]) * random.uniform(0.5, 2), 1.5, 6))

def run_game():
    clock = pygame.time.Clock()
    FPS = 60

    # Цикл игры
    running = True
    while running:
        screan.fill([255, 255, 255])

        # Держим цикл на правильной скорости
        clock.tick(FPS)
        # Ввод процесса (события)
        for event in pygame.event.get():
            # проверяет закрытие окна
            if event.type == pygame.QUIT:
                running = False

        # Обновление
        Update()

        # После отрисовки всего, переворачиваем экран
        pygame.display.flip()

    pygame.quit()

def Update():
    ball.move()
    screan.blit(ball.image, ball.rect)

def Clamp(value, min, max):
    ret = value
    if value < min:
        ret = min
    elif value > max:
        ret = max
    return ret

size = widht, height = 600, 600


screan = pygame.display.set_mode(size)
screan.fill([255, 255, 255])

imgFile = "pict.png"
location = [10, 10]
speed = [2, 2]
ball = MyBallClass(imgFile, location, speed)


run_game()