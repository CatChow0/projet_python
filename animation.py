import pygame

class Animation(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(0, 20):
            img = pygame.image.load(f"assets/Bigboom{num}.png")
            img = pygame.tansform.scale(img,(100,100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.counter = 0
        
    def update(self):
        explosion_speed = 4
        self.counter += 1
        
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
            
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill