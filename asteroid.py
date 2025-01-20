import pygame
from circleshape import CircleShape
from constants import COLOR_WHITE

class Asteroid(CircleShape):
    """Represents and asteroid object."""

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = COLOR_WHITE
        self.width = 2

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, (100, 100, 100), self.position, self.width)

    def update(self, dt) -> None:
        self.position += self.velocity * dt

