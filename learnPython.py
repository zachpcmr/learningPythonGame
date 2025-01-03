import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks()/1000)-start_time
    score_surface = test_font.render(str(current_time),False,(64,64,64))
    score_rect = score_surface.get_rect(center = (400,50))
    screen.blit(score_surface,score_rect)
    return current_time

def player_animation():
    #play walking, play jumping
    global player_surface, player_index
    if player_rect.bottom<300:
        player_surface = player_jump
    else:
        player_index+=.1
        if player_index >=len(player_walk): player_index = 0
        player_surface = player_walk[int(player_index)]


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
#controlls framerate
clock = pygame.time.Clock()
#font type, size
player_gravity = 0
start_time = 0
score = 0
player_index = 0
test_font = pygame.font.Font('Documents/python/Python_game/font/Pixeltype.ttf',50)

sky_surface = pygame.image.load('Documents/python/Python_game/graphics/Sky.png').convert()
ground_surface = pygame.image.load('Documents/python/Python_game/graphics/ground.png').convert()
game_over_text = test_font.render('Dodge the snails by jumping over them!',False,(64,64,64))
game_over_text2 = test_font.render('Press space to start!',False,(64,64,64))

                                 #text info,anti-alias,color
#score_surface = test_font.render('My game',False, 'white')
snail_surface = pygame.image.load('Documents/python/Python_game/graphics/snail1.png').convert_alpha()
player_walk_1 = pygame.image.load('Documents/python/Python_game/graphics/player_walk_1.png').convert_alpha()
player_walk_2 = pygame.image.load('Documents/python/Python_game/graphics/player_walk_2.png').convert_alpha()
player_walk = [player_walk_1,player_walk_2]
player_jump = pygame.image.load('Documents/python/Python_game/graphics/player_jump.png').convert_alpha()

player_surface = player_walk[player_index]
game_active = False
#making things rectangles for hitboxes and easy manipulation
player_stand = pygame.image.load('Documents/python/Python_game/graphics/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400,200))
player_rect = player_walk_1.get_rect(midbottom = (80,300))
snail_rect = snail_surface.get_rect(midbottom = (720,300))
game_over_rect = game_over_text.get_rect(center = (400,50))
game_over_rect2 = game_over_text.get_rect(center = (520,360))

#Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)
#score_rect = score_surface.get_rect(center = (400,50))

while True:
    key = pygame.key.get_pressed()
    player_animation()
    #if the key pressed is a, move to the right
    if game_active:
        if key[pygame.K_a] == True:
            player_rect.move_ip(-3,0)
        elif key[pygame.K_d] == True:
            player_rect.move_ip(3,0)
        elif key[pygame.K_SPACE] == True and player_rect.bottom==300:
            #player_animation()
            player_gravity = -15
        elif key[pygame.K_s] == True:
            player_rect.move_ip(0,3)

    else:
        if key[pygame.K_SPACE] == True:
            game_active = True
            snail_rect = snail_surface.get_rect(midbottom = (720,300))
            player_rect = player_walk_1.get_rect(midbottom = (80,300))
            print('its rewind time')
            start_time = int(pygame.time.get_ticks()/1000)-start_time



    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            pygame.quit()
            exit()



#remember when making these surfaces make a rectangle for them and move that instead. Makes way more sense.
   
    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
#        pygame.draw.rect(screen,'#c0e8ec',score_rect)
 #       pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
  #      screen.blit(score_surface,score_rect)
        score = display_score()

        snail_rect.left -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surface,snail_rect)

        player_gravity += 1
        player_rect.bottom+=player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface,player_rect)


        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('maroon')

        screen.blit(player_stand,player_stand_rect)
        screen.blit(game_over_text,game_over_rect)
        score_message = test_font.render(f'your score: {score}',False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400,330))

        if score == 0:
            screen.blit(game_over_text2,game_over_rect2)
        else:
            screen.blit(score_message,score_message_rect)

    pygame.display.update()
    #stop the loop from running too quickly, giving us 60 frames
    clock.tick(60)



