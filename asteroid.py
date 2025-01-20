import pygame
from circleshape import CircleShape
from constants import COLOR_WHITE
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    """Represents and asteroid object."""

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.color = COLOR_WHITE
        self.width = 2

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, self.color, self.position, self.radius)

    def update(self, dt) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        left_asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        right_asteroid = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
        left_asteroid.velocity = self.velocity.rotate(split_angle) * 1.2
        right_asteroid.velocity = self.velocity.rotate(-split_angle) * 1.2