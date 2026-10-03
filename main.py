import pygame
from snake import Snake 
from apple import Apple
pygame.init()
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
black = pygame.Color(0, 0, 0)
clock = pygame.time.Clock()
pygame.display.set_caption("Snake Game")
snake = Snake()
apple = Apple()
running = True
pausing = False
score = 0 
font = pygame.font.Font("freesansbold.ttf", 30)  
def gameover(): 
    global font
    gameover_text = font.render("You lose!", True,  (255, 255, 255))
    screen.blit(gameover_text, (280, 220))
def show_score():
    score_text = font.render("Score:" + str(score), True,  (255, 255, 255))
    screen.blit(score_text, (10, 10))
while running:
    screen.fill(black)
    snake.draw_snake(screen)
    apple.draw_apple(screen)
    if snake.hit_wall(): 
        gameover()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
             snake.handle_key(event.key)
    snake.move()
    clock.tick(60)  
    pygame.display.update()
pygame.quit()


