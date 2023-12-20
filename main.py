import pygame
import threading

pygame.init()
run = True
hauteur = pygame.display.Info().current_h
largeur = hauteur * 16 / 9
fond = pygame.image.load('images/background.jpg')
fond = pygame.transform.scale(fond, (largeur, hauteur))
surf = pygame.display.set_mode((largeur, hauteur))
centre_x = largeur // 2
centre_y = hauteur // 2
posX = 50
vx = 1
cadeau = []
pygame.mixer.init()
pygame.mixer.music.load("musique/musique.wav")
logo_cordeliers = pygame.image.load('images/logo_cordeliers.png')

font = pygame.font.SysFont("Arial", 30)
text_noel = font.render("Joyeux Noël !", True, (0, 0, 0))

f = 0.1
if 800 <= largeur < 1200:
    f = 1
elif 400 <= largeur < 800:
    f = 0.5
elif 1200 <= largeur < 1600:
    f = 1.5
elif 1600 <= largeur < 2000:
    f = 2
elif 2000 <= largeur:
    f = 2.5
images_ganonkek = [pygame.image.load(f"frames/frame_{i:02d}_delay-0.04s.gif") for i in range(18)]
images_ganonkek = [pygame.transform.scale(image, (int(image.get_width() * f), int(image.get_height() * f))) for image in images_ganonkek]
compteur_frame = 0
pressed_enter = False
clock=pygame.time.Clock()

def draw_cad(x, y, m):
    pygame.draw.line(surf, (255,255,255), (x, y), (x+100*m, y), 10)
    pygame.draw.line(surf, (255, 255, 255), (x+100*m, y), (x+100*m, y+100*m), 10)
    pygame.draw.line(surf, (255, 255, 255), (x+100*m, y+100*m), (x, y+100), 10)
    pygame.draw.line(surf, (255, 255, 255), (x, y+100*m), (x, y), 10)
    pygame.draw.line(surf, (0, 0, 255), (x+50*m, y), (x+50*m, y+100*m), 30)


def Ganonkek():
    compteur_frame_internal = 0
    clock = pygame.time.Clock()
    x, y = centre_x - images_ganonkek[0].get_width() // 2, centre_y - images_ganonkek[0].get_height() // 2
    while run:
        nbr_image = compteur_frame_internal % len(images_ganonkek)
        surf.blit(images_ganonkek[nbr_image], (x, y))
        compteur_frame_internal = compteur_frame_internal + 1
        clock.tick(35)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    surf.blit(fond, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pressed_enter is False:
                if event.key == pygame.K_RETURN:
                    pressed_enter = True
                    thread_ganonkek = threading.Thread(target=Ganonkek)
                    thread_ganonkek.start()
                    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=1500)
            if event.key == pygame.K_ESCAPE:
                run = False


    surf.blit(fond, (0, 0))
    surf.blit(logo_cordeliers, (50, 50))
    surf.blit(text_noel, (centre_x, centre_y-100*f))
    pygame.display.flip()
    clock.tick(30)

pygame.quit()