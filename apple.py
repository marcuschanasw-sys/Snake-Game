import pygame
import random
GREEN = pygame.Color(0, 255, 0)
class Apple:
    def __init__(self):
        self.size = 20
        self.apple_x = random.randrange(0,700,20)
        self.apple_y = random.randrange(0,460,20)
    def draw_apple(self, screen): 
        pygame.draw.rect(screen, GREEN, (self.apple_x, self.apple_y, self.size, self.size))