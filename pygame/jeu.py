import pygame
import random
from vaisseau import *

# Initialize Pygame
pygame.init()

# ----------------------------------- Récupérer la valeur dans Vaisseau.txt ----------------------------- #
def get_selected_option():
    try:
        with open("./Save_Stats/Skin_Vaisseau.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

# ----------------------------------- Récupérer la valeur dans Vaisseau_Stats.txt ----------------------------- #
def get_stats():
    try:
        with open("./Save_Stats/Vaisseau_stats.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None
# ----------------------------------- Récupérer la valeur dans Player_Gold.txt ----------------------------- #
def get_gold():
    try:
        with open("./Save_Stats/Player_Gold.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None


def boucle_jeu():

    # Set up the display
    width, height = 1280, 720
    screen = pygame.display.set_mode((width, height))

    # Set up the clock
    clock = pygame.time.Clock()

    # Set up the background
    bg = pygame.image.load("image/background1.png").convert_alpha()
    bg = pygame.transform.scale(bg, (width,height))

    # Load the player sprite
    default_vaisseau = pygame.image.load("assets/vaisseau_in_game/vaisseau5.png").convert_alpha()

    # Load the enemy sprite
    enemy_image = pygame.image.load("assets/enemy/enemy.png").convert_alpha()
    enemy_alt_image = pygame.image.load("assets/enemy/enemy_alt.png").convert_alpha()

    # Load Beam sprite
    beam_image = pygame.image.load("assets/skill_arme/beam.png").convert_alpha()

    skin_vaisseau1 = pygame.image.load('assets/vaisseau_in_game/vaisseau1.png').convert_alpha()
    skin_vaisseau2 = pygame.image.load('assets/vaisseau_in_game/vaisseau2.png').convert_alpha()
    skin_vaisseau3 = pygame.image.load('assets/vaisseau_in_game/vaisseau3.png').convert_alpha()
    skin_vaisseau4 = pygame.image.load('assets/vaisseau_in_game/vaisseau4.png').convert_alpha()
    skin_vaisseau5 = pygame.image.load('assets/vaisseau_in_game/vaisseau5.png').convert_alpha()
    skin_vaisseau6 = pygame.image.load('assets/vaisseau_in_game/vaisseau6.png').convert_alpha()
    skin_vaisseau7 = pygame.image.load('assets/vaisseau_in_game/vaisseau7.png').convert_alpha()
    skin_vaisseau8 = pygame.image.load('assets/vaisseau_in_game/vaisseau8.png').convert_alpha()
    skin_vaisseau9 = pygame.image.load('assets/vaisseau_in_game/vaisseau9.png').convert_alpha()
    skin_vaisseau10 = pygame.image.load('assets/vaisseau_in_game/vaisseau10.png').convert_alpha()

    # Player Gold
    gold = get_gold()

    # player Skin
    skin1 = False
    skin2 = False
    skin3 = False
    skin4 = False
    skin5 = False
    skin6 = False
    skin7 = False
    skin8 = False
    skin9 = False
    skin10 = False

    # Set up the score
    score = 0
    font = pygame.font.SysFont(None, 24)

    # Load the life bar sprite
    life_bar_image = pygame.image.load("assets/barre_vie/LifeBarFull.png").convert_alpha()
    life_bar_image1hit = pygame.image.load("assets/barre_vie/LifeBar1hit.png").convert_alpha()
    life_bar_image2hit = pygame.image.load("assets/barre_vie/LifeBar2hit.png").convert_alpha()
    life_bar_image3hit = pygame.image.load("assets/barre_vie/LifeBar3hit.png").convert_alpha()
    life_bar_image4hit = pygame.image.load("assets/barre_vie/LifeBar4hit.png").convert_alpha()
    life_bar_imageDead = pygame.image.load("assets/barre_vie/LifeBarDead.png").convert_alpha()
    life_bar_imageFull = life_bar_image

    # Set up the life bar
    life_bar_size = (200,75)
    life_bar_image = pygame.transform.scale(life_bar_image,life_bar_size)
    life_bar_rect = life_bar_image.get_rect()
    life_bar_rect.left = 10
    life_bar_rect.top = 10
    player_pv = 25

    # Set up the player
    player_size = (20,10)
    default_vaisseau = pygame.transform.scale(default_vaisseau,player_size)
    player_rect = default_vaisseau.get_rect()
    player_rect.centerx = width // 2
    player_rect.bottom = height - 5
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


    def update_life_bar(x):
        x = pygame.transform.scale(x,life_bar_size)
        screen.blit(x, life_bar_rect)
        


        
        return int(0)
    # Main game loop
    running_boucle_game = True
    while running_boucle_game:

        selected_option = get_selected_option()
        stats = get_stats()

        if selected_option == 'Skin 1':
            skin1 = True
        elif selected_option == 'Skin 2':
            skin2 = True
        elif selected_option == 'Skin 3':
            skin3 = True
        elif selected_option == 'Skin 4':
            skin4 = True
        elif selected_option == 'Skin 5':
            skin5 = True
        elif selected_option == 'Skin 6':
            skin6 = True
        elif selected_option == 'Skin 7':
            skin7 = True
        elif selected_option == 'Skin 8':
            skin8 = True
        elif selected_option == 'Skin 9':
            skin9 = True
        elif selected_option == 'Skin 10':
            skin10 = True
        
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
                running_boucle_game = False
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

        # Spawn new enemies
        enemy_spawn_counter += 1
        if enemy_spawn_counter >= enemy_spawn_rate:
            enemy_rect = enemy_image.get_rect()
            enemy_rect.centerx = random.randint(0, width)
            enemy_rect.top = -enemy_rect.height
            enemy_list.append(enemy_rect)
            enemy_spawn_counter = 0
        
        enemy_alt_spawn_counter += 1
        if enemy_alt_spawn_counter >= enemy_alt_spawn_rate:
            enemy_alt_rect = enemy_alt_image.get_rect()
            enemy_alt_rect.centerx = random.randint(0, width)
            enemy_alt_rect.top = -enemy_alt_rect.height
            enemy_alt_list.append(enemy_alt_rect)
            enemy_alt_spawn_counter = 0
            
        for bullet_rect in bullet_list:
            for enemy_rect in enemy_list:
                if bullet_rect.colliderect(enemy_rect):
                    enemy_list.remove(enemy_rect)
                    bullet_list.remove(bullet_rect)
                    score += 1
                    gold = int(gold)+1
                    with open("./Save_Stats/Player_Gold.txt", "w") as f:
                        f.write(str(gold))
        for bullet_rect in bullet_list:
            for enemy_rect in enemy_alt_list:
                if bullet_rect.colliderect(enemy_rect):
                    enemy_alt_list.remove(enemy_rect)
                    bullet_list.remove(bullet_rect)
                    score += 3
                    gold = int(gold)+3
                    with open("./Save_Stats/Player_Gold.txt", "w") as f:
                        f.write(str(gold))
        for skill_bullet_rect in skill_bullet_list:
            for mob_rect in enemy_list:
                if skill_bullet_rect.colliderect(mob_rect):
                    enemy_list.remove(mob_rect)
                    score += 1
                    gold = int(gold)+1
                    with open("./Save_Stats/Player_Gold.txt", "w") as f:
                        f.write(str(gold))
        for skill_bullet_rect in skill_bullet_list:
            for mob_rect in enemy_alt_list:
                if skill_bullet_rect.colliderect(mob_rect):
                    enemy_alt_list.remove(mob_rect)
                    score += 3
                    gold = int(gold)+3
                    with open("./Save_Stats/Player_Gold.txt", "w") as f:
                        f.write(str(gold))

        

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
        screen.blit(bg,(0,0))
        if skin1 == True:
            screen.fill((0, 0, 0))
            screen.blit(skin_vaisseau5, player_rect)
        elif skin2 == True:
            screen.fill((0, 0, 0))
            screen.blit(skin_vaisseau6, player_rect)
        elif skin3 == True:
            screen.fill((0, 0, 0))
            screen.blit(skin_vaisseau7, player_rect)
        elif skin4 == True:
            screen.fill((0, 0, 0))
            screen.blit(skin_vaisseau1, player_rect)
        elif skin5 == True:
            screen.fill((0, 0, 0))
            screen.blit(skin_vaisseau2, player_rect)
        elif skin6 == True:
            screen.fill((0, 0, 0))
            screen.blit(skin_vaisseau3, player_rect)
        elif skin7 == True:
            screen.fill((0, 0, 0))
            screen.blit(skin_vaisseau8, player_rect)
        elif skin8 == True:
            screen.fill((0, 0, 0))
            screen.blit(skin_vaisseau10, player_rect)
        elif skin9 == True:
            screen.fill((0, 0, 0))
            screen.blit(skin_vaisseau4, player_rect)
        elif skin10 == True:
            screen.fill((0, 0, 0))
            screen.blit(skin_vaisseau9, player_rect)
        
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
            
        # Draw score
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(width/2,20))
        screen.blit(score_text, score_rect)

        # Draw Gold
        gold_text = font.render("Gold: " + str(gold), True, (255, 255, 255))
        gold_rect = gold_text.get_rect(center=(1235,10))
        screen.blit(gold_text, gold_rect)
        
        # Draw life
        if player_pv >= 25:
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
