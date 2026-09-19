import pygame
import random
RED = pygame.Color(255, 0, 0)
class Snake:
    
    def __init__(self):
        self.snake_x = random.randint(0,720)
        self.snake_y = 450
        self.size = 20
    def draw_snake(self, screen): 
        pygame.draw.rect(screen, RED, (self.snake_x, self.snake_y, self.size, self.size))