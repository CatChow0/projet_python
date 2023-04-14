import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))

# Set up the background
bg = pygame.image.load("assets/background.png").convert()
bg = pygame.transform.scale(bg, (width,height))

# Set up the clock
clock = pygame.time.Clock()

# Load the player sprite
player_image = pygame.image.load("assets/player.png").convert_alpha()

# Load the enemy sprite
enemy_image = pygame.image.load("assets/enemy.png").convert_alpha()
enemy_alt_image = pygame.image.load("assets/enemy_alt.png").convert_alpha()

# Load Beam sprite
beam_image = pygame.image.load("assets/beam.png").convert_alpha()

# Load the life bar sprite
life_bar_image = pygame.image.load("assets/LifeBarFull.png").convert_alpha()
life_bar_image1hit = pygame.image.load("assets/LifeBar1hit.png").convert_alpha()
life_bar_image2hit = pygame.image.load("assets/LifeBar2hit.png").convert_alpha()
life_bar_image3hit = pygame.image.load("assets/LifeBar3hit.png").convert_alpha()
life_bar_image4hit = pygame.image.load("assets/LifeBar4hit.png").convert_alpha()
life_bar_imageDead = pygame.image.load("assets/LifeBarDead.png").convert_alpha()
life_bar_imageShield = pygame.image.load("assets/LifeBarShield.png").convert_alpha()
life_bar_imageFull = life_bar_image

# Load the bonus sprite
life_bonus_image = pygame.image.load("assets/LifeBonus.png").convert_alpha()
rocket_bonus_image = pygame.image.load("assets/RocketBonus.png").convert_alpha()

# Set up the background
bg_y = 0
scroll_speed = 3

# Set up the life bar
life_bar_size = (200,75)
life_bar_image = pygame.transform.scale(life_bar_image,life_bar_size)
life_bar_rect = life_bar_image.get_rect()
life_bar_rect.left = 10
life_bar_rect.top = 10
player_pv = 25

# Set up the player
player_size = (75,75)
player_image = pygame.transform.scale(player_image,player_size)
player_rect = player_image.get_rect()
player_rect.centerx = width // 2
player_rect.bottom = height - 10
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

# Set up the normal enemies
enemy_size = (40,40)
enemy_image = pygame.transform.scale(enemy_image, enemy_size)
enemy_list = []
enemy_speed = 5
enemy_spawn_rate = 60
enemy_spawn_counter = 60

# Set up the normal enemies alternate
enemy_alt_size = (80,80)
enemy_alt_image = pygame.transform.scale(enemy_alt_image, enemy_alt_size)
enemy_alt_list = []
enemy_alt_speed = 1
enemy_alt_spawn_rate = 300
enemy_alt_spawn_counter = 300

# Set up the life bonus
life_bonus_size = (40,40)
life_bonus_image = pygame.transform.scale(life_bonus_image, life_bonus_size)
life_bonus_list = []
life_bonus_speed = 5
life_bonus_spawn_rate = random.randint(600,1200)
life_bonus_spawn_counter = 0

# Set up the Rocket Bonus
rocket_bonus_size = (40,40)
rocket_bonus_image = pygame.transform.scale(rocket_bonus_image, rocket_bonus_size)
rocket_bonus_list = []
rocket_bonus_speed = 5
rocket_bonus_spawn_rate = random.randint(10,60)
rocket_bonus_spawn_counter = 0

# Set up the score
best_score = 0
score = 0
font = pygame.font.SysFont(None, 24)

def update_life_bar(x):
    x = pygame.transform.scale(x,life_bar_size)
    screen.blit(x, life_bar_rect)
    
def truc(mob_rect,mob_list):
    # Detect collisions bullet
    for bullet_rect in bullet_list:
        for mob_rect in mob_list:
            if bullet_rect.colliderect(mob_rect):
                mob_list.remove(mob_rect)
                bullet_list.remove(bullet_rect)
                if mob_rect == enemy_alt_rect:
                    return int(3)
                else:
                    return int(1)
                
    # Detect collisions skills bullet
    for skill_bullet_rect in skill_bullet_list:
        for mob_rect in mob_list:
            if skill_bullet_rect.colliderect(mob_rect):   
                mob_list.remove(mob_rect)
                if mob_rect == enemy_alt_rect:
                    return int(3)
                else:
                    return int(1)
    
    return int(0)

