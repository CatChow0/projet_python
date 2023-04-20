import pygame

pygame.init()

background_launcher = pygame.image.load("image/background.png")

font = pygame.font.Font(None, 50)

plus_pos = (260, 335)
minus_pos = (400, 335)

plus_surface = font.render("+", True, (255, 0, 0))
minus_surface = font.render('-', True, (255, 0, 0))

def background_music():
    pygame.mixer.init()
    pygame.mixer.music.load('assets/music/faded.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)

background_music()
def options():
    # Initialisation des variables

    running = True
    screen_width = 1000
    screen_height = 600

    # Initialisation de la fenêtre
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Mon jeu")

    # Initialisation de la police de caractères
    font = pygame.font.SysFont('Arial', 32)

    # Initialisation des couleurs
    text_color = (255, 0, 0)
    selected_color = (0, 0, 0)

    # Initialisation des éléments du menu
    title = font.render('Paramètres', True, text_color)
    title_rect = title.get_rect(center=(screen_width // 2, 50))

    sound_label = font.render('Volume : ', True, text_color)
    sound_label_rect = sound_label.get_rect(center=(screen_width // 2 - 65, 335))

    music_label = font.render('Musique :', True, text_color)
    music_label_rect = music_label.get_rect(center=(screen_width // 2 - 100, 250))

    music_checkbox = pygame.Rect(screen_width // 2 - 30, 230, 50, 50)
    music_checked = False

    volume_music = 0.1

    # Boucle principale du jeu
    while running:

        # Efface l'écran
        screen.blit(background_launcher, (0, 0))

        # Affiche le titre du menu
        screen.blit(title, title_rect)

        screen.blit(music_label, music_label_rect)
        screen.blit(sound_label, sound_label_rect)
        pygame.draw.rect(screen, text_color, music_checkbox, 2)
        if music_checked:
            pygame.draw.line(screen, text_color, (music_checkbox.x, music_checkbox.y), (music_checkbox.x + music_checkbox.width, music_checkbox.y + music_checkbox.height), 2)
            pygame.draw.line(screen, text_color, (music_checkbox.x + music_checkbox.width, music_checkbox.y), (music_checkbox.x, music_checkbox.y + music_checkbox.height), 2)
            # background_music()

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Vérifie si l'utilisateur a cliqué sur les cases à cocher du son ou de la musique
                if music_checkbox.collidepoint(event.pos):
                    music_checked = not music_checked
                # Vérifie si l'utilisateur a cliqué sur le bouton de la résolution
                button_rect = pygame.Rect(screen_width - 200, 0, 200, 50)
                if button_rect.collidepoint(event.pos):
                    dropdown_open = not dropdown_open
                if plus_surface.get_rect(center=plus_pos).collidepoint(event.pos):
                    volume_music = min(1.0, volume_music + 0.01)
                    pygame.mixer.music.set_volume(volume_music)
                # Vérifier si le clic est sur le -
                elif minus_surface.get_rect(center=minus_pos).collidepoint(event.pos):
                    volume_music= max(0.1, volume_music - 0.01)
                    pygame.mixer.music.set_volume(volume_music)

        screen.blit(plus_surface, plus_surface.get_rect(center=plus_pos))
        screen.blit(minus_surface, minus_surface.get_rect(center=minus_pos))
        # Mise à jour de l'écran
        pygame.display.update()
    pygame.quit()