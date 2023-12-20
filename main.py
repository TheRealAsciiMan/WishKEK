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
pygame.mixer.init()
pygame.mixer.music.load("musique/musique.wav")
font = pygame.font.SysFont("Harrington", 128)
text_noel = font.render("Joyeux Noël !", True, (0, 0, 0))
text_enter = font.render("Appuyez sur Entrée", True, (255, 255, 255))
f = 0.1
if 800 <= largeur < 1200:
    f = 0.25
elif 400 <= largeur < 800:
    f = 0.20
elif 1200 <= largeur < 1600:
    f = 0.5
elif 1600 <= largeur < 2000:
    f = 1
elif 2000 <= largeur:
    f = 2
images_ganonkek = [pygame.image.load(f"frames/frame_{i:02d}_delay-0.04s.gif") for i in range(18)]
images_ganonkek = [pygame.transform.scale(image, (int(image.get_width() * f), int(image.get_height() * f))) for image in images_ganonkek]
logo_cordeliers = pygame.image.load('images/logo_cordeliers.png')
logo_cordeliers = pygame.transform.scale(logo_cordeliers, (int(logo_cordeliers.get_width() * f/2), int(logo_cordeliers.get_height() * f/2)))
image_cadeau = pygame.image.load('images/Cadeau.png')
image_cadeau = pygame.transform.scale(image_cadeau, (int(image_cadeau.get_width() * f/2), int(image_cadeau.get_height() * f/2)))
image_traineau = pygame.image.load('images/traineau.png')
image_traineau = pygame.transform.scale(image_traineau, (int(image_traineau.get_width() * f/2), int(image_traineau.get_height() * f/2)))
compteur_frame = 0
pressed_enter = False
clock=pygame.time.Clock()



def Ganonkek():
    compteur_frame_internal = 0
    clock = pygame.time.Clock()
    x, y = centre_x - images_ganonkek[0].get_width() // 2, centre_y - images_ganonkek[0].get_height() // 2
    while run:
        nbr_image = compteur_frame_internal % len(images_ganonkek)
        surf.blit(fond, (0, 0))
        surf.blit(images_ganonkek[nbr_image], (x, y))
        compteur_frame_internal = compteur_frame_internal + 1
        clock.tick(38)
        pygame.display.flip()

def images():
    compteur_frame_internal = 0
    clock = pygame.time.Clock()
    x1, y1 = centre_x - largeur // 4, centre_y
    x1 -= 150 *f
    x2, y2 = centre_x + largeur // 4, centre_y
    x2 -= 150 *f
    rainbow_colors = [
        (255, 0, 0),    # Rouge
        (255, 165, 0),  # Orange
        (255, 255, 0),  # Jaune
        (0, 255, 0),    # Vert
        (0, 0, 255),    # Bleu
        (75, 0, 130),   # Indigo
        (148, 0, 211)   # Violet
    ]
    while run:
        couleur_actuelle = rainbow_colors[compteur_frame_internal % len(rainbow_colors)]
        surf.blit(image_cadeau, (x1, y1))
        surf.blit(image_traineau, (x2, y2))
        surf.blit(logo_cordeliers, (50, 50))
        text_noel = font.render("Joyeux Noël !", True, couleur_actuelle)
        surf.blit(text_noel, (centre_x - 330, centre_y - 300 * f))
        compteur_frame_internal += 1
        clock.tick(60)




surf.blit(fond, (0, 0))
surf.blit(logo_cordeliers, (50, 50))
surf.blit(text_noel, (centre_x - 330, centre_y - 300 * f))
surf.blit(text_enter, (centre_x - 500, centre_y + 150 * f))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pressed_enter is False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pressed_enter = True
                    thread_ganonkek = threading.Thread(target=Ganonkek)
                    thread_dessins = threading.Thread(target=images)
                    thread_ganonkek.start()
                    thread_dessins.start()
                    pygame.mixer.music.play(loops=-1, start=0.0, fade_ms=1500)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    if pressed_enter is False:
        surf.blit(text_enter, (centre_x - 500, centre_y + 150 * f))
    clock.tick(10)

pygame.quit()