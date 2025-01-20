"""
Asteroids game.
"""

import pygame

from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

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
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # player setup
    Player.containers = (updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    player = Player(*ORIGIN)

    # asteroids setup
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(COLOR_BLACK)
        for x in updatable:
            x.update(dt)
        for x in drawable:
            x.draw(screen)
        for x in asteroids:
            if player.check_collision(x):
                print("Game over!")
                return
            for shot in shots:
                if shot.check_collision(x):
                    shot.kill()
                    x.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
