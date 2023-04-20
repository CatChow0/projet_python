import pygame, sys
from button import Button
from cosmetique import *
from jeu import boucle_jeu, get_gold, get_stats
from vaisseau import *

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Menu")

# # Music de fond du Launcher #
# def sound():
#     pygame.mixer.init()
#     pygame.mixer.music.load('assets/music/faded.mp3')
#     pygame.mixer.music.set_volume(0.1)
#     pygame.mixer.music.play(-1)
# # Activation de la music lors du lancement de la fenêtre #
# sound()

background_launcher = pygame.image.load("image/background.png")
background_shop = pygame.image.load("image/background_shop.png")

start_btn = pygame.image.load('image/1.png').convert_alpha()
exit_btn = pygame.image.load('image/2.png').convert_alpha()
setting_btn = pygame.image.load('image/3.png').convert_alpha()
shop_btn = pygame.image.load('image/shop.png').convert_alpha()
retour_btn = pygame.image.load('image/retour.png').convert_alpha()

cosmetique_btn = pygame.image.load('image/retour.png').convert_alpha()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/SIXTY.ttf", size)

# Create a function to draw the menu
def draw_menu(x, y):
    global selected_option
    for i, option in enumerate(menu_options):
        text = get_font(27).render(option, True, WHITE)
        rect = text.get_rect()
        rect.x = x
        rect.y = y + i * rect.height
        if rect.collidepoint(pygame.mouse.get_pos()):
            text = get_font(27).render(option, True, "#FFAA00")
            if pygame.mouse.get_pressed()[0]:
                selected_option = i
        screen.blit(text, rect)



# Create a function to draw the "Valider" button
def draw_button_valider(x, y, stats):
    gold = int(get_gold())
    button_text = get_font(27).render("Valider", True, WHITE)
    button_rect = button_text.get_rect()
    button_rect.x = x
    button_rect.y = y
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        button_text = get_font(27).render("Valider", True, "#FFAA00")
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if selected_option is not None and (List_Vaisseau[selected_option].locked == True and List_Vaisseau[selected_option].prix <= gold):
                        with open("./Save_Stats/Skin_Vaisseau.txt", "w") as f:
                            f.write(menu_options[selected_option])
                        with open("./Save_Stats/Vaisseau_stats.txt", "w") as f:
                            f.write(str(selected_option))
                        gold = gold - List_Vaisseau[selected_option].prix
                        List_Vaisseau[int(stats)].locked = False
                        with open("./Save_Stats/Player_Gold.txt", "w") as f:
                            f.write(str(gold))
    if selected_option is not None and List_Vaisseau[selected_option].locked == True and List_Vaisseau[selected_option].prix > gold:
        skin_lock_text = font.render("Skin Vérouiller", True, (255, 0, 0))
        skin_lock_rect = skin_lock_text.get_rect(center=(720, 80))
        screen.blit(skin_lock_text, skin_lock_rect)
    else:
        skin_unlock_text = font.render("Skin Disponible à l'achat", True, (0, 255, 0))
        skin_unlock_rect = skin_unlock_text.get_rect(center=(720, 80))
        screen.blit(skin_unlock_text, skin_unlock_rect)
    screen.blit(button_text, button_rect)

# Create a function to draw the "Menu Principal" button
def draw_button_menu_principal(x, y):
    button_text = get_font(27).render("Retour", True, WHITE)
    button_rect = button_text.get_rect()
    button_rect.x = x
    button_rect.y = y
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        button_text = get_font(27).render("Retour", True, "#FFAA00")
        if pygame.mouse.get_pressed()[0]:
            main_menu()
    screen.blit(button_text, button_rect)

