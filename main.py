import pygame
import random

from classes import enemy,projectile,displayable

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

backround_image = pygame.image.load("background1.png").convert()
backround_rect = backround_image.get_rect()
backround_rect.left = width + 50
backround_rect.bottom = height - 1

# Set up the clock
clock = pygame.time.Clock()

# Load the player sprite
player_image = pygame.image.load("player.png").convert_alpha()
player_image = pygame.transform.scale(player_image,(75,75))

# Load Enemies
enemy_vert = enemy("enemy",40,1,5)

# Load missile
player_missile = projectile("player_missile_sprite",50,10,5)

# Explosion frames
missile_exlposion = displayable("tile003",100)
explo_size = missile_exlposion.image.get_size()

# Set up the player
player_rect = player_image.get_rect()
player_rect.centerx = width // 2
player_rect.bottom = height - 10
player_pv = 20

# Set up the bullets
bullet_list = []

# Set up the enemies
enemy_list = []
enemy_spawn_rate = 60
enemy_spawn_counter = 0


# Set up the score
score = 0
font = pygame.font.SysFont(None, 24)

# Main game loop
running = True
while running:
    
    screen.fill((0, 0, 0))
    screen.blit(backround_image, backround_rect)
    screen.blit(player_image, player_rect)
    for bullet_rect in bullet_list:
        screen.blit(player_missile.image,bullet_rect)
    for enemy_rect in enemy_list:
        screen.blit(enemy_vert.image, enemy_rect)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (450, 10))
    pv_text = font.render("Pv: " + str(player_pv), True, (255,255,255))
    screen.blit(pv_text, (10,10))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Fire a bullet
                bullet_rect = player_missile.image.get_rect()
                bullet_rect.centerx = player_rect.centerx
                bullet_rect.bottom = player_rect.top
                bullet_list.append(bullet_rect)

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.move_ip(-10, 0)
    if keys[pygame.K_RIGHT] and player_rect.right < width:
        player_rect.move_ip(10, 0)
    if keys[pygame.K_UP] and player_rect.left > 0:
        player_rect.move_ip(-10, 0)
    if keys[pygame.K_DOWN] and player_rect.right < width:
        player_rect.move_ip(10, 0)


    # Move the bullets
    for bullet_rect in bullet_list:
        bullet_rect.move_ip(0, -player_missile.speed)

    # Move the enemies
    for enemy_rect in enemy_list:
        enemy_rect.move_ip(0, enemy_vert.speed)

    # Spawn new enemies
    enemy_spawn_counter += 1
    if enemy_spawn_counter >= enemy_spawn_rate:
        enemy_rect = enemy_vert.image.get_rect()
        enemy_rect.centerx = random.randint(0, width)
        enemy_rect.top = -enemy_rect.height
        enemy_list.append(enemy_rect)
        enemy_spawn_counter = 0

    # Detect collisions bullet
    for bullet_rect in bullet_list:
        for enemy_rect in enemy_list:
            if bullet_rect.colliderect(enemy_rect) :
                temp_enemy_rect = (enemy_rect[0] - explo_size[0]/4, enemy_rect[1] - explo_size[1]/4,enemy_rect[2],enemy_rect[3])
                screen.blit(missile_exlposion.image,temp_enemy_rect)
                enemy_list.remove(enemy_rect)
                bullet_list.remove(bullet_rect)
                score += 1
    
    
    # Detect collisions player
    for enemy_rect in enemy_list:
        if player_rect.colliderect(enemy_rect):
            enemy_list.remove(enemy_rect)
            player_pv -= 5
    
    if player_pv <= 0 :
        running = False
        
    # Draw the screen
    pygame.display.flip()


    # Limit the frame rate
    clock.tick(60)

# Clean up
pygame.quit()