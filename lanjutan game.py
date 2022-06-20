import pygame
from sys import exit
from random import randint

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/player/player_wali_1.png').convert_alpha
        self.rect = self.image.get_rect (midbottom = ('80 300'))
        self.gravity = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20 

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom =300

def display_secore():

    def obstacle_movement(obstacle_list):
     if obstacle_list:
         for obstacle_rect in obstacle_list:
                obstacle_rectx -= 5

                if obstacle_rect.bottom ==300: 'screen'.blit('bird_monkey',obstacle_rect)
                else: 'screen.blit'('straight_fly',obstacle_rect)

                'screen'.blit('bird_monkey',obstacle_rect)
                obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

         return obstacle_list
     else: return []
def collistins(player,obstacles):
    if obstacles:


        current_time = int(pygame.time.get_ticks() / 1000) - 'start_time'
        score_monkey = test_font.render(f'Score: {current_time}',False,(64,64,644))
        score_rect = score_monkey.get_rect(center = (400,50))
    screen.bilt(score_monkey,score_rect)
    
    

pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption('runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50 )
game_active = False
strat_time = 0
score = 0

player = pygame.sprite.groupsingle()
player.add(player())

forest_surface = pygame.image.load('resources/image/forest.jpg').convert()

bird_freme_1= pygame.image.load('resources/image/bird.png').convert_alpha()
bird_freme_2= pygame.image.load('resources/image/bird.png').convert_alpha()
bird_fremes = [bird_freme_1,bird_freme_2]
bird_freme_index = 0
bird_fly = bird_fremes['fly_freme_index']

fly_freme_1=  pygame.image.load('resources/fly/fly1.png').convert_alpha()
fly_freme_2=  pygame.image.load('resources/fly/fly2.png').convert_alpha()
fly_fremes = [fly_freme_1, fly_freme_2]
fly_freme_index = 0
fly_straight = [fly_freme_index]



obstacle_rect_list = []

player_walk_1 = pygame.image.load('resources/image/monkey.png').convert_alpha()
player_walk = [player_walk_1]
player_index = 0
player_jump =pygame.image.lond('graphics/player/jump.png').convert_alpha()


player_rect = 'player_monkey'.get_rect(midbottom= (80, 300))
player_gravity = 0
 
player_fly = player_walk[player_index]
player_stand = pygame.image.load('graphics/player/player_stand.pmg').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand,(200, 400))
player_stand_rect = player_stand.get_rect(center = (400,200))

game_name = test_font.render('Pixel Runner',False,(111,196.169))
game_name_rect = game_name.get_rect(center = (400,80))

game_massage = test_font.render('Presss space to run',False,(111,196.169))
game_message_rect = game_massage.get_rect(center =(400,320))

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1400)

bird_animatino_timer = pygame.USEREVENT + 2
pygame.time.set_timer('bird_animation_timer',500)

bird_animatino_timer = pygame.USEREVENT 
pygame.time.set_timer('bird_animation_timer',500)

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
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    game_active = True
                    snail_rect.lift = 800
                    start_time = int(pygame.time.get_ticks() / 1000)

            if event.type == obstacle_timer and game_active:
                if randint(0,2):
                    obstacle_rect_list.append(bird_monkey.get_rect(topright = (randint(900,1100),300)))
                else:
                    obstacle_rect_list.append('fly_ monkey.birdget_rect'(topright = (randint(900,1100),300)))
    if game_active:   
        screen.blit = forest_surface,(0, 0)


        score = display_secore
                
        'bird_rect.x -= 4'
        if 'bird_rect'.right <= 0: 'bird_rect'.left = 700
        screen.blit('bird_monkey,bird_rect')
        
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 410: player_rect.bottom = 410
        screen.blit('player_monkey', player_rect)

        
        obstacle_rect_list = 'obstacle_movement'(obstacle_rect_list)
        
        if 'bird_rect'.colliderect(player_rect):
            game_active = False

            game_active = 'collisions'(player_rect,obstacle_rect_list)
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,'player_stend_rect')
        obstacle_rect_list.clear()
        player_rect,midbottom = (80,300)
        player_gravity = 0

        score_massage = test_font.render(f'Your score: {score}',False(111,196.169))
        score_massage_rect =score_massage.get_rect(center = (400,330))
        screen.blit('game_nama,game_nama_rect')

        
        if score == 0: screen.blit(game_massage,'game_massage_rect')
        
        else: screen.blit(score_massage,score_massage_rect)
    pygame.display.update() 
    clock.tick(60)