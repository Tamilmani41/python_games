import pygame
                    # importing and initilizing pygame
pygame.init()
    # initilizing the screen and frame rate 
pygame.display.set_caption("One step further")  # window title
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

# while loop for hold the window 
while True:
    # for loop for quit the game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() # function for (pygame.error: video system not initialized) error
    # updates the screen 
    pygame.display.update()
    clock.tick(60) # frame rate initilizing