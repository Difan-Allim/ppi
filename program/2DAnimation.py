import pygame

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2D Animation")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define a sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Create a sprite group
all_sprites = pygame.sprite.Group()

# Create a sprite object
player = Sprite(RED, 0, 0, 50, 50)

# Add the sprite object to the sprite group
all_sprites.add(player)

# Set up the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprites
    all_sprites.update()

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
