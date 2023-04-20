import pygame

class Vaisseau:
    def __init__(self, pv, degat, prix, locked, image_name, scale):
        self.pv = pv
        self.degat = degat
        self.prix = prix
        self.locked = locked
        self.image = pygame.image.load("assets/vaisseau/"+image_name+".png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(scale,scale))

    def up(self):
        self.pv = 1
        self.degat += 10


Vaisseau_1 = Vaisseau(10,10, 0, True, "vaisseau_01", 40)
Vaisseau_2 = Vaisseau(20,20, 0, True, "vaisseau_02", 40)
Vaisseau_3 = Vaisseau(30,30, 0, True, "vaisseau_03", 40)
Vaisseau_4 = Vaisseau(40,40, 250, True, "vaisseau_04", 40)
Vaisseau_5 = Vaisseau(50,50, 250, True, "vaisseau_05", 40)
Vaisseau_6 = Vaisseau(60,60, 250, True, "vaisseau_06", 40)
Vaisseau_7 = Vaisseau(70,70, 250, True, "vaisseau_07", 40)
Vaisseau_8 = Vaisseau(80,80, 250, True, "vaisseau_08", 40)
# Vaisseau_9 = Vaisseau(90,90, 250, True, "vaisseau4", 40)
# Vaisseau_10 = Vaisseau(100,100, 250, True, "vaisseau9", 40)


List_Vaisseau = [Vaisseau_1, Vaisseau_2, Vaisseau_3, Vaisseau_4, Vaisseau_5, Vaisseau_6, Vaisseau_7, Vaisseau_8]