import pygame
from pygame.locals import *
from Joueur import Joueur
from Balle import Balle
import os
import time
os.nice(0)
print(str(os.getpid()))
print(str(os.getppid()))
pygame.init()

fenetre = pygame.display.set_mode((1000,500))

fond = pygame.image.load("ressource/121217-kissa.jpg").convert()


joueur1 = Joueur("ressource/Player1.png")
joueur2 = Joueur("ressource/Player2.png")




balle = Balle()

joueur1.rect.x = 40
joueur2.rect.x = 947

ite = 0
sortie = True

continuer = 1
font = pygame.font.SysFont("comicsansms", 100)
for i in range(0, 3):
    text_timer = font.render(str(3-i), True, (255,255,255))
    fenetre.blit(fond, (0,0))
    fenetre.blit(text_timer, (500 - text_timer.get_width()//2, 250 - text_timer.get_height() // 2 ))
    pygame.display.flip()
    time.sleep(1)

font = pygame.font.SysFont("comicsansms", 50)
stop = 1
while continuer:

    if ite == 300:
        balle.velocity += 1
        ite = 0
    ite+=1

    fenetre.blit(fond, (0,0))
    fenetre.blit(joueur1.image,joueur1.rect)
    fenetre.blit(joueur2.image,joueur2.rect)
    fenetre.blit(balle.image, balle.rect)
    text = font.render(str(joueur1.score) + " | " + str(joueur2.score), True, (255,255,255))
    fenetre.blit(text, (500 - text.get_width()//2, 0))
    balle.move()
    


    if balle.rect.x + balle.rect.width > 1000 or (balle.rect.x + balle.rect.width > 947 and joueur2.rect.y < balle.rect.y + balle.rect.height < joueur2.rect.y + joueur2.rect.height) :
        balle.dirx = -1
        
    elif balle.rect.x < 0 or (balle.rect.x < 40 + joueur1.rect.width and joueur1.rect.y < balle.rect.y + balle.rect.height < joueur1.rect.y + joueur1.rect.height):
        balle.dirx = 1
        


    if balle.rect.y + balle.rect.height > 500:
        balle.diry = -1
        balle.velocity += 1

    elif balle.rect.y < 0:
        balle.diry = 1
        balle.velocity += 1


    if joueur1.pressed.get(pygame.K_z) and joueur1.rect.y > 0:
        joueur1.move_up()
    elif joueur1.pressed.get(pygame.K_s) and joueur1.rect.y < 500-112:
        joueur1.move_down()

    if joueur2.pressed.get(pygame.K_UP)  and joueur2.rect.y > 0:
        joueur2.move_up()
    elif joueur2.pressed.get(pygame.K_DOWN) and joueur2.rect.y < 500-112:
        joueur2.move_down()
    
    if balle.rect.x + balle.rect.width < joueur1.rect.x and sortie :
        joueur2.add_score()
        balle = Balle()
        balle.dirx = 1
        sortie = False
    if balle.rect.x > joueur2.rect.x + joueur2.rect.width and sortie:
        joueur1.add_score()
        balle = Balle()
        balle.dirx = -1
        sortie = False
    if (balle.rect.x > joueur1.rect.x and balle.rect.x < fenetre.get_width() / 2  )or ( balle.rect.x < joueur2.rect.x and balle.rect.x > fenetre.get_width() / 2 ):
        sortie = True
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            continuer = 0
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            joueur1.pressed[event.key] = True
            joueur2.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            joueur1.pressed[event.key] = False
            joueur2.pressed[event.key] = False
    
    if joueur1.score == 7:
        fenetre.blit(fond, (0,0))
        text_vict = font.render("Victoire du Joueur 1", True, (179, 0, 0))
        fenetre.blit(text_vict, (500 - text_timer.get_width()//2, 250 - text_timer.get_height() // 2 ))
        pygame.display.flip()
        time.sleep(10)
        continuer = 0
    elif joueur2.score == 7:
        fenetre.blit(fond, (0,0))
        text_vict = font.render("Victoire du Joueur 2", True, (0, 82, 204))
        fenetre.blit(text_vict, (500 - text_timer.get_width()//2, 250 - text_timer.get_height() // 2 ))
        pygame.display.flip()
        time.sleep(10)
        continuer = 0
            