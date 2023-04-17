import pygame

pygame.init()
window = pygame.display.set_mode((250, 250))

sprite1 = pygame.sprite.Sprite()
sprite1.image = pygame.Surface((80, 80), pygame.SRCALPHA)
pygame.draw.circle(sprite1.image, (255, 0, 0), (40, 40), 40)
sprite1.rect = pygame.Rect(*window.get_rect().center, 0, 0).inflate(80, 80)
sprite1.radius = 40

all_group = pygame.sprite.Group([sprite1])

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    sprite1.rect.center = pygame.mouse.get_pos()

    window.fill(0)
    all_group.draw(window)
    pygame.display.flip()

pygame.quit()
exit()