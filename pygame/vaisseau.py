class Vaisseau:
    def __init__(self, pv, degat):
        self.pv = pv
        self.degat = degat

    def up(self):
        self.pv = 1
        self.degat += 10


Vaisseau_1 = Vaisseau(10,10)
Vaisseau_2 = Vaisseau(20,20)
Vaisseau_3 = Vaisseau(30,30)
Vaisseau_4 = Vaisseau(40,40)
Vaisseau_5 = Vaisseau(50,50)
Vaisseau_6 = Vaisseau(60,60)
Vaisseau_7 = Vaisseau(70,70)
Vaisseau_8 = Vaisseau(80,80)
Vaisseau_9 = Vaisseau(90,90)
Vaisseau_10 = Vaisseau(100,100)


List_Vaisseau = [Vaisseau_1, Vaisseau_2, Vaisseau_3, Vaisseau_4, Vaisseau_5, Vaisseau_6, Vaisseau_7, Vaisseau_8, Vaisseau_9, Vaisseau_10]