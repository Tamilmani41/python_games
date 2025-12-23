# this score.py also has the transforming surfaces in it... 
import pygame # this timer.py also contains player animation

from random import randint

def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_s = text.render(f'score :{current_time}',False,("black"))    # score updating
    score_r = score_s.get_rect(center = (400,50))       # score positioning 
    screen.blit(score_s,score_r)
    return current_time

def obstecle_movement(obstecle_list):
    if obstecle_list:
        for obstecle_rect in obstecle_list:
            obstecle_rect.x -= 5

            if obstecle_rect.bottom == 300: screen.blit(alien,obstecle_rect)
            else : screen.blit(ship,obstecle_rect)
            
        obstecle_list = [obstecle for obstecle in obstecle_list if obstecle.x > -100]    #"this list comprihension copies the existing list if it is not 
        return obstecle_list                                                             # greater than -100 if it's greatter than -100 it dosen't copies it " ->
    else:return []                                                                       # that means the obstecle will be deleted ...

def player_animation():
    # player jump + walking animation
    global player_s,player_index
    if player_r.bottom < 300:
        player_s = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_float): player_index = 0
        player_s = player_float[int(player_index)]
        
def collisions(player,obstecles):
    if obstecles:
        for obstecle_rect in obstecles:
            if player.colliderect(obstecle_rect): return False
    return True  

pygame.init()
#                                  x   y
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

text = pygame.font.Font(r"C:\Users\hp\Downloads\Inkfree.ttf",50)  # creating a font 

test_s = pygame.image.load(r"C:\Users\hp\Downloads\nebula_1.png").convert()   # import an back_ground image on the screen

# text_s = text.render("First game",True,"black")    # import the text that created
# obstecle 
alien_frame_1 = pygame.image.load(r"C:\python\game assets\alien_1.png").convert_alpha()  # convert the image to python can
alien_frame_2 = pygame.image.load(r"C:\python\game assets\alien_2.png").convert_alpha()
alien_frames = [alien_frame_1,alien_frame_2]
alien_frame_index = 0 
alien = alien_frames[alien_frame_index]
alien_r = alien.get_rect(bottomright = (600,300))                                                    # easily work with

ship_frame_1 = pygame.image.load(r"C:\python\game assets\ship_1.png").convert_alpha()
ship_frame_2 = pygame.image.load(r"C:\python\game assets\ship_2.png").convert_alpha()
ship_frame = [ship_frame_1,ship_frame_2]
ship_frame_index = 0 
ship = ship_frame[ship_frame_index]

obstecle_rect_list = []

# player                                                     
player_float_1 = pygame.image.load(r"C:\python\game assets\astronaut_1.png").convert_alpha()  # player image cration
player_float_2 = pygame.image.load(r"C:\python\game assets\astronaut_2.png").convert_alpha()
player_float_3 = pygame.image.load(r"C:\python\game assets\astronaut_3.png").convert_alpha()
player_float_4 = pygame.image.load(r"C:\python\game assets\astronaut_2.png").convert_alpha()
player_float = [player_float_1,player_float_2,player_float_3,player_float_4]
player_index = 0
player_jump = pygame.image.load(r"C:\python\game assets\astronaut_2.png").convert_alpha()

player_s = player_float[player_index]
player_r = player_s.get_rect(midbottom=(80,310))                          # player rectangle creation
# player stand on the over screen
# background palyer stand 
player_stand = pygame.image.load(r"C:\Users\hp\Downloads\astronaut_1.png").convert_alpha()
# player_stand = pygame.transform.scale(player_stand,(200,400))       # transforming surfaces 
# player_stand = pygame.transform.scale2x(player_stand) 
player_stand = pygame.transform.rotozoom(player_stand,0,2) 
player_stand_r = player_stand.get_rect(midbottom=(400,200)) 

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
# Timer 
obstecle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstecle_timer,1500)

# obstecle timer 
alien_animation_timer  = pygame.USEREVENT + 2
pygame.time.set_timer(alien_animation_timer,500)

ship_animation_timer  = pygame.USEREVENT + 3
pygame.time.set_timer(ship_animation_timer,200)

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active :
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
        if game_active:
            if event.type == obstecle_timer :
                if randint(0,2):
                    obstecle_rect_list.append (alien.get_rect(bottomright = (randint(900,1100),300)))
                else:
                    obstecle_rect_list.append (ship.get_rect(bottomright = (randint(900,1100),200)))

            if event.type == alien_animation_timer :
                if alien_frame_index == 0 : alien_frame_index = 1
                else: alien_frame_index = 0
                alien = alien_frames[alien_frame_index]

            if event.type == ship_animation_timer:
                if ship_frame_index == 0 : ship_frame_index = 1
                else: ship_frame_index = 0
                ship = ship_frame[ship_frame_index]
        

    if game_active :
        screen.blit(test_s,(0,0))    # show the image on the screen 
        # screen.blit(text_s,(300,50))    # show teext on the screen 
        score = display_score()
        
        # alien_r.left -= 4
        # if alien_r.right < 0 : alien_r.left = 800             get rid of the alien rect cause we are applying new obstcle logic
            
        # screen.blit(alien,alien_r)
        
        # gravity apply to the player     
        player_gravity += 1
        # another different method to apply gravity it's more realistic 
        player_r.y += player_gravity
        # if player_r : player_r.y += 1       # gravity applied

        # create a ground 
        if player_r.bottom >= 300 : player_r.bottom = 300
        player_animation()
        screen.blit(player_s,player_r)          # player rectengle render on the screen
        
        # player collide with alien
        # if alien_r.colliderect(player_r):
        #     game_active = False
        
        # obstecle 
        obstecle_rect_list = obstecle_movement(obstecle_rect_list)
        game_active = collisions(player_r,obstecle_rect_list) 
    
    else :
        screen.blit(back_ground_oc,(0,0))
        screen.blit(player_stand,player_stand_r)
        obstecle_rect_list.clear()
        player_r.midbottom = (80,300)
        player_gravity = 0

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