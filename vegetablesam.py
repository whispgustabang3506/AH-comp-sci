import pygame
pygame.init() # initiliazes pygame 

win = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("fruit ninja ")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    pygame.display.update() 

 
