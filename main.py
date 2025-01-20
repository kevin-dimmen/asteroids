"""
Asteroids game.
"""
import pygame

from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH 

from constants import ASTEROID_MIN_RADIUS 
from constants import ASTEROID_KINDS 
from constants import ASTEROID_SPAWN_RATE 
from constants import ASTEROID_MAX_RADIUS 
from constants import COLOR_BLACK

import os

# fix needed for pygame init
os.environ['SDL_AUDIODRIVER'] = 'dsp'


def main() -> None:
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(COLOR_BLACK)
        pygame.display.flip()

    print("Game over")


if __name__ == "__main__":
    main()
