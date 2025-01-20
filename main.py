"""
Asteroids game.
"""

import pygame

from player import Player

from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH

from constants import ASTEROID_MIN_RADIUS
from constants import ASTEROID_KINDS
from constants import ASTEROID_SPAWN_RATE
from constants import ASTEROID_MAX_RADIUS
from constants import COLOR_BLACK

import os

# fix needed for pygame init
os.environ["SDL_AUDIODRIVER"] = "dsp"

ORIGIN = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


def main() -> None:
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # group setup
    updatable  = pygame.sprite.Group()
    drawable   = pygame.sprite.Group()

    # player setup
    Player.containers = (updatable, drawable)
    player = Player(*ORIGIN)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(COLOR_BLACK)
        for x in updatable:
            x.update(dt)
        for x in drawable:
            x.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
