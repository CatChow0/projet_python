import pygame
import time

fenetre = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jeu")
COULEUR_FOND = (255, 255, 255)

background_launcher = pygame.image.load("image/background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/SIXTY.ttf", size)

def loading_screen():
    fenetre.blit(background_launcher, (0, 0))

    for i in range(101):
        pygame.draw.rect(fenetre, (255, 0, 0), (100, 250, i * 6.5, 100))
        MENU_TEXT = get_font(50).render("CHARGEMENT", True, "#050000")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 300))
        fenetre.blit(MENU_TEXT, MENU_RECT)
        pygame.display.update()
        time.sleep(0.01)