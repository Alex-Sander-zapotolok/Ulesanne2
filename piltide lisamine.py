import pygame


pygame.init()


screen = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine (Alex-Sander Zapotõlok)")


screen.fill([204, 255, 204])


bg = pygame.image.load("unnamed (5).jpg")
youWin = pygame.image.load("unnamed (3).png")
youWin = pygame.transform.scale(youWin, [300, 120])


screen.blit(bg, [0, 0])
screen.blit(youWin, [180, 100])


pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()