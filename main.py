import pygame

surf = pygame.display.set_mode((800, 600))
run = True
img = pygame.image.load("pyg.png")
posX = 50
vx = 1
clock=pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                print(pygame.mouse.get_pos())
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("vous avez appuyé sur la touche espace")
                surf.blit(img, (200, 200))
                pygame.display.flip()
            elif event.key == pygame.K_a:
                print("vous avez appuyé sur la touche A")
            elif event.key == pygame.K_RETURN:
                print("vous avez appuyé sur la touche Entrée")
                surf.fill((0, 0, 0))
                pygame.draw.circle(surf, (255, 0, 0), (posX, 300), 30, 2)
                if posX > 770 or posX < 30:
                    vx = -vx
                posX = posX + vx
                pygame.display.flip()
            else:
                print("vous avez appuyé sur une touche")

    surf.fill((0, 0, 0))
    clock.tick(60)

pygame.quit()