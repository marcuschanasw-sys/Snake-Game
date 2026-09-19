import pygame
from snake import Snake
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
black = pygame.Color(0, 0, 0)
clock = pygame.time.Clock()
pygame.display.set_caption("Snake Game")
snake = Snake()


pygame.init()
running = True
pausing = False
score = 0 
while running:
    screen.fill(black)
    snake.draw_snake(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)  
    pygame.display.update()
pygame.quit()