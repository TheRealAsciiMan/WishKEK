import pygame
import threading

# Initialisation de Pygame
pygame.init()

# Définition de constantes
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Création de la fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dessin Pixel par Pixel")

# Indicateur pour savoir si les threads sont en cours d'exécution
threads_en_cours = False

# Fonction pour dessiner un cercle pixel par pixel
def dessiner_cercle():
    clock = pygame.time.Clock()
    for x in range(100):
        for y in range(100):
            pygame.draw.circle(screen, WHITE, (x + 100, y + 100), 1)
            pygame.display.flip()
            clock.tick(60)

# Fonction pour dessiner un rectangle pixel par pixel
def dessiner_rectangle():
    clock = pygame.time.Clock()
    for x in range(100):
        for y in range(100):
            pygame.draw.rect(screen, WHITE, (x + 300, y + 100, 1, 1))
            pygame.display.flip()
            clock.tick(60)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not threads_en_cours:
                threads_en_cours = True
                thread_cercle = threading.Thread(target=dessiner_cercle)
                thread_rectangle = threading.Thread(target=dessiner_rectangle)
                thread_cercle.start()
                thread_rectangle.start()
            elif event.key == pygame.K_a:
                print("vous avez appuyé sur la touche A")
# Quitter Pygame
pygame.quit()
