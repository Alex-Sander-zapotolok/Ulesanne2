import pygame

pygame.init()

screen = pygame.display.set_mode([640,480])
pygame.display.set_caption("Harjutamine (Alex-Sander Zapotõlok)")
screen.fill([204,255,204])

font = pygame.font.Font(pygame.font.match_font('times new roman'), 50)
text = font.render("Hello Pygame", True, [0,0,0])

text_width = text.get_rect().width
text_height = text.get_rect().height

screen.blit(text, [320,240])

pygame.display.flip()

while True:
    print()