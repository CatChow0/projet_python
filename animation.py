import pygame

class Animation(pygame.sprite.Sprite):
    def __init__(self,x,y,speed):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.speed = speed
        for num in range(0, 20):
            img = pygame.image.load(f"assets/Big_boom{num}.png")
            img = pygame.transform.scale(img,(600,600))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.counter = 0
                
    def updateTest(self):
        explosion_speed = 4
        self.counter += 1
        self.rect.center =(self.rect.center[0],self.rect.center[1] + self.speed)
        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
            return True
        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.kill
            return False
        
        return True