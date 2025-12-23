# this score.py also has the transforming surfaces in it... 
import pygame 

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_s = text.render(f'score :{current_time}',False,("black"))    # score updating
    score_r = score_s.get_rect(center = (400,50))       # score positioning 
    screen.blit(score_s,score_r)
    return current_time

pygame.init()
#                                  x   y
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

text = pygame.font.Font(r"C:\Users\hp\Downloads\Inkfree.ttf",50)  # creating a font 

test_s = pygame.image.load(r"C:\Users\hp\Downloads\nebula_1.png").convert()   # import an back_ground image on the screen

# text_s = text.render("First game",True,"black")    # import the text that created

alien = pygame.image.load(r"C:\Users\hp\Downloads\alien_1.png").convert_alpha()  # convert the image to python can
alien_r = alien.get_rect(bottomright = (600,300))                                                    # easily work with
                                                           
player_s = pygame.image.load(r"C:\Users\hp\Downloads\astronaut_1.png")  # player image cration
player_r = player_s.get_rect(midbottom=(80,310))                           # player rectangle creation

# player stand on the over screen
player_stand = pygame.image.load(r"C:\Users\hp\Downloads\astronaut_1.png").convert_alpha()
# player_stand = pygame.transform.scale(player_stand,(200,400))       # transforming surfaces 
# player_stand = pygame.transform.scale2x(player_stand) 
player_stand = pygame.transform.rotozoom(player_stand,0,2) 
player_stand_r = player_s.get_rect(midbottom=(400,200)) 

# back ground image for over screen 
back_ground_oc = pygame.image.load(r"C:\Users\hp\Downloads\planet_1.png").convert()

game_active = False
start_time = 0
# gravity implementation , insted of 0 ,we can use negative values to make player go upwards and downwards 
# kinda like jumping 
player_gravity = 0
# player_gravity = -20    # player make a jump 

# adding instructions 
text_s = text.render("My first game",True,"black")      # game name
text_os = pygame.font.Font(r"C:\Users\hp\Downloads\Inkfree.ttf",30)     # text creation
text_s_instruct = text_os.render("press \"space\" to start the game :)",True,'#fbfb00')     # game start instruction

score = 0

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
             # if event.type == pygame.MOUSEBUTTONDOWN:
            if event.type == pygame.MOUSEBUTTONDOWN :
                # if player_r.bottom == 300:         another way                    # check mouse button down
                if player_r.collidepoint(event.pos) and player_r.bottom == 300:    # check collision of player & mouse arrow
                    player_gravity = -20                                            # jump if collieded

            if event.type == pygame.KEYDOWN:
                # if player_r.bottom == 300:        another way                # we aren't going to apply the gravity there insted we need
                if event.key == pygame.K_SPACE and player_r.bottom == 300:     # our player to jump while the keys is pressed 
                    player_gravity = -20                                        # using the gravity over here
                                    
        else: 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    alien_r.bottomright = (600,300)
                    game_active = True
                    start_time = int(pygame.time.get_ticks() /1000)

    if game_active :
        screen.blit(test_s,(0,0))    # show the image on the screen 
        # screen.blit(text_s,(300,50))    # show teext on the screen 
        score = display_score()
        
        alien_r.left -= 4
        if alien_r.right < 0 : alien_r.left = 800 
            
        screen.blit(alien,alien_r)
        
        # gravity apply to the player     
        player_gravity += 1
        # another different method to apply gravity it's more realistic 
        player_r.y += player_gravity
        # if player_r : player_r.y += 1       # gravity applied

        # create a ground 
        if player_r.bottom >= 300 : player_r.bottom = 300
        screen.blit(player_s,player_r)          # player rectengle render on the screen
        
        # player collide with alien
        if alien_r.colliderect(player_r):
            game_active = False
    
    else :
        screen.blit(back_ground_oc,(0,0))
        screen.blit(player_stand,player_stand_r)
        if game_active == False and score == 0:
            screen.blit(text_s,(250,20))
            screen.blit(text_s_instruct,(200,350))
        else:
            score_achived_s = text_os.render(f"scored :{score}",True,"#000000") 
            screen.blit(score_achived_s,(290,100))
            screen.blit(text_s,(250,20))
            screen.blit(text_s_instruct,(200,350))
    pygame.display.update()
    clock.tick(60)