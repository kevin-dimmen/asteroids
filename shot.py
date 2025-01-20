from circleshape import CircleShape
from constants import COLOR_WHITE
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_SPEED
import pygame


class Shot(CircleShape):
    """A shot from the player character."""

    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.color = COLOR_WHITE
        self.width = 2
        self.velocity = pygame.Vector2(0, 1).rotate(rotation)
        self.velocity *= PLAYER_SHOOT_SPEED

    def draw(self, screen) -> None:
        pygame.draw.circle(screen, (100, 100, 100), self.position, SHOT_RADIUS)

    def update(self, dt) -> None:
        self.position += self.velocity * dt

