import pygame
import random
RED = pygame.Color(255, 0, 0)
class Snake:
    def __init__(self):
        self.snake_x = random.randint(0,720)
        self.snake_y = 450
        self.x_change = 0
        self.y_change = 0
        self.size = 20
    def draw_snake(self, screen): 
        pygame.draw.rect(screen, RED, (self.snake_x, self.snake_y, self.size, self.size))
    def handle_key(self, key):       
            if key == pygame.K_LEFT:
                self.x_change = -5
                self.y_change = 0
            if key == pygame.K_RIGHT:
                self.x_change = 5
                self.y_change = 0
            if key == pygame.K_UP:
                self.y_change = -5
                self.x_change = 0
            if key == pygame.K_DOWN:
                self.y_change = 5
                self.x_change = 0
    def move(self):
        self.snake_x += self.x_change
        self.snake_y += self.y_change