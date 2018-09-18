import pygame

from settings import Settings

from rocket import Rocket

import game_function as gf

from pygame.sprite import Group


def run_game():
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Rocket Game")
    rocket = Rocket(ai_settings, screen)
    bullets = Group()

    while True:
        gf.check_events(ai_settings, screen, rocket, bullets)
        rocket.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))
        gf.update_screen(ai_settings, screen, rocket, bullets)


run_game()
