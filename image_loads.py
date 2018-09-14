import pygame
import sys


def show_window():
    pygame.init()
    screen = pygame.display.set_mode((1280, 800))
    image = pygame.image.load('greatwall.bmp').convert_alpha()
    pygame.display.set_caption("Wallpaper")

    bg_color = (230, 122, 20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        screen.blit(image, (0, 0))
        pygame.display.flip()


show_window()
