"""


Bonus1: Lancer une boule de feu si on appui sur la touche espace
Bonus2: Modifier le programme pour que le dragon se déplace et rejoigne le clic de la souris en calculant l'angle et distance entre dragon et souris
Ressources: Fonctions sur https://www.pygame.org/docs/
https://riptutorial.com/fr/pygame/topic/3959/commencer-avec-pygame
"""
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
x=402
y=302
FPS = 60
score=0
j=0
directionFacing = 0
i = 0
clockAutoMovement = 0
coords = [x+ 256/2,y +256/2]

objectiveX = 0
objectiveY = 0
obj = [objectiveX,objectiveY]
goingToObjective = False

dragonGauche=[]  # Liste des 8 images du dragon se déplaçant vers la gauche.
dragonGaucheHaut=[]
dragonGaucheBas=[]

dragonDroite=[]
dragonDroiteHaut=[]
dragonDroiteBas=[]

dragonBas=[]
dragonHaut=[]

directions=[dragonGauche,dragonGaucheHaut,dragonGaucheBas,dragonDroite,dragonDroiteHaut,dragonDroiteBas,dragonBas,dragonHaut]

pygame.init() #Initialisation de la bibliothèque Pygame
clock = pygame.time.Clock()  # créer un système permettant de gérer le temps
pygame.key.set_repeat(1, 60) # Si touche appuyée plus de 400ms répétition de 30ms
fenetre = pygame.display.set_mode((largeur, hauteur), RESIZABLE) #Création de la fenêtre redimensionnable
font_obj = pygame.font.Font('freesansbold.ttf', 18)  #On charge la police
im = Image.open("data\wyvern_vol.png")  #On ouvre l'image

# Découpage des 8 premières images du fichier wyvern_vol.png et les mettre dans la liste dragongauche
for i in range (8): #Pour une ligne d'images en entier
    box = (256*i,0,256*(i+1), 256 ) #On découpe un boite autour
    image=im.crop(box) # crée l'image découpée.
    image.save("data\dragonseul.png", "PNG") #On sauvegarde l'image créée
    dragonseul = pygame.image.load("data\dragonseul.png")  #On la charge
    dragonGauche.append(dragonseul) #On l'ajoute dans la liste

for i in range (8): 
    box = (256*i,4*256,256*(i+1), 5*256 ) 
    image=im.crop(box) 
    image.save("data\dragonseul.png", "PNG") 
    dragonseul = pygame.image.load("data\dragonseul.png")  
    dragonDroite.append(dragonseul) 

for i in range (8): 
    box = (256*i,2*256,256*(i+1), 3*256 ) 
    image=im.crop(box) 
    image.save("data\dragonseul.png", "PNG") 
    dragonseul = pygame.image.load("data\dragonseul.png")  
    dragonHaut.append(dragonseul) 

for i in range (8): 
    box = (256*i,6*256,256*(i+1), 7*256 ) 
    image=im.crop(box) 
    image.save("data\dragonseul.png", "PNG") 
    dragonseul = pygame.image.load("data\dragonseul.png")  
    dragonBas.append(dragonseul) 

for i in range (8): 
    box = (256*i,1*256,256*(i+1), 2*256 ) 
    image=im.crop(box) 
    image.save("data\dragonseul.png", "PNG") 
    dragonseul = pygame.image.load("data\dragonseul.png")  
    dragonGaucheHaut.append(dragonseul)

for i in range (8): 
    box = (256*i,3*256,256*(i+1), 4*256 ) 
    image=im.crop(box) 
    image.save("data\dragonseul.png", "PNG") 
    dragonseul = pygame.image.load("data\dragonseul.png")  
    dragonDroiteHaut.append(dragonseul)

for i in range (8): 
    box = (256*i,5*256,256*(i+1), 6*256 ) 
    image=im.crop(box) 
    image.save("data\dragonseul.png", "PNG") 
    dragonseul = pygame.image.load("data\dragonseul.png")  
    dragonDroiteBas.append(dragonseul)


for i in range (8): 
    box = (256*i,7*256,256*(i+1), 8*256 ) 
    image=im.crop(box) 
    image.save("data\dragonseul.png", "PNG") 
    dragonseul = pygame.image.load("data\dragonseul.png")  
    dragonGaucheBas.append(dragonseul)









