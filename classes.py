import pygame
import random

class displayable :
    def __init__(self,image_name,scaleSize):
        self.image = pygame.image.load(image_name+".png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(scaleSize,scaleSize))


# class animated(displayable) :
#     def __init__(self, image_name, scaleSize):
#         super().__init__(image_name, scaleSize)

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

    def __onDest__(self,hp,score) :
        if hp <= 0 :
            score += 1

class boss(enemy) :
    def __init__(self, image_name, scaleSize, hp, speed,shootSpeed,score):
        self.aS = shootSpeed
        super().__init__(image_name, scaleSize, hp, speed)
    
    def __onDest__(self, hp):
        super().__onDest__(hp)
    
    def shoot_pattern(playerPos,shootSpeed,projectileBoss):
        



class player(entity) :
    def __init__(self, image_name, scaleSize, hp,speed,attackSpeed):
        self.hp = hp
        self.attackSpeed = attackSpeed

        super().__init__(image_name, scaleSize, speed)


