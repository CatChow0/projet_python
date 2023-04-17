import pygame
import random


# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1280, 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Endless Scroll")

#load background image
background_size = (width, height)
background = pygame.image.load("bg1.png","bg2.png").convert()
background = pygame.transform.scale(background,background_size)
background_y=0

#Vitesse fond
scroll_speed= 2.5


# Set up the clock
clock = pygame.time.Clock()
FPS= 60

# Load the player sprite
player_size = (100,100)
player_image = pygame.image.load("player1.png").convert_alpha()
player_image = pygame.transform.scale(player_image,player_size)

# Load the enemy sprite
enemy_size = (80,80)
enemy_image = pygame.image.load("enemy.png").convert_alpha()
enemy_image = pygame.transform.scale(enemy_image,enemy_size)

# Set up the player
player_rect = player_image.get_rect()
player_rect.centerx = width // 2
player_rect.bottom = height - 50

# Set up the bullets
bullet_list = []
bullet_speed = 20


# Set up the enemies
enemy_list = []
enemy_speed = 5
enemy_spawn_rate = 60
enemy_spawn_counter = 0

score = 0
font = pygame.font.SysFont(None, 24)

# Main game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Fire a bullet
                bullet_rect = pygame.Rect(0, 0, 5, 5)
                bullet_rect.centerx = player_rect.centerx
                bullet_rect.bottom = player_rect.top
                bullet_list.append(bullet_rect)
    
    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.move_ip(-5, 0)
    if keys[pygame.K_RIGHT] and player_rect.right < width:
        player_rect.move_ip(5, 0)

    # Move the bullets
    for bullet_rect in bullet_list:
        bullet_rect.move_ip(0, -bullet_speed)

    # Move the enemies
    for enemy_rect in enemy_list:
        enemy_rect.move_ip(0, enemy_speed)

    # Spawn new enemies
    enemy_spawn_counter += 1
    if enemy_spawn_counter >= enemy_spawn_rate:
        enemy_rect = enemy_image.get_rect()
        enemy_rect.centerx = random.randint(0, width)
        enemy_rect.top = -enemy_rect.height
        enemy_list.append(enemy_rect)
        enemy_spawn_counter = 0

    # Detect collisions
    for bullet_rect in bullet_list:
        for enemy_rect in enemy_list:
            if bullet_rect.colliderect(enemy_rect):
                enemy_list.remove(enemy_rect)
                bullet_list.remove(bullet_rect)
                score += 1

    # Draw the screen
    screen.fill((0, 0, 0))
    background_y+=scroll_speed
    if background_y>background.get_height():
        background_y=0
    screen.blit(background, (0,background_y))
    screen.blit(background,(0,background_y-background.get_height()))
            
    
    screen.blit(player_image, player_rect)
    for bullet_rect in bullet_list:
        pygame.draw.rect(screen, (255, 255, 255), bullet_rect)
    for enemy_rect in enemy_list:
        screen.blit(enemy_image, enemy_rect)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    pygame.display.update()

    # Limit the frame rate
    clock.tick(FPS)

# Clean up
pygame.quit()