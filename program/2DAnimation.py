import pygame
import math

# инициализация Pygame
pygame.init()

# задание размера окна
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# задание цвета фона
bg_color = (255, 255, 255)

# задание параметров круга
circle_radius = 50
circle_color = (255, 0, 0)
circle_pos = (screen_width // 2, screen_height // 2)

# задание параметров анимации
fps = 60
clock = pygame.time.Clock()
angle = 0
speed = 2
radius = 200

# цикл анимации
while True:
    # обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # очистка экрана
    screen.fill(bg_color)

    # расчет новой позиции круга
    angle += speed
    x = circle_pos[0] + math.cos(math.radians(angle)) * radius
    y = circle_pos[1] + math.sin(math.radians(angle)) * radius

    # отрисовка круга
    pygame.draw.circle(screen, circle_color, (int(x), int(y)), circle_radius)

    # обновление экрана
    pygame.display.flip()

    # ограничение частоты кадров
    clock.tick(fps)