dragon=dragonGauche[2] # Initialise la première image du dragon
def deplacementGauche():  # Fonction pour déplacer le dragon vers la gauche
    global x, dragon,j
    x=x-10
    



def deplacementDroite():  
    global x, dragon,j
    x=x+10
    

def deplacementHaut():
    global y, dragon,j
    y=y-10
    

def deplacementBas():  
    global y, dragon,j
    y=y+10
    

def deplacementGaucheHaut():  
    global y, x, dragon,j
    y=y-10
    x-=10
    

def deplacementDroiteHaut():  
    global y, x, dragon,j
    y=y-10
    x+=10
    

def deplacementDroiteBas():  
    global y, x, dragon,j
    y=y+10
    x+=10
    

def deplacementGaucheBas():  
    global y, x, dragon,j
    y=y+10
    x-=10
    

#BOUCLE INFINIE
continuer = True
while continuer:
    clock.tick(FPS)#Précise le nombre d'image par seconde Frame par seconde
    coords = [x+ 256/2,y+ 256/2]
    
    clockAutoMovement +=1
    if clockAutoMovement == 2:
        clockAutoMovement =0
    
    obj = [objectiveX,objectiveY]
    while obj[0]%10 != 0:
        obj[0] +=1
    while obj[1]%10 != 0:
        obj[1] +=1
        
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
            if event.key == K_KP1: # Si touche clavier numérique 1
                deplacementGaucheBas()
                directionFacing = 2
            elif event.key == K_KP2: # Si touche clavier numérique 2
                deplacementBas()
                directionFacing = 6
            elif event.key == K_KP3: # Si touche clavier numérique 3
                deplacementDroiteBas()
                directionFacing = 5
            elif event.key == K_KP4: # Si touche clavier numérique 4
                deplacementGauche()
                directionFacing= 0
            elif event.key == K_KP6: # Si touche clavier numérique 6
                deplacementDroite()
                directionFacing= 3
            elif event.key == K_KP7: # Si touche clavier numérique 7
                deplacementGaucheHaut()
                directionFacing = 1
            elif event.key == K_KP8: # Si touche clavier numérique 8
                deplacementHaut()
                directionFacing = 7
            elif event.key == K_KP9: # Si touche clavier numérique 9
                deplacementDroiteHaut()
                directionFacing = 4
            elif event.key == K_KP5:
                if goingToObjective == True:
                    print("Stopped automatic movement by pressing numPad5")
                goingToObjective = False
            
            elif event.key == K_c:
                print("Dragon coordinates =", coords)
            elif event.key == K_o:
                print("Objective coordinates =", obj)


        if event.type == pygame.MOUSEBUTTONDOWN:
            print("MouseX =",mouseX)
            print("MouseY =",mouseY)
            if goingToObjective == False:
                objectiveX = mouseX
                objectiveY = mouseY
                goingToObjective = True
            print("dragonX =", x)
            print("dragonY =", y)
    
    if goingToObjective == True and coords == obj:
        goingToObjective = False
        print("Reached destination and stopped")
              
    if goingToObjective == True and clockAutoMovement == 0:
        if coords[0] < obj[0] and coords[1] < obj[1]:
            deplacementDroiteBas()
            directionFacing = 5
        elif coords[0] > obj[0] and coords[1] > obj[1]:
            deplacementGaucheHaut()
            directionFacing = 1
        elif coords[0] > obj[0] and coords[1] < obj[1]:
            deplacementGaucheBas()
            directionFacing = 2
        elif coords[0] < obj[0] and coords[1] > obj[1]:
            deplacementDroiteHaut()
            directionFacing = 4 
        else:
            if coords[0] < obj[0] and coords[1] == obj[1]:
                deplacementDroite()
                directionFacing = 3
            elif coords[0] > obj[0] and coords[1] == obj[1]:
                deplacementGauche()
                directionFacing = 0
            elif coords[0] == obj[0] and coords[1] > obj[1]:
                deplacementHaut()
                directionFacing = 7
            elif coords[0] == obj[0] and coords[1] < obj[1]:
                deplacementBas()
                directionFacing = 6
                
    
    fenetre.fill(colorWhite) # efface l'image    
    fenetre.blit(dragon, (x,y))  #collage de l'image sur la fenêtre
    pygame.display.flip()  #Rafraîchissement de l'écran