# Main game loop
running = True
while running:
    
    while player_pv <= 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    running = True
                    player_pv = 25
                    score = 0
                    enemy_list = []
                    enemy_alt_list = []
                    bullet_list = []
                    skill_bullet_list = []
                    life_bonus_list = []
                    q_cooldown = 0
                    life_bar_image = life_bar_imageFull
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
                # Set up the game over message
                game_over_text = font.render("Game Over", True, (255, 0, 0))
                game_over_rect = game_over_text.get_rect(center=(width/2, height/2-20))
                screen.blit(game_over_text, game_over_rect)
                
                final_score_text = font.render("Score final: " + str(score), True, (255, 255, 255))
                final_score_rect = final_score_text.get_rect(center=(width/2, height/2+20))
                screen.blit(final_score_text, final_score_rect)
                
                restart_text = font.render("Appuyez sur Entrée pour rejouer ou sur Echap pour quitter", True, (255, 255, 255))
                restart_rect = restart_text.get_rect(center=(width/2, height/2+60))
                screen.blit(restart_text, restart_rect)
                
                pygame.display.flip()
                clock.tick(60)

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
    
    for enemy_alt_rect in enemy_alt_list:
        enemy_alt_rect.move_ip(0,enemy_alt_speed)
        
    # Move the life bonus
    for life_bonus_rect in life_bonus_list:
        life_bonus_rect.move_ip(0,life_bonus_speed)
        
    # Move the rocket bonus
    for rocket_bonus_rect in rocket_bonus_list:
        rocket_bonus_rect.move_ip(0,rocket_bonus_speed)

    # Spawn new enemies
    enemy_spawn_counter += 1
    if enemy_spawn_counter >= enemy_spawn_rate:
        
        enemy_rect = enemy_image.get_rect()
        enemy_rect.centerx = random.randint(10, (width-10))
        enemy_rect.top = -enemy_rect.height
        enemy_list.append(enemy_rect)
        enemy_spawn_counter = 0
    
    enemy_alt_spawn_counter += 1
    if enemy_alt_spawn_counter >= enemy_alt_spawn_rate:
        
        enemy_alt_rect = enemy_alt_image.get_rect()
        enemy_alt_rect.centerx = random.randint(10, (width-10))
        enemy_alt_rect.top = -enemy_alt_rect.height
        enemy_alt_list.append(enemy_alt_rect)
        enemy_alt_spawn_counter = 0
    
    # Spawn life bonus
    life_bonus_spawn_counter += 1
    if life_bonus_spawn_counter >= life_bonus_spawn_rate:
        
        life_bonus_rect = life_bonus_image.get_rect()
        life_bonus_rect.centerx = random.randint(10, (width - 10))
        life_bonus_rect.top = -life_bonus_rect.height
        life_bonus_list.append(life_bonus_rect)
        life_bonus_spawn_rate = random.randint(600,1200)
        life_bonus_spawn_counter = 0
        
    # Spawn rocket bonus
    rocket_bonus_spawn_counter += 1
    if rocket_bonus_spawn_counter >= rocket_bonus_spawn_rate:
        
        rocket_bonus_rect = rocket_bonus_image.get_rect()
        rocket_bonus_rect.centerx = random.randint(10, (width- 10))
        rocket_bonus_rect.top = -rocket_bonus_rect.height
        rocket_bonus_list.append(rocket_bonus_rect)
        rocket_bonus_spawn_rate = random.randint(0,60)
        rocket_bonus_spawn_counter = 0
        
        
    score = score + truc(enemy_rect,enemy_list)   
    score = score + truc(enemy_alt_rect,enemy_alt_list) 
    
    # Detect collisions life bonus
    for life_bonus_rect in life_bonus_list:
        if player_rect.colliderect(life_bonus_rect):
            life_bonus_list.remove(life_bonus_rect)
            if player_pv <= 25:
                player_pv += 5
            elif player_pv >= 30:
                player_pv = 30

    # Detect collisions player
    for enemy_rect in enemy_list:
        if player_rect.colliderect(enemy_rect):
            enemy_list.remove(enemy_rect)
            player_pv -= 5
    
    for enemy_alt_rect in enemy_alt_list:
        if player_rect.colliderect(enemy_alt_rect):
            enemy_alt_list.remove(enemy_alt_rect)
            player_pv -= 10
            
    # Draw the screen
    screen.fill((0, 0, 0))
    
    # Move the background
    bg_y += scroll_speed
    if bg_y > bg.get_height():
        bg_y = 0
    
    # Render the background
    screen.blit(bg, (0, bg_y))
    screen.blit(bg, (0, bg_y - bg.get_height()))

    screen.blit(player_image, player_rect)
    
    # Draw bullet
    for bullet_rect in bullet_list:
        pygame.draw.rect(screen, (255, 255, 255), bullet_rect)
        
    for skill_bullet_rect in skill_bullet_list:
        screen.blit(beam_image, skill_bullet_rect)
        
    # Render enemy
    for enemy_rect in enemy_list:
        screen.blit(enemy_image, enemy_rect)
        
    for enemy_alt_rect in enemy_alt_list:
        screen.blit(enemy_alt_image, enemy_alt_rect)
        
    # Render life bonus
    for life_bonus_rect in life_bonus_list:
        screen.blit(life_bonus_image, life_bonus_rect)
    
    # Render Rocket Bonus
    for rocket_bonus_rect in rocket_bonus_list:
        screen.blit(rocket_bonus_image, rocket_bonus_rect)
        
    # Draw score
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(width/2,20))
    screen.blit(score_text, score_rect)
    
    # Draw life
    if player_pv >= 30:
        life_bar_image = life_bar_imageShield
        update_life_bar(life_bar_image)
    elif player_pv >= 25:
        life_bar_image = life_bar_imageFull
        update_life_bar(life_bar_image)
    elif player_pv >= 20:
        life_bar_image = life_bar_image1hit
        update_life_bar(life_bar_image)
    elif player_pv >= 15:
        life_bar_image = life_bar_image2hit
        update_life_bar(life_bar_image)
    elif player_pv >= 10:
        life_bar_image = life_bar_image3hit
        update_life_bar(life_bar_image)
    elif player_pv >= 5:
        life_bar_image = life_bar_image4hit
        update_life_bar(life_bar_image)
    elif player_pv <= 0:
        life_bar_image = life_bar_imageDead
        update_life_bar(life_bar_image)
    
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
