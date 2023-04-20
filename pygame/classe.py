import pygame
import random

class displayable :
    def __init__(self,image_name,scaleSize):
        self.image = pygame.image.load(image_name+".png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(scaleSize,scaleSize))

class entity(displayable):
    def __init__(self, image_name, scaleSize,speed):
        self.speed = speed
        super().__init__(image_name, scaleSize)

class projectile(entity):
    def __init__(self, image_name, scaleSize, speed,damage):
        self.dmg = damage
        super().__init__(image_name, scaleSize, speed)

class enemy(entity) : 
    def __init__(self,image_name,scaleSize,hp,speed):
        self.hp = hp
        super().__init__(image_name,scaleSize,speed)

class player(entity) :
    def __init__(self, image_name, scaleSize, hp,speed,attackSpeed):
        self.hp = hp
        self.attackSpeed = attackSpeed

        super().__init__(image_name, scaleSize, speed)