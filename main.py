import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

# Set up the background
bg = pygame.image.load("background1.png").convert_alpha()
bg = pygame.transform.scale(bg, (width,height))

# Set up the clock
clock = pygame.time.Clock()

# Load the player sprite
player_image = pygame.image.load("player.png").convert_alpha()

# Load the enemy sprite
enemy_image = pygame.image.load("enemy.png").convert_alpha()

# Load Beam sprite
beam_image = pygame.image.load("beam.png").convert_alpha()

# Set up the player
player_size = (75,75)
player_image = pygame.transform.scale(player_image,player_size)
player_rect = player_image.get_rect()
player_rect.centerx = width // 2
player_rect.bottom = height - 10
player_pv = 20
player_speed = 7

# Set up the bullets
bullet_list = []
bullet_speed = 10

# Set up the q skill
beam_size =(32,800)
beam_image = pygame.transform.scale(beam_image, beam_size)
skill_bullet_list = []
skill_bullet_speed = 20
q_cooldown = 0

# Set up the enemies
enemy_size = (40,40)
enemy_image = pygame.transform.scale(enemy_image, enemy_size)
enemy_list = []
enemy_speed = 5
enemy_spawn_rate = 60
enemy_spawn_counter = 0

# Set up the score
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
                bullet_rect = pygame.Rect(0, 0, 8, 20)
                bullet_rect.centerx = player_rect.centerx
                bullet_rect.bottom = player_rect.top
                bullet_list.append(bullet_rect)
                # Fire skill bullet
            if event.key == pygame.K_q:
                if q_cooldown == 0:
                    skill_bullet_rect = beam_image.get_rect()
                    skill_bullet_rect.centerx = player_rect.centerx
                    skill_bullet_rect.bottom = player_rect.top
                    skill_bullet_list.append(skill_bullet_rect)
                    q_cooldown = 600

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.move_ip(-player_speed, 0)
    if keys[pygame.K_RIGHT] and player_rect.right < width:
        player_rect.move_ip(player_speed, 0)
    if keys[pygame.K_UP] and player_rect.left > 0:
        player_rect.move_ip(-player_speed, 0)
    if keys[pygame.K_DOWN] and player_rect.right < width:
        player_rect.move_ip(player_speed, 0)

    # Move the bullets
    for bullet_rect in bullet_list:
        bullet_rect.move_ip(0, -bullet_speed)
    
    # Move the bullets skills
    for skill_bullet_rect in skill_bullet_list:
        skill_bullet_rect.move_ip(0, -skill_bullet_speed)

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

    # Detect collisions bullet
    for bullet_rect in bullet_list:
        for enemy_rect in enemy_list:
            if bullet_rect.colliderect(enemy_rect):
                enemy_list.remove(enemy_rect)
                bullet_list.remove(bullet_rect)
                score += 1
                
    # Detect collisions skills bullet
    for skill_bullet_rect in skill_bullet_list:
        for enemy_rect in enemy_list:
            if skill_bullet_rect.colliderect(enemy_rect):
                enemy_list.remove(enemy_rect)
                score += 1

    # Detect collisions player
    for enemy_rect in enemy_list:
        if player_rect.colliderect(enemy_rect):
            enemy_list.remove(enemy_rect)
            player_pv -= 5
            
    # Draw the screen
    screen.fill((0, 0, 0))
    screen.blit(bg,(0,0))
    screen.blit(player_image, player_rect)
    # Draw bullet
    for bullet_rect in bullet_list:
        pygame.draw.rect(screen, (255, 255, 255), bullet_rect)
    for skill_bullet_rect in skill_bullet_list:
        screen.blit(beam_image, skill_bullet_rect)
    # Render enemy
    for enemy_rect in enemy_list:
        screen.blit(enemy_image, enemy_rect)
    # Draw score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(width/2,20))
    screen.blit(score_text, score_rect)
    # Draw life
    pv_text = font.render("Pv: " + str(player_pv), True, (255,255,255))
    screen.blit(pv_text, (10,10))
    # Drow cooldown
    if q_cooldown > 0:
        q_cooldown_rt = round(q_cooldown/60)
        q_skill_text = font.render("Laser dans: " + str(q_cooldown_rt) + "s", True, (255,0,0))
        q_skill_rect = q_skill_text.get_rect(center=(70,height-20))
        screen.blit(q_skill_text, q_skill_rect)
        q_cooldown -= 1
    elif q_cooldown == 0:
        q_skill_text = font.render("Laser: q", True, (0,255,0))
        q_skill_rect = q_skill_text.get_rect(center=(70,height-20))
        screen.blit(q_skill_text, q_skill_rect)
        
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
    
# Clean up
pygame.quit()

