import pygame
pygame.init()

inputPressed = []
#vector direction corresponding to the key the player press
inputDir = {pygame.K_LEFT:(-1,0),pygame.K_RIGHT:(1,0),pygame.K_UP:(0,-1),pygame.K_DOWN:(0,1)}
#sprite direction corresponding to the key the player press
spriteDir = {pygame.K_LEFT:"l",pygame.K_RIGHT:"r",pygame.K_UP:"b",pygame.K_DOWN:"f"}

size = width, height = 1000, 750
#factor to scall all my sprites
spriteSize = size[0]/500+size[1]/500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
#store all object I want to display each frames
displayList = []
#store all object animated
animatedList = []

class displayable:
    def __init__(self,n,s,p):
        self.name = n
        #save coords in world
        self.x,self.y = p[0],p[1]
        self.spriteName = s
        #associate sprite with object
        s = pygame.image.load("sprites/"+s+".png").convert_alpha()
        self.sizeStart = s.get_size()
        s = pygame.transform.scale(s, (self.sizeStart[0] *spriteSize , self.sizeStart[1] *spriteSize ))
        self.sprite = s
        #add to list to be display each frames
        displayList.append(self)

class animated(displayable):
     def __init__(self,n,s,p,f):
        super().__init__(n,s,p)
        self.maxSprite = f

     def changeSprite(self,s,n):
        self.spriteName = s
        s = pygame.image.load("sprites/"+s+n+".png").convert_alpha()
        s = pygame.transform.scale(s, (self.sizeStart[0] *spriteSize , self.sizeStart[1] *spriteSize ))
        self.sprite = s

class entity(animated):    
    def moveInWorld(self,dir,speed):
        self.x+=inputDir[dir][0]*speed
        self.y+=inputDir[dir][1]*speed

class animLoop(animated):
    def __init__(self, n, s, p, f):
        super().__init__(n, s, p, f)
        animatedList.append(self)

class interactable(animated):
    def __init__(self, n, s, p, f, i):
        super().__init__(n, s, p, f)
        self.playedSprite = 1-(1/i)
        self.imageRate = i

    def changeSprite(self,s,n):     
        self.spriteName = s
        self.playedSprite+=1/self.imageRate
        s = pygame.image.load("sprites/"+s+str(int(self.playedSprite))+".png").convert_alpha()
        s = pygame.transform.scale(s, (self.sizeStart[0] *spriteSize , self.sizeStart[1] *spriteSize ))
        self.sprite = s
        #check if all sprites in the animation have been shown
        if self.playedSprite >= self.maxSprite-1:
            animatedList.remove(self)
            #reset from animation
            self.playedSprite = 1-(1/self.imageRate)

class inputSystem:
    def newDirkey(self,k,t):
        return (not k in inputPressed) and t == pygame.KEYDOWN
    def removeDirKey(self,k,t):
        return k in inputPressed and t == pygame.KEYUP
    def checkDirKey(self,k):
        try :
            spriteDir[k]
            return True
        except:
            return False

running = True
animeFrame = 0
centerPos = (size[0]/2,size[1]/2)

inputsys = inputSystem()
background = animLoop("BG","bg0",(centerPos[0]-(540*spriteSize/2),centerPos[1]-(287 *spriteSize/2)),8)
bedGarry = interactable("Bed","Zz0",(-200+centerPos[0]-(31*spriteSize/2),centerPos[1]-(44 *spriteSize/2)),3,20)
perso = entity("Garry","Gf0",(centerPos[0]-(18*spriteSize/2),centerPos[1]-(26 *spriteSize/2)),4)

while running:
    for event in pygame.event.get():        
        if event.type == pygame.QUIT: 
            running = False        
        
        try:
            if len(inputPressed)>0: 
                #add and remove key from list when is press unpress
                if  inputsys.removeDirKey(event.key,event.type):
                    inputPressed.remove(event.key)
                elif inputsys.newDirkey(event.key,event.type):
                    if inputsys.checkDirKey(event.key):
                        inputPressed.append(event.key)
            else :
                if inputsys.newDirkey(event.key,event.type):
                    if inputsys.checkDirKey(event.key):
                        inputPressed.append(event.key)
                    else :
                        #if its not a ←↑→↓ key go to bed
                        animatedList.append(bedGarry)
                        displayList.remove(perso)
        except:pass  
                    
    if len(inputPressed)>0:
        #save last step direction
        lastDir = inputPressed[len(inputPressed)-1]
        try:
            #move in the curent direction
            perso.moveInWorld(lastDir,10)
        except:pass
        #change animation frames (in motion)
        perso.changeSprite("G"+spriteDir[lastDir] ,str(int((animeFrame*perso.maxSprite)%perso.maxSprite))) 
    else:
        #change animation frames (if is not moving with the last direction)
        perso.changeSprite("G"+perso.spriteName[1:2],"0")
    
    for l in animatedList:
        #change animation frames (for loop animation and curent animation playing)
        l.changeSprite(l.spriteName[0:2],str(int((animeFrame*l.maxSprite)% l.maxSprite)))


    #animationFrameRate
    animeFrame +=0.0375
      
    screen.fill((0,0,0))
    for s in displayList:
        #display all sprite
        screen.blit(s.sprite,(s.x,s.y))
    
    pygame.display.flip()
    clock.tick(60)


pygame.quit()