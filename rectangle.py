import pygame 

pygame.init()

screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

text = pygame.font.Font(r"C:\Users\hp\Downloads\Inkfree.ttf",50)  # creating a font 


test_s = pygame.image.load(r"C:\Users\hp\Downloads\nebula_1.png").convert()   # import an back_ground image on the screen


text_s = text.render("First game",True,"black")    # import the text that created

alien = pygame.image.load(r"C:\Users\hp\Downloads\alien_1.png").convert_alpha()  # convert the image to python can
alien_r = alien.get_rect(bottomright = (600,300))                                                                                # easily work with
                                                           

player_s = pygame.image.load(r"C:\Users\hp\Downloads\astronaut_1.png")  # player image cration
player_r = player_s.get_rect(midbottom=(80,310))                           # player rectangle creation
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(test_s,(0,0))    # show the image on the screen 
    screen.blit(text_s,(300,50))
    
    alien_r.left -= 4
    if alien_r.right < 0 : alien_r.left = 800 

    screen.blit(alien,alien_r)
    screen.blit(player_s,player_r)          # player rectengle render on the screen 
    pygame.display.update()
    clock.tick(60)