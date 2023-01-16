#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
from math import sqrt  #
#from image import *
from PIL import Image  #
# Initialisation des variables
(largeur, hauteur) = (1000, 800)  # definit la hauteur et la largeur de la fenêtre de l'application
colorWhite=(255,255,255)   #On définit la couleur blanche
colorRed=(255,0,0)   #On définit la couleur rouge
dragonX=402
dragonY=302
FPS = 60
score=0
j=0
directionFacing = 0
i = 0
clockAutoMovement = 0
coords = [dragonX+ 256/2,dragonY +256/2]

fireballX = -100
fireballY = -100
fireballRun = False
fireballCounter = 0

objectiveX = 0
objectiveY = 0
obj = [objectiveX,objectiveY]
goingToObjective = False

dragonLeft=[]  # Liste des 8 images du dragon se déplaçant vers la gauche.
dragonLeftUp=[]
dragonLeftDown=[]

dragonRight=[]
dragonRightUp=[]
dragonRightDown=[]

dragonDown=[]
dragonUp=[]

directions=[dragonLeft,dragonLeftUp,dragonLeftDown,dragonRight,dragonRightUp,dragonRightDown,dragonDown,dragonUp]

fireballAnim=[]

pygame.init() #Initialisation de la bibliothèque Pygame
clock = pygame.time.Clock()  # créer un système permettant de gérer le temps
pygame.key.set_repeat(1, 60) # Si touche appuyée plus de 400ms répétition de 30ms
fenetre = pygame.display.set_mode((largeur, hauteur), RESIZABLE) #Création de la fenêtre redimensionnable
font_obj = pygame.font.Font('freesansbold.ttf', 18)  #On charge la police
im = Image.open("data\wyvern_vol.png")  #On ouvre l'image
im2 = Image.open("data\explosion.png")
# Découpage des 8 premières images du fichier wyvern_vol.png et les mettre dans la liste dragongauche
for i in range (8): #Pour une ligne d'images en entier
    box = (256*i,0,256*(i+1), 256 ) #On découpe un boite autour
    image=im.crop(box) # crée l'image découpée.
    image.save("data\dragonAlone.png", "PNG") #On sauvegarde l'image créée
    dragonAlone = pygame.image.load("data\dragonAlone.png")  #On la charge
    dragonLeft.append(dragonAlone) #On l'ajoute dans la liste

for i in range (8): 
    box = (256*i,4*256,256*(i+1), 5*256 ) 
    image=im.crop(box) 
    image.save("data\dragonAlone.png", "PNG") 
    dragonAlone = pygame.image.load("data\dragonAlone.png")  
    dragonRight.append(dragonAlone) 

for i in range (8): 
    box = (256*i,2*256,256*(i+1), 3*256 ) 
    image=im.crop(box) 
    image.save("data\dragonAlone.png", "PNG") 
    dragonAlone = pygame.image.load("data\dragonAlone.png")  
    dragonUp.append(dragonAlone) 

for i in range (8): 
    box = (256*i,6*256,256*(i+1), 7*256 ) 
    image=im.crop(box) 
    image.save("data\dragonAlone.png", "PNG") 
    dragonAlone = pygame.image.load("data\dragonAlone.png")  
    dragonDown.append(dragonAlone) 

for i in range (8): 
    box = (256*i,1*256,256*(i+1), 2*256 ) 
    image=im.crop(box) 
    image.save("data\dragonAlone.png", "PNG") 
    dragonAlone = pygame.image.load("data\dragonAlone.png")  
    dragonLeftUp.append(dragonAlone)

for i in range (8): 
    box = (256*i,3*256,256*(i+1), 4*256 ) 
    image=im.crop(box) 
    image.save("data\dragonAlone.png", "PNG") 
    dragonAlone = pygame.image.load("data\dragonAlone.png")  
    dragonRightUp.append(dragonAlone)

for i in range (8): 
    box = (256*i,5*256,256*(i+1), 6*256 ) 
    image=im.crop(box) 
    image.save("data\dragonAlone.png", "PNG") 
    dragonAlone = pygame.image.load("data\dragonAlone.png")  
    dragonRightDown.append(dragonAlone)


for i in range (8): 
    box = (256*i,7*256,256*(i+1), 8*256 ) 
    image=im.crop(box) 
    image.save("data\dragonAlone.png", "PNG") 
    dragonAlone = pygame.image.load("data\dragonAlone.png")  
    dragonLeftDown.append(dragonAlone)

for n in range(5):
    for i in range (8): 
        box = (128*i,n*128,128*(i+1), n*128+128 ) 
        image=im2.crop(box) 
        image.save("data\\fireballAlone.png", "PNG") 
        fireballAlone = pygame.image.load("data\\fireballAlone.png")  
        fireballAnim.append(fireballAlone)





fireball = fireballAnim[0]
dragon=dragonLeft[2] # Initialise la première image du dragon
def movingLeft():  # Fonction pour déplacer le dragon vers la gauche
    global dragonX, dragon,j
    dragonX=dragonX-10
    
def movingRight():  
    global dragonX, dragon,j
    dragonX=dragonX+10
    

def movingUp():
    global dragonY, dragon,j
    dragonY=dragonY-10
    

def movingDown():  
    global dragonY, dragon,j
    dragonY=dragonY+10
    

def movingLeftUp():  
    global dragonY, dragonX, dragon,j
    dragonY=dragonY-5
    dragonX-=5
    

def movingRightUp():  
    global dragonY, dragonX, dragon,j
    dragonY=dragonY-5
    dragonX+=5
    

