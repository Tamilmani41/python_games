import pygame 

pygame.init()

screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
# test_s = pygame.Surface((100,200))  # inserting a plain color 
# test_s.fill("red")
text = pygame.font.Font(r"C:\Users\hp\Downloads\Inkfree.ttf",50)  # creating a font 


test_s = pygame.image.load(r"C:\Users\hp\Downloads\nebula_1.png").convert()   # import an image on the screen


text_s = text.render("First game",True,"black")    # import the text that created

alien = pygame.image.load(r"C:\Users\hp\Downloads\alien_1.png").convert_alpha()  # convert the image to python can
alien_x_pos = 600                                                                 # easily work with
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(test_s,(0,0))    # show the image on the screen 
    screen.blit(text_s,(300,50))
    alien_x_pos -= 3
    if alien_x_pos < -100: alien_x_pos = 800
    
    screen.blit(alien,(alien_x_pos,250))
    pygame.display.update()
    clock.tick(60)
