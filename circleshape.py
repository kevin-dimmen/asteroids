"""Handles circles in the game."""

from __future__ import annotations

import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collision(self, other: CircleShape) -> bool:
        """Check if this is colliding with another circle."""
        collision_distance = self.radius + other.radius
        actual_distance = self.position.distance_to(other.position)
        return actual_distance <= collision_distance
