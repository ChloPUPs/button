import pygame
from pygame import mixer
running = True

width = 800
height = 600

pygame.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CLICK IT")

font = pygame.font.Font("freesansbold.ttf", 64)

# button size = 400x 100y
buttonImg = pygame.image.load("button.png")

def text():
    v_text = font.render("Press button?", True, (255, 255, 255))
    screen.blit(v_text, (180, 100))

def button(x, y):
    screen.blit(buttonImg, (x, y))

while running:
    screen.fill((255, 0, 0))

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse[0] >= 200 and mouse[0] <= 600 + 1 and mouse[1] >= 200 and mouse[1] <= 301:
                a_sound = mixer.Sound("metal_pipe.mp3")
                a_sound.play()
    if mouse[0] >= 200 and mouse[0] <= 600 + 1 and mouse[1] >= 200 and mouse[1] <= 301:
        buttonImg = pygame.image.load("buttonhl.png")
    else:
        buttonImg = pygame.image.load("button.png")



    text()
    button(200, 200)
    pygame.display.update()