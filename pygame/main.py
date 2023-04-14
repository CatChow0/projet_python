import pygame, sys
from button import Button
from cosmetique import *
from jeu import boucle_jeu
from settings import options

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Menu")

background_launcher = pygame.image.load("image/background.png")
background_shop = pygame.image.load("image/background_shop.png")

start_btn = pygame.image.load('image/1.png').convert_alpha()
exit_btn = pygame.image.load('image/2.png').convert_alpha()
setting_btn = pygame.image.load('image/3.png').convert_alpha()
shop_btn = pygame.image.load('image/shop.png').convert_alpha()
retour_btn = pygame.image.load('image/retour.png').convert_alpha()

cosmetique_btn = pygame.image.load('image/retour.png').convert_alpha()

# background_music()

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/SIXTY.ttf", size)

# Create a function to draw the menu
def draw_menu(x, y):
    global selected_option
    for i, option in enumerate(menu_options):
        text = font.render(option, True, WHITE)
        rect = text.get_rect()
        rect.x = x
        rect.y = y + i * rect.height
        if rect.collidepoint(pygame.mouse.get_pos()):
            text = font.render(option, True, GREEN)
            if pygame.mouse.get_pressed()[0]:
                selected_option = i
        screen.blit(text, rect)

# Create a function to draw the "Valider" button
def draw_button_valider(x, y):
    button_text = font.render("Valider", True, WHITE)
    button_rect = button_text.get_rect()
    button_rect.x = x
    button_rect.y = y
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        button_text = font.render("Valider", True, GREEN)
        if pygame.mouse.get_pressed()[0]:
            if selected_option is not None:
                with open("./Save_Stats/Skin_Vaisseau.txt", "w") as f:
                    f.write(menu_options[selected_option])
                with open("./Save_Stats/Vaisseau_stats.txt", "w") as f:
                    f.write(str(selected_option))
    screen.blit(button_text, button_rect)

# Create a function to draw the "Menu Principal" button
def draw_button_menu_principal(x, y):
    button_text = font.render("Retour", True, WHITE)
    button_rect = button_text.get_rect()
    button_rect.x = x
    button_rect.y = y
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        button_text = font.render("Retour", True, GREEN)
        if pygame.mouse.get_pressed()[0]:
            main_menu()
    screen.blit(button_text, button_rect)

def shop_cosmetique():
    run_shop = True
    while run_shop:
        screen.blit(background_shop, (0, 0))

        MENU_TEXT = get_font(40).render("Skin Vaisseau", True, "#FFB833")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 50))
        screen.blit(MENU_TEXT, MENU_RECT)

        draw_menu(85, 150)
        draw_button_valider(270, 470)
        draw_button_menu_principal(150, 470)

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

        nouvelle_taille9 = (option9_image.get_width() // 3.5, option9_image.get_height() // 3.5)
        image_agrandie9 = pygame.transform.scale(option9_image, nouvelle_taille9)

        nouvelle_taille10 = (option10_image.get_width() // 3.5, option10_image.get_height() // 3.5)
        image_agrandie10 = pygame.transform.scale(option10_image, nouvelle_taille10)

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
        elif selected_option == 8:
            screen.blit(image_agrandie9, (300, 175))
        elif selected_option == 9:
            screen.blit(image_agrandie10, (300, 175))
        
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
        screen.blit(background_launcher, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("SPACE BONGO NA BONGO", True, "#6EF119")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        PLAY_BUTTON = Button(90, 300, start_btn, 0.8)
        QUIT_BUTTON = Button(400, 310, exit_btn, 0.74)
        OPTIONS_BUTTON = Button(740, 10, setting_btn, 0.1)
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
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if SHOP_BUTTON.checkForInput(MENU_MOUSE_POS):
                    shop_cosmetique()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()