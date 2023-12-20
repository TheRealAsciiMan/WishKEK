import pygame
import math
import threading
import random

pygame.init()
run = True
largeur, hauteur = pygame.display.Info().current_w, pygame.display.Info().current_h
fond = pygame.image.load('images/background.jpg')
fond = pygame.transform.scale(fond, (largeur, hauteur))
surf = pygame.display.set_mode((largeur, hauteur))
centre_x = largeur // 2
centre_y = hauteur // 2
posX = 50
vx = 1
pygame.mixer.music.load("musique/musique.mp3")
kek0 = pygame.image.load("frames/frame_00_delay-0.04s.gif")
kek1 = pygame.image.load("frames/frame_01_delay-0.04s.gif")
kek2 = pygame.image.load("frames/frame_02_delay-0.04s.gif")
kek3 = pygame.image.load("frames/frame_03_delay-0.04s.gif")
kek4 = pygame.image.load("frames/frame_04_delay-0.04s.gif")
kek5 = pygame.image.load("frames/frame_05_delay-0.04s.gif")
kek6 = pygame.image.load("frames/frame_06_delay-0.04s.gif")
kek7 = pygame.image.load("frames/frame_07_delay-0.04s.gif")
kek8 = pygame.image.load("frames/frame_08_delay-0.04s.gif")
kek9 = pygame.image.load("frames/frame_09_delay-0.04s.gif")
kek10 = pygame.image.load("frames/frame_10_delay-0.04s.gif")
kek11 = pygame.image.load("frames/frame_11_delay-0.04s.gif")
kek12 = pygame.image.load("frames/frame_12_delay-0.04s.gif")
kek13 = pygame.image.load("frames/frame_13_delay-0.04s.gif")
kek14 = pygame.image.load("frames/frame_14_delay-0.04s.gif")
kek15 = pygame.image.load("frames/frame_15_delay-0.04s.gif")
kek16 = pygame.image.load("frames/frame_16_delay-0.04s.gif")
kek17 = pygame.image.load("frames/frame_17_delay-0.04s.gif")
images_ganonkek = [kek0, kek1, kek2, kek3, kek4, kek5, kek6, kek7, kek8, kek9, kek10, kek11, kek12, kek13, kek14, kek15, kek16, kek17]
traineau_s = pygame.image.load('images/traineau.png')
if 800 <= largeur < 1200:
    f = 1
elif 400 <= largeur < 800:
    f = 1
elif 1200 <= largeur < 1600:
    f = 1
elif 1600 <= largeur < 2000:
    f = 1
elif 2000 <= largeur:
    f = 1
compteur_frame = 0
clock=pygame.time.Clock()

def draw_cad(x, y, m):
    pygame.draw.line(surf, (255,255,255), (x, y), (x))
    pygame.draw.lin

class Cadeaux:
    def __init__(self):

        self.y = None

    sprite = pygame.image.load('images/Cadeau.png')

    def draw(self, surf, x, y):
        self.y = y

        cox = x-1
        coy = y

        surf.blit(self.sprite,(cox,coy))

        cox += 0.2
        coy = - cox**2 + 1

def destruction(lst):
    for i in lst:
        if i.y == hauteur:
            del i

def traineau(lst):
    xtrain = 1920//2
    ytrain = 540
    surf.blit(traineau_s, (int(xtrain), int(ytrain)))
    if xtrain == 0:
        xtrain = 1920
    elif xtrain == 1920//3:
        if lst[0] == None:
            pass
        else:
            lst[0].draw(surf, xtrain, ytrain)
    elif xtrain == 1920//2:
        if lst[1] == None:
            pass
        else:
            lst[1].draw(surf, xtrain, ytrain)
    elif xtrain == (1920//3)*2:
        if lst[2] == None:
            pass
        else:
            lst[2].draw(surf, xtrain, ytrain)
    xtrain -= 3
    pygame.display.flip()



pressed_enter = False
cadeau = []
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.mixer.music.play(loops=-1)
    surf.blit(fond, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            pressed_enter == False
            while pressed_enter is False:
                if event.key == pygame.K_RETURN:
                    x, y = centre_x - 360 // 2, centre_y - 360 // 2
                    nbr_image = compteur_frame % len(images_ganonkek)
                    surf.blit(images_ganonkek[nbr_image], (x, y))
                    compteur_frame = compteur_frame + 1
                    pygame.display.flip()
                    clock.tick(30)
                    surf.blit(fond, (0, 0))
                elif event.key == pygame.K_SPACE:
                    if cadeau == []:
                        cadeau = [Cadeaux() for i in range(3)]
                    traineau(cadeau)
                    destruction(cadeau)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()