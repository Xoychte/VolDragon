"""
Vol de dragon en python avec biblio Pygame
Copier si nécessaire le dossier PIL contenant la bibliothèque PIL dans le dossier C:\Program Files (x86)\Thonny\Lib\site-packages
Créer par F HERGNIOT complété par ..........  
Ouvrir et analyser le fichier wyvern_vol.png. Déterminer la taille de découpe de chaque image.
Analyser le programme en cours en le commentant derrière #
Utiliser la bibliothèque Image de PIL pour découper le fichier  wyvern_vol.png en une suite de 8x8 images 
Mettre ces images dans des listes en fonction du déplacement vers la gauche, droite, haut, nord-est ....
En fonction de l'appui sur les touches du clavier numérique déplacer le dragon selon la direction ( 4 à gauche 8 en haut 7 nord-est...)
en changeant les 8 images de la liste correspondante pour donner l'impression de vol.
Si aucune touche est appuyée, il fera du surplace.

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
x=400
y=300
FPS = 60
score=0
j=0


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
    dragon=dragonGauche[j]   # à compléter pour changer d'image lors du déplacement
    j+=1
    if j == 8:
        j = 0


def deplacementDroite():  
    global x, dragon,j
    x=x+10
    dragon=dragonDroite[j]   
    j+=1
    if j == 8:
        j = 0

def deplacementHaut():
    global y, dragon,j
    y=y-10
    dragon=dragonHaut[j]  
    j+=1
    if j == 8:
        j = 0

def deplacementBas():  
    global y, dragon,j
    y=y+10
    dragon=dragonBas[j]   
    j+=1
    if j == 8:
        j = 0

def deplacementGaucheHaut():  
    global y, x, dragon,j
    y=y-10
    x-=10
    dragon=dragonGaucheHaut[j]   
    j+=1
    if j == 8:
        j = 0

def deplacementDroiteHaut():  
    global y, x, dragon,j
    y=y-10
    x+=10
    dragon=dragonDroiteHaut[j]   
    j+=1
    if j == 8:
        j = 0

def deplacementDroiteBas():  
    global y, x, dragon,j
    y=y+10
    x+=10
    dragon=dragonDroiteBas[j]   
    j+=1
    if j == 8:
        j = 0

def deplacementGaucheBas():  
    global y, x, dragon,j
    y=y+10
    x-=10
    dragon=dragonGaucheBas[j]   
    j+=1
    if j == 8:
        j = 0


#BOUCLE INFINIE
continuer = True
while continuer:
    clock.tick(FPS)#Précise le nombre d'image par seconde Frame par seconde

    #j+=1
    #if j == 8:
    #    j = 0

    for event in pygame.event.get() :   #On parcours la liste de tous les événements reçus
        if event.type == QUIT:     #Si un de ces événements est de type QUIT (Alt+F4) ou bouton fermeture
            continuer = False      #On arrête la boucle
        if event.type == KEYDOWN :  # Si touche appuyée
            if event.key == K_KP1: # Si touche clavier numérique 1
                deplacementGaucheBas()
            if event.key == K_KP2: # Si touche clavier numérique 2
                deplacementBas()
            if event.key == K_KP3: # Si touche clavier numérique 3
                deplacementDroiteBas()
            if event.key == K_KP4: # Si touche clavier numérique 4
                deplacementGauche()
            if event.key == K_KP6: # Si touche clavier numérique 6
                deplacementDroite()
            if event.key == K_KP7: # Si touche clavier numérique 7
                deplacementGaucheHaut()
            if event.key == K_KP8: # Si touche clavier numérique 8
                deplacementHaut()
            if event.key == K_KP9: # Si touche clavier numérique 9
                deplacementDroiteHaut()

                
                

              
                
                
    
    fenetre.fill(colorWhite) # efface l'image    
    fenetre.blit(dragon, (x,y))  #collage de l'image sur la fenêtre
    pygame.display.flip()  #Rafraîchissement de l'écran