def movingRightDown():  
    global dragonY, dragonX, dragon,j
    dragonY=dragonY+5
    dragonX+=5
    

def movingLeftDown():  
    global dragonY, dragonX, dragon,j
    dragonY=dragonY+5
    dragonX-=5
    

#BOUCLE INFINIE
continuer = True
while continuer:
    clock.tick(FPS)#Précise le nombre d'image par seconde Frame par seconde
    coords = [dragonX+ 256/2,dragonY+ 256/2]
    
    clockAutoMovement +=1
    if clockAutoMovement == 2:
        clockAutoMovement =0
    
    
        
    mouseX, mouseY =  pygame.mouse.get_pos()
    
    
    dragon = directions[directionFacing][j]
    i+=1
    if i > 4: 
        j += 1
        if j == 8:
            j = 0
        i = 0
    for event in pygame.event.get() :   #On parcours la liste de tous les événements reçus
        if event.type == QUIT:     #Si un de ces événements est de type QUIT (Alt+F4) ou bouton fermeture
            continuer = False      
        if event.type == KEYDOWN :  # Si touche appuyée
            if event.key == K_KP1 and goingToObjective == False: # Si touche clavier numérique 1
                movingLeftDown()
                directionFacing = 2
            elif event.key == K_KP2 and goingToObjective == False: # Si touche clavier numérique 2
                movingDown()
                directionFacing = 6
            elif event.key == K_KP3 and goingToObjective == False: # Si touche clavier numérique 3
                movingRightDown()
                directionFacing = 5
            elif event.key == K_KP4 and goingToObjective == False: # Si touche clavier numérique 4
                movingLeft()
                directionFacing= 0
            elif event.key == K_KP6 and goingToObjective == False: # Si touche clavier numérique 6
                movingRight()
                directionFacing= 3
            elif event.key == K_KP7 and goingToObjective == False: # Si touche clavier numérique 7
                movingLeftUp()
                directionFacing = 1
            elif event.key == K_KP8 and goingToObjective == False: # Si touche clavier numérique 8
                movingUp()
                directionFacing = 7
            elif event.key == K_KP9 and goingToObjective == False: # Si touche clavier numérique 9
                movingRightUp()
                directionFacing = 4
            elif event.key == K_KP5:
                if goingToObjective == True:
                    print("Stopped automatic movement by pressing numPad5")
                    goingToObjective = False
            
            elif event.key == K_c:
                print("Dragon coordinates =", coords)
            elif event.key == K_o:
                print("Objective coordinates =", obj)
            elif event.key == K_SPACE and fireballRun == False:
                print("Launching fireball")
                fireballX = dragonX+64
                fireballY = dragonY+64
                fireballDirection = directionFacing
                fireballRun = True
                



        if event.type == pygame.MOUSEBUTTONDOWN:
            print("MouseX =",mouseX)
            print("MouseY =",mouseY)
            if goingToObjective == False and fireballRun == False :
                objectiveX = mouseX
                objectiveY = mouseY
                goingToObjective = True
            print("dragonX =", dragonX)
            print("dragonY =", dragonY)
    
    obj = [objectiveX,objectiveY]
    while obj[0]%10 != 0:
        obj[0] +=1
    while obj[1]%10 != 0:
        obj[1] +=1
              
    if goingToObjective == True and clockAutoMovement == 0:
        if coords[0] < obj[0] and coords[1] < obj[1]:
            movingRightDown()
            directionFacing = 5
        elif coords[0] > obj[0] and coords[1] > obj[1]:
            movingLeftUp()
            directionFacing = 1
        elif coords[0] > obj[0] and coords[1] < obj[1]:
            movingLeftDown()
            directionFacing = 2
        elif coords[0] < obj[0] and coords[1] > obj[1]:
            movingRightUp()
            directionFacing = 4 
        else:
            if coords[0] < obj[0] and coords[1] == obj[1]:
                movingRight()
                directionFacing = 3
            elif coords[0] > obj[0] and coords[1] == obj[1]:
                movingLeft()
                directionFacing = 0
            elif coords[0] == obj[0] and coords[1] > obj[1]:
                movingUp()
                directionFacing = 7
            elif coords[0] == obj[0] and coords[1] < obj[1]:
                movingDown()
                directionFacing = 6
    if goingToObjective == True and coords == obj:
        goingToObjective = False
        print("Reached destination and stopped")              
    
    if fireballRun == True and clockAutoMovement == 0 and goingToObjective == False:
        fireballCounter += 1
        fireball= fireballAnim[fireballCounter]
        if fireballDirection == 6:
            fireballY+=15
        elif fireballDirection == 7:
            fireballY-=15
        elif fireballDirection == 0:
            fireballX-=15
        elif fireballDirection == 3:
            fireballX+=15
        
        elif fireballDirection == 1:
            fireballY-=10
            fireballX-=10
        elif fireballDirection == 2:
            fireballY+=10
            fireballX-=10
        elif fireballDirection == 4:
            fireballY-=10
            fireballX+=10          
        elif fireballDirection == 5:
            fireballY+=10
            fireballX+=10
           
        if fireballCounter == 39:
            fireballCounter = 0
            fireballRun = False
        
    
    
    fenetre.fill(colorWhite) # efface l'image    
    fenetre.blit(dragon, (dragonX,dragonY))  #collage de l'image sur la fenêtre
    fenetre.blit(fireball,(fireballX,fireballY))
    pygame.display.flip()  #Rafraîchissement de l'écran


