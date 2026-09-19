import pygame
import random
RED = pygame.Color(255, 0, 0)
class Snake:
    def __init__(self):
        self.apple_x = random.randrange(0,700,20)
        self.apple_y = random.randrange(0,460,20)