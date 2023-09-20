import pygame
from sys import exit


def display_score():
    current_time = int(pygame.time.get_ticks()  / 1000) - start_time
    score_surface = text_font.render(f'Score:{current_time}', False, (64, 64, 64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return current_time

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
text_font = pygame.font.Font('pygame tutorial/textfont/pixel.otf', 30)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('pygame tutorial/graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('pygame tutorial/graphics/Ground.png').convert_alpha()

enemy_surface = pygame.image.load('pygame tutorial/graphics/enemy/snail1.png').convert_alpha()
enemy_rect = enemy_surface.get_rect(bottomright = (600, 300))

player_surface = pygame.image.load('pygame tutorial/graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))
player_gravity = 0

game_name_surface = text_font.render('Pygame Tutorial', False, (111, 196, 169))
game_name_rect = game_name_surface.get_rect(center = (400, 60))

game_message_surface = text_font.render('Press Space to run', False, (111, 196, 169))
game_message_rect = game_message_surface.get_rect(midbottom = (400, 350))

#Intro screen
player_stand = pygame.image.load('pygame tutorial/graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400, 200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                        player_gravity = -20

            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                        player_gravity = -20
        else:
             if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                enemy_rect.left = 800
                game_active = True
                start_time = int(pygame.time.get_ticks()/1000)

    if game_active:

        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))

        score = display_score()

        enemy_rect.x -= 5
        if enemy_rect.right < 0:
            enemy_rect.left = 800
        screen.blit(enemy_surface, enemy_rect)


        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surface, player_rect)

        #collisions
        if enemy_rect.colliderect(player_rect):
            game_active = False

    else:
         screen.fill((94, 129, 192))
         screen.blit(player_stand, player_stand_rect)

         score_message_surface = text_font.render(f'Your score:{score}', False, (111, 196, 169))
         score_message_rect = score_message_surface.get_rect(center = (400, 330))
         screen.blit(game_name_surface, game_name_rect)

         if score == 0:
            screen.blit(game_message_surface, game_message_rect)
         else:
             screen.blit(score_message_surface, score_message_rect)


    pygame.display.update()
    clock.tick(60)