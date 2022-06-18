import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption('runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50 )
game_active = True

forest_surface = pygame.image.load('resources/image/forest.jpg').convert()

score_monkey = test_font.render('my game', False,(64,64,64))
score_rect = score_monkey.get_rect(center = (400, 50))

bird_monkey= pygame.image.load('resources/image/bird.png')
bird_monkey.set_colorkey('BLACK')
bird_rect = bird_monkey.get_rect(topright = (600, 300))

player_monkey = pygame.image.load('resources/image/monkey.png')
player_rect = player_monkey.get_rect(midbottom= (80, 430))
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if player_rect.collidepoint(event.pos) and player_rect.bottom >= 410:
                player_gravity = -20
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.bottom >= 410:
                player_gravity = -20
            
        
    if game_active:   
        screen.blit(forest_surface,(0, 0))
        pygame.draw.rect(screen,'#c0e8ec',score_rect)
        pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        screen.blit(score_monkey,score_rect)

        bird_rect.x -= 4
        if bird_rect.right <= 0: bird_rect.left = 700
        screen.blit(bird_monkey,bird_rect)
        
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 410: player_rect.bottom = 410
        screen.blit(player_monkey, player_rect)
        
        
        if bird_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Yellow')
    
    pygame.display.update() 
    clock.tick(60)