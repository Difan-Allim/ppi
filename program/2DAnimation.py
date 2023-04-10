import pygame

pygame.init()

# создание окна
screen = pygame.display.set_mode((800, 600))

# загрузка изображения
ball_image = pygame.image.load('ball.png')

# начальное положение шара
x = 0
y = 0

# скорость перемещения шара
dx = 5
dy = 5

# основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # перемещение шара
    x += dx
    y += dy

    # отражение шара при касании края экрана
    if x < 0 or x > 800 - ball_image.get_width():
        dx = -dx
    if y < 0 or y > 600 - ball_image.get_height():
        dy = -dy

    # отрисовка шара
    screen.blit(ball_image, (x, y))

    # обновление экрана
    pygame.display.update()
