import pygame
import random
import time
from load_vaisseau_animer import *
from vaisseau import *
from classe import *

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
    width, height = 1000, 800
    screen = pygame.display.set_mode((width, height))

    # Set up the clock
    clock = pygame.time.Clock()

    #load background image
    bg_size = (width, height)
    bg = pygame.image.load("image/bg2.png").convert()
    
    bg_y=0
    scroll_speed= 2.5

    # Load the player sprite
    default_vaisseau = pygame.image.load("assets/vaisseau/vaisseau_08.png").convert_alpha()

    # Load the enemy sprite
    enemy_image = pygame.image.load("assets/enemy/enemy.png").convert_alpha()
    enemy_alt_image = pygame.image.load("assets/enemy/enemy_alt.png").convert_alpha()
    # Load Shield Boost image
    boost_shield_image = pygame.image.load("assets/Boost/boost_shield.png").convert_alpha()
    # Load Shield Boost image
    boost_rocket_image = pygame.image.load("assets/Boost/boost_rocket.png").convert_alpha()

    vaisseau_05_shield_image = pygame.image.load("assets/vaisseau/Shield/Vaisseau_07/shield_00.png").convert_alpha()
    player_size = (80,80)
    vaisseau_05_shield_image = pygame.transform.scale(vaisseau_05_shield_image,player_size)

    # Player Gold
    gold = get_gold()

    # player Skin
    skin1 = True
    skin2 = False
    skin3 = False
    skin4 = False
    skin5 = False
    skin6 = False
    skin7 = False
    skin8 = False

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
    player_size = (20,80)
    default_vaisseau = pygame.transform.scale(default_vaisseau,player_size)
    player_rect = default_vaisseau.get_rect()
    player_rect.centerx = width // 2
    player_rect.bottom = height - 25
    player_speed = 7

    # Set up the bullets
    bullet_list = []
    bullet_speed = 10

    # anim bullet

    missile_exlposion = displayable("tile003",100)
    explo_size = missile_exlposion.image.get_size()

    # Set up the q skill
    skill_bullet_list = []
    skill_bullet_speed = 20
    q_cooldown = 0
    a_cooldown = 0
    new_a_cooldown = 100
    new_a_cooldown_rt = 100

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

    # Set up the shield boost
    boost_shield_size = (40,40)
    boost_shield_image = pygame.transform.scale(boost_shield_image, boost_shield_size)
    boost_shield_list = []
    boost_shield_speed = 1
    boost_shield_spawn_rate = 500
    boost_shield_spawn_counter = 300

    # Set up the rocket boost
    boost_rocket_size = (40,40)
    boost_rocket_image = pygame.transform.scale(boost_rocket_image, boost_rocket_size)
    boost_rocket_list = []
    boost_rocket_speed = 1
    boost_rocket_spawn_rate = 500
    boost_rocket_spawn_counter = 300

    cooldown_text = True
    shield_attraper = False
    cooldown_text_rocket = True
    rocket_attraper = False
    actif_tir_rocket = None
    skin_rocket = False
    skin_rocket2 = False
    skin_rocket3 = False
    skin_rocket4 = False
    skin_rocket5 = False
    skin_rocket6 = False
    skin_rocket7 = False
    skin_rocket8 = False
    skin_rocket9 = False
    skin_rocket10 = False
    skin_rocket11 = False
    skin_rocket12 = False
    nb_rocket = 6

    def update_life_bar(x):
        x = pygame.transform.scale(x,life_bar_size)
        screen.blit(x, life_bar_rect)
        


        
        return int(0)
    index_vaisseau = 0
    index_skill = 0
    index_bullet = 0
    index_shield = 0
    index_rocket_boost = 0
    index_rocket2_boost = 0
    # Main game loop
    running_boucle_game = True
    while running_boucle_game:
        
        selected_option = get_selected_option()

        if selected_option == 'Skin 2':
            skin2 = True
            skin1 = False    
        if selected_option == 'Skin 3':
            skin3 = True
            skin1 = False
        if selected_option == 'Skin 4':
            skin4 = True
            skin1 = False
        if selected_option == 'Skin 5':
            skin5 = True
            skin1 = False           
        if selected_option == 'Skin 6':
            skin6 = True
            skin1 = False 
        if selected_option == 'Skin 7':
            skin7 = True
            skin1 = False
        if selected_option == 'Skin 8':
            skin8 = True
            skin1 = False
            
        
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
                        a_cooldown = 600
                        new_a_cooldown = 0
                        new_a_cooldown_rt = 0
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
                    bullet_rect = image_bullet.get_rect()
                    bullet_rect.centerx = player_rect.centerx+30
                    bullet_rect.bottom = player_rect.top+40
                    bullet_list.append(bullet_rect)
                    # Fire skill bullet
                if event.key == pygame.K_q:
                    if q_cooldown == 0:
                        skill_bullet_rect = image_beam.get_rect()
                        skill_bullet_rect.centerx = player_rect.centerx+30
                        skill_bullet_rect.bottom = player_rect.top+30
                        skill_bullet_list.append(skill_bullet_rect)
                        q_cooldown = 600
                if event.key == pygame.K_w and actif_tir_rocket == True:
                    cooldown_text_rocket = False
                    if nb_rocket == 6:
                        bullet_rect = image_bullet.get_rect()
                        bullet_rect.centerx = player_rect.centerx+42
                        bullet_rect.bottom = player_rect.top+65
                        bullet_list.append(bullet_rect)
                        skin_rocket = True
                    if nb_rocket == 5:
                        bullet_rect = image_bullet.get_rect()
                        bullet_rect.centerx = player_rect.centerx+20
                        bullet_rect.bottom = player_rect.top+65
                        bullet_list.append(bullet_rect)
                        skin_rocket2 = True
                    if nb_rocket == 4:
                        bullet_rect = image_bullet.get_rect()
                        bullet_rect.centerx = player_rect.centerx+50
                        bullet_rect.bottom = player_rect.top+65
                        bullet_list.append(bullet_rect)
                        skin_rocket5 = True
                    if nb_rocket == 3:
                        bullet_rect = image_bullet.get_rect()
                        bullet_rect.centerx = player_rect.centerx+12
                        bullet_rect.bottom = player_rect.top+65
                        bullet_list.append(bullet_rect)
                        skin_rocket7 = True
                    if nb_rocket == 2:
                        bullet_rect = image_bullet.get_rect()
                        bullet_rect.centerx = player_rect.centerx+58
                        bullet_rect.bottom = player_rect.top+65
                        bullet_list.append(bullet_rect)
                        skin_rocket9 = True
                    if nb_rocket == 1:
                        bullet_rect = image_bullet.get_rect()
                        bullet_rect.centerx = player_rect.centerx+4
                        bullet_rect.bottom = player_rect.top+65
                        bullet_list.append(bullet_rect)
                        skin_rocket11 = True
                    nb_rocket -= 1
                    if nb_rocket <= 0:
                        rocket_attraper = False
                        actif_tir_rocket = False
                        cooldown_text_rocket = True
                        nb_rocket = 6

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

        for boost_shield_rect in boost_shield_list:
            boost_shield_rect.move_ip(0, boost_shield_speed)

        for boost_rocket_rect in boost_rocket_list:
            boost_rocket_rect.move_ip(0, boost_rocket_speed)

        # Draw the screen
        screen.fill((0, 0, 0))
        screen.blit(bg,(0,0))
        if skin1 == True:
            screen.fill((0, 0, 0))
            bg_y+=scroll_speed
            if bg_y>bg.get_height():
                bg_y=0
            screen.blit(bg, (0,bg_y))
            screen.blit(bg,(0,bg_y-bg.get_height())) 
            screen.blit(vaisseau_1[index_vaisseau], player_rect)
            # Passer à l'image suivante de l'animation
            index_vaisseau += 1
            if index_vaisseau >= len(vaisseau_1):
                index_vaisseau = 0
        elif skin2 == True:
            screen.fill((0, 0, 0))
            bg_y+=scroll_speed
            if bg_y>bg.get_height():
                bg_y=0
            screen.blit(bg, (0,bg_y))
            screen.blit(bg,(0,bg_y-bg.get_height()))            
            screen.blit(vaisseau_2[index_vaisseau], player_rect)
            # Passer à l'image suivante de l'animation
            index_vaisseau += 1
            if index_vaisseau >= len(vaisseau_2):
                index_vaisseau = 0
        elif skin3 == True:
            screen.fill((0, 0, 0))
            bg_y+=scroll_speed
            if bg_y>bg.get_height():
                bg_y=0
            screen.blit(bg, (0,bg_y))
            screen.blit(bg,(0,bg_y-bg.get_height()))            
            screen.blit(vaisseau_3[index_vaisseau], player_rect)
            # Passer à l'image suivante de l'animation
            index_vaisseau += 1
            if index_vaisseau >= len(vaisseau_3):
                index_vaisseau = 0
        elif skin4 == True:
            screen.fill((0, 0, 0))
            bg_y+=scroll_speed
            if bg_y>bg.get_height():
                bg_y=0
            screen.blit(bg, (0,bg_y))
            screen.blit(bg,(0,bg_y-bg.get_height()))            
            screen.blit(vaisseau_4[index_vaisseau], player_rect)
            # Passer à l'image suivante de l'animation
            index_vaisseau += 1
            if index_vaisseau >= len(vaisseau_4):
                index_vaisseau = 0
        elif skin5 == True:
            screen.fill((0, 0, 0))
            bg_y+=scroll_speed
            if bg_y>bg.get_height():
                bg_y=0
            screen.blit(bg, (0,bg_y))
            screen.blit(bg,(0,bg_y-bg.get_height()))            
            screen.blit(vaisseau_5[index_vaisseau], player_rect)
            # Passer à l'image suivante de l'animation
            index_vaisseau += 1
            if index_vaisseau >= len(vaisseau_5):
                index_vaisseau = 0
        elif skin6 == True:
            screen.fill((0, 0, 0))
            bg_y+=scroll_speed
            if bg_y>bg.get_height():
                bg_y=0
            screen.blit(bg, (0,bg_y))
            screen.blit(bg,(0,bg_y-bg.get_height()))            
            screen.blit(vaisseau_6[index_vaisseau], player_rect)
            # Passer à l'image suivante de l'animation
            index_vaisseau += 1
            if index_vaisseau >= len(vaisseau_6):
                index_vaisseau = 0
        elif skin7 == True:
            screen.fill((0, 0, 0))
            bg_y+=scroll_speed
            if bg_y>bg.get_height():
                bg_y=0
            screen.blit(bg, (0,bg_y))
            screen.blit(bg,(0,bg_y-bg.get_height()))            
            screen.blit(vaisseau_7[index_vaisseau], player_rect)
            # Passer à l'image suivante de l'animation
            index_vaisseau += 1
            if index_vaisseau >= len(vaisseau_7):
                index_vaisseau = 0
        elif skin8 == True:
            screen.fill((0, 0, 0))
            bg_y+=scroll_speed
            if bg_y>bg.get_height():
                bg_y=0
            screen.blit(bg, (0,bg_y))
            screen.blit(bg,(0,bg_y-bg.get_height()))            
            screen.blit(vaisseau_8[index_vaisseau], player_rect)
            # Passer à l'image suivante de l'animation
            index_vaisseau += 1
            if index_vaisseau >= len(vaisseau_8):
                index_vaisseau = 0
        if skin_rocket == True:          
            screen.blit(vaisseau_06_rocket_image[index_rocket_boost], player_rect)
            # Passer à l'image suivante de l'animation
            index_rocket_boost += 1
            if index_rocket_boost >= 5 :
                skin_rocket = False
                skin_rocket3 = True
            if index_rocket_boost >= len(vaisseau_06_rocket_image):
                index_rocket_boost = 0
        if skin_rocket3 == True:
            screen.blit(vaisseau_06_rocket_image[5], player_rect)
        if skin_rocket2 == True:      
            screen.blit(vaisseau_06_rocket2_image[index_rocket2_boost], player_rect)
            # Passer à l'image suivante de l'animation
            index_rocket2_boost += 1
            if index_rocket2_boost >= 2:
                skin_rocket2 = False
                skin_rocket3 = False
                skin_rocket4 = True
            if index_rocket2_boost >= len(vaisseau_06_rocket2_image):
                index_rocket2_boost = 0
        if skin_rocket4 == True:
            screen.blit(vaisseau_06_rocket2_image[1], player_rect)
        if skin_rocket5 == True:      
            screen.blit(vaisseau_06_rocket3_image[index_rocket2_boost], player_rect)
            # Passer à l'image suivante de l'animation
            index_rocket2_boost += 1
            if index_rocket2_boost >= 2:
                skin_rocket5 = False
                skin_rocket4 = False
                skin_rocket6 = True
            if index_rocket2_boost >= len(vaisseau_06_rocket3_image):
                index_rocket2_boost = 0
        if skin_rocket6 == True:
            screen.blit(vaisseau_06_rocket3_image[1], player_rect)
        if skin_rocket7 == True:      
            screen.blit(vaisseau_06_rocket4_image[index_rocket2_boost], player_rect)
            # Passer à l'image suivante de l'animation
            index_rocket2_boost += 1
            if index_rocket2_boost >= 2:
                skin_rocket7 = False
                skin_rocket6 = False
                skin_rocket8 = True
            if index_rocket2_boost >= len(vaisseau_06_rocket4_image):
                index_rocket2_boost = 0
        if skin_rocket8 == True:
            screen.blit(vaisseau_06_rocket4_image[1], player_rect)
        if skin_rocket9 == True:      
            screen.blit(vaisseau_06_rocket5_image[index_rocket2_boost], player_rect)
            # Passer à l'image suivante de l'animation
            index_rocket2_boost += 1
            if index_rocket2_boost >= 2:
                skin_rocket9 = False
                skin_rocket8 = False
                skin_rocket10 = True
            if index_rocket2_boost >= len(vaisseau_06_rocket5_image):
                index_rocket2_boost = 0
        if skin_rocket10 == True:
            screen.blit(vaisseau_06_rocket5_image[1], player_rect)
        if skin_rocket11 == True:      
            screen.blit(vaisseau_06_rocket6_image[index_rocket2_boost], player_rect)
            # Passer à l'image suivante de l'animation
            index_rocket2_boost += 1
            if index_rocket2_boost >= 2:
                skin_rocket11 = False
                skin_rocket10 = False
                skin_rocket12 = True
            if index_rocket2_boost >= len(vaisseau_06_rocket6_image):
                index_rocket2_boost = 0
        if skin_rocket12 == True:
            screen.blit(vaisseau_06_rocket6_image[1], player_rect)


        # Move the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.move_ip(-player_speed, 0)
        if keys[pygame.K_RIGHT] and player_rect.right < width:
            player_rect.move_ip(player_speed, 0)
        if keys[pygame.K_UP] and player_rect.top > 0:
            player_rect.move_ip(0, -player_speed)
        if keys[pygame.K_DOWN] and player_rect.bottom < height:
            player_rect.move_ip(0, player_speed)
        # Spawn new enemies
        enemy_spawn_counter += 2
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

        boost_shield_spawn_counter += 1
        if boost_shield_spawn_counter >= boost_shield_spawn_rate:
            boost_shield_rect = boost_shield_image.get_rect()
            boost_shield_rect.centerx = random.randint(0, width)
            boost_shield_rect.top = -boost_shield_rect.height
            boost_shield_list.append(boost_shield_rect)
            boost_shield_spawn_counter = 0

        for boost_shield_rect in boost_shield_list:
            if player_rect.colliderect(boost_shield_rect):
                boost_shield_list.remove(boost_shield_rect)
                shield_attraper = True

        boost_rocket_spawn_counter += 1
        if boost_rocket_spawn_counter >= boost_rocket_spawn_rate:
            boost_rocket_rect = boost_rocket_image.get_rect()
            boost_rocket_rect.centerx = random.randint(0, width)
            boost_rocket_rect.top = -boost_rocket_rect.height
            boost_rocket_list.append(boost_rocket_rect)
            boost_rocket_spawn_counter = 0

        for boost_rocket_rect in boost_rocket_list:
            if player_rect.colliderect(boost_rocket_rect):
                boost_rocket_list.remove(boost_rocket_rect)
                rocket_attraper = True

        # a mettre dans une liste
        for bullet_rect in bullet_list:
            for enemy_rect in enemy_list:
                if bullet_rect.colliderect(enemy_rect):
                    temp_enemy_rect = (enemy_rect[0] - explo_size[0]/4, enemy_rect[1] - explo_size[1]/4,enemy_rect[2],enemy_rect[3])
                    enemy_list.remove(enemy_rect)
                    bullet_list.remove(bullet_rect)
                    score += 1
                    gold = int(gold)+1
                    with open("./Save_Stats/Player_Gold.txt", "w") as f:
                        f.write(str(gold))
                    screen.blit(missile_exlposion.image,temp_enemy_rect)
        for bullet_rect in bullet_list:
            for enemy_rect in enemy_alt_list:
                if bullet_rect.colliderect(enemy_rect):
                    temp_enemy_rect = (enemy_rect[0] - explo_size[0]/4, enemy_rect[1] - explo_size[1]/4,enemy_rect[2],enemy_rect[3])
                    enemy_alt_list.remove(enemy_rect)
                    bullet_list.remove(bullet_rect)
                    score += 3
                    gold = int(gold)+3
                    with open("./Save_Stats/Player_Gold.txt", "w") as f:
                        f.write(str(gold))
                    screen.blit(missile_exlposion.image,temp_enemy_rect)
        for skill_bullet_rect in skill_bullet_list:
            for mob_rect in enemy_list:
                if skill_bullet_rect.colliderect(mob_rect):
                    temp_enemy_rect = (enemy_rect[0] - explo_size[0]/4, enemy_rect[1] - explo_size[1]/4,enemy_rect[2],enemy_rect[3])
                    enemy_list.remove(mob_rect)
                    score += 1
                    gold = int(gold)+1
                    with open("./Save_Stats/Player_Gold.txt", "w") as f:
                        f.write(str(gold))
                    screen.blit(missile_exlposion.image,temp_enemy_rect)
        for skill_bullet_rect in skill_bullet_list:
            for mob_rect in enemy_alt_list:
                if skill_bullet_rect.colliderect(mob_rect):
                    temp_enemy_rect = (enemy_rect[0] - explo_size[0]/4, enemy_rect[1] - explo_size[1]/4,enemy_rect[2],enemy_rect[3])
                    enemy_alt_list.remove(mob_rect)
                    score += 3
                    gold = int(gold)+3
                    with open("./Save_Stats/Player_Gold.txt", "w") as f:
                        f.write(str(gold))
                    screen.blit(missile_exlposion.image,temp_enemy_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and cooldown_text == False:
            screen.fill((0, 0, 0))            
            if bg_y>bg.get_height():
                bg_y=0
            screen.blit(bg, (0,bg_y))
            screen.blit(bg,(0,bg_y-bg.get_height()))                                  
            # screen.blit(shield_image, player_rect)
            if skin1:
                screen.blit(vaisseau_01_shield_image[index_vaisseau], player_rect)
            if skin2:
                screen.blit(vaisseau_02_shield_image[index_vaisseau], player_rect)
            if skin3:
                screen.blit(vaisseau_03_shield_image[index_shield], player_rect)
            if skin5:
                screen.blit(vaisseau_05_shield_image, player_rect)
            if skin6:
                screen.blit(vaisseau_06_shield_image[index_vaisseau], player_rect)
            if skin7:
                screen.blit(vaisseau_07_shield_image[index_vaisseau], player_rect)
            # Passer à l'image suivante de l'animation
            if index_shield >= len(vaisseau_03_shield_image):
                index_shield = 0
            new_a_cooldown -= 0.1
        if cooldown_text == False:
            new_a_cooldown_rt = round(new_a_cooldown/1)
            a_skill_text = font.render("Shield Restant: " + str(new_a_cooldown_rt) + "%", True, (255,0,0))
            a_skill_rect = a_skill_text.get_rect(center=(220,height-20))
            screen.blit(a_skill_text, a_skill_rect)
        if new_a_cooldown >= -1 and new_a_cooldown <= 0:
            shield_attraper = False
            cooldown_text = True
        if new_a_cooldown <= 0 and shield_attraper == False:
            a_cooldown = 600
            new_a_cooldown = 100
            new_a_cooldown_rt = 100

        if cooldown_text_rocket == False:
            a_skill_text_rocket = font.render("Nombre de Rockets:" + str(nb_rocket), True, (255,0,0))
            a_skill_rect_rocket = a_skill_text_rocket.get_rect(center=(400,height-20))
            screen.blit(a_skill_text_rocket, a_skill_rect_rocket)

        # Detect collisions player
        for enemy_rect in enemy_list:
            if player_rect.colliderect(enemy_rect):
                enemy_list.remove(enemy_rect)
                player_pv -= 5
        
        for enemy_alt_rect in enemy_alt_list:
            if player_rect.colliderect(enemy_alt_rect):
                enemy_alt_list.remove(enemy_alt_rect)
                player_pv -= 10
                
        # Draw bullet
        for bullet_rect in bullet_list:
            screen.blit(bullet_image[index_bullet], bullet_rect)
            # Passer à l'image suivante de l'animation
            index_bullet += 1
            if index_bullet >= len(bullet_image):
                index_bullet = 0
        for skill_bullet_rect in skill_bullet_list:
            screen.blit(beam_image[index_skill], skill_bullet_rect)
            # Passer à l'image suivante de l'animation
            index_skill += 1
            if index_skill >= len(beam_image):
                index_skill = 0
            
        # Render enemy
        for enemy_rect in enemy_list:
            screen.blit(enemy_image, enemy_rect)
            
        for enemy_alt_rect in enemy_alt_list:
            screen.blit(enemy_alt_image, enemy_alt_rect)

        for boost_shield_rect in boost_shield_list:
            if skin1 == True or skin2 == True or skin3 == True or skin5 == True or skin6 == True or skin7 == True:
                screen.blit(boost_shield_image, boost_shield_rect)
            else:
                pass

        for boost_rocket_rect in boost_rocket_list:
            screen.blit(boost_rocket_image, boost_rocket_rect)
            
        # Draw score
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        score_rect = score_text.get_rect(center=(width/2,20))
        screen.blit(score_text, score_rect)

        # Draw Gold
        gold_text = font.render("Gold: " + str(gold), True, (255, 255, 255))
        gold_rect = gold_text.get_rect(center=(900,10))
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

        if shield_attraper == True:
            if a_cooldown >= 0 and cooldown_text == True and shield_attraper == True:
                a_cooldown_rt = round(a_cooldown/60)
                a_skill_text = font.render("Shield à: " + str(a_cooldown_rt) + "%", True, (255,0,0))
                a_skill_rect = a_skill_text.get_rect(center=(200,height-20))
                screen.blit(a_skill_text, a_skill_rect)
                a_cooldown += 5

            if a_cooldown_rt >= 100.0:
                cooldown_text = False

        if rocket_attraper == True:
            if cooldown_text_rocket == True:
                actif_tir_rocket = True
                a_skill_text_rocket = font.render("Nombre de Rockets:10", True, (255,0,0))
                a_skill_rect_rocket = a_skill_text_rocket.get_rect(center=(400,height-20))
                screen.blit(a_skill_text_rocket, a_skill_rect_rocket)

        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)
        
    # Clean up
    pygame.quit()