def shop_cosmetique(stats):
    run_shop = True
    while run_shop:
        stats = get_stats()

        screen.blit(background_shop, (0, 0))

        MENU_TEXT = get_font(40).render("Skin Vaisseau", True, "#FFB833")
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH // 2, 120))
        screen.blit(MENU_TEXT, MENU_RECT)

        draw_menu(110, 145)
        draw_button_valider(320, 520, stats)
        draw_button_menu_principal(210, 520)

        ################################### AGRANDIR L IMAGE POUR MIEUX LA VOIR #########################################
        nouvelle_taille = (option1_image.get_width() // 2, option1_image.get_height() // 2)
        image_agrandie = pygame.transform.scale(option1_image, nouvelle_taille)

        nouvelle_taille2 = (option2_image.get_width() // 2, option2_image.get_height() // 2)
        image_agrandie2 = pygame.transform.scale(option2_image, nouvelle_taille2)

        nouvelle_taille3 = (option3_image.get_width() // 2, option3_image.get_height() // 2)
        image_agrandie3 = pygame.transform.scale(option3_image, nouvelle_taille3)

        nouvelle_taille4 = (option4_image.get_width() // 3.5, option4_image.get_height() // 3.5)
        image_agrandie4 = pygame.transform.scale(option4_image, nouvelle_taille4)

        nouvelle_taille5 = (option5_image.get_width() // 3.5, option5_image.get_height() // 3.5)
        image_agrandie5 = pygame.transform.scale(option5_image, nouvelle_taille5)

        nouvelle_taille6 = (option6_image.get_width() // 3.5, option6_image.get_height() // 3.5)
        image_agrandie6 = pygame.transform.scale(option6_image, nouvelle_taille6)

        nouvelle_taille7 = (option7_image.get_width() // 3.5, option7_image.get_height() // 3.5)
        image_agrandie7 = pygame.transform.scale(option7_image, nouvelle_taille7)

        nouvelle_taille8 = (option8_image.get_width() // 3.5, option8_image.get_height() // 3.5)
        image_agrandie8 = pygame.transform.scale(option8_image, nouvelle_taille8)

        # nouvelle_taille9 = (option9_image.get_width() // 3.5, option9_image.get_height() // 3.5)
        # image_agrandie9 = pygame.transform.scale(option9_image, nouvelle_taille9)

        # nouvelle_taille10 = (option10_image.get_width() // 3.5, option10_image.get_height() // 3.5)
        # image_agrandie10 = pygame.transform.scale(option10_image, nouvelle_taille10)

        # Draw the selected option
        if selected_option == 0:
            screen.blit(image_agrandie, (300, 175))
        elif selected_option == 1:
            screen.blit(image_agrandie2, (300, 175))
        elif selected_option == 2:
            screen.blit(image_agrandie3, (300, 175))
        elif selected_option == 3:
            screen.blit(image_agrandie4, (300, 175))
        elif selected_option == 4:
            screen.blit(image_agrandie5, (300, 175))
        elif selected_option == 5:
            screen.blit(image_agrandie6, (300, 175))
        elif selected_option == 6:
            screen.blit(image_agrandie7, (300, 175))
        elif selected_option == 7:
            screen.blit(image_agrandie8, (300, 175))
        # elif selected_option == 8:
        #     screen.blit(image_agrandie9, (300, 175))
        # elif selected_option == 9:
        #     screen.blit(image_agrandie10, (300, 175))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Mise à jour de l'écran
        pygame.display.update()

# ------------------------------------------------------------------------ FIN FUNCTION OPTIONS ------------------------------------------------------------------------ #


start_button = Button(200, 300, start_btn, 0.8)
exit_button = Button(500, 310, exit_btn, 0.74)
setting_button = Button(940, 10, setting_btn, 0.1)
shop_button = Button(800, 300, shop_btn, 0.1)
retour_boutton = Button(940, 10, retour_btn, 0.1)

def main_menu():
    while True:
        stats = get_stats()

        screen.blit(background_launcher, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("Alien Assault", True, "#FFAA00")
        MENU_RECT = MENU_TEXT.get_rect(center=(SCREEN_WIDTH // 2, 100))

        PLAY_BUTTON = Button(SCREEN_WIDTH // 5, SCREEN_HEIGHT // 2, start_btn, 0.8)
        QUIT_BUTTON = Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.94, exit_btn, 0.74)
        OPTIONS_BUTTON = Button(940, 10, setting_btn, 0.1)
        SHOP_BUTTON = Button(10, 10, shop_btn, 0.1)

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, SHOP_BUTTON, QUIT_BUTTON]:

            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    boucle_jeu()
                # if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                #     sound()
                if SHOP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    shop_cosmetique(stats)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()