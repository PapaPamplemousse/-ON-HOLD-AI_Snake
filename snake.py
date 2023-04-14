"""
Snake module for the Snake game.

This module contains the Snake class that represents the snake in the game.
"""

import pygame


class Snake:
    """Class that represents the snake in the game."""

    SIZE = 10

    def __init__(self, pos):
        """Initialize the snake."""
        self.pos = pos
        self.vel = (0, -self.SIZE)
        self.body = [self.pos, (self.pos[0], self.pos[1] + self.SIZE)]

    def handle_keys(self):
        """Handle keyboard input."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.vel = (-self.SIZE, 0)
        elif keys[pygame.K_RIGHT]:
            self.vel = (self.SIZE, 0)
        elif keys[pygame.K_UP]:
            self.vel = (0, -self.SIZE)
        elif keys[pygame.K_DOWN]:
            self.vel = (0, self.SIZE)

    def update(self):
        """Update the snake's position."""
        head = (self.body[0][0] + self.vel[0], self.body[0][1] + self.vel[1])
        self.body.insert(0, head)
        self.body.pop()

    def eat(self, apple):
        """Grow the snake when it eats an apple."""
        self.body.append(self.body[-1])

    def collides_with(self, other):
        """Check if the snake collides with another object."""
        return pygame.Rect(self.pos, (self.SIZE, self.SIZE)).colliderect(
            pygame.Rect(other.pos, (other.SIZE, other.SIZE))
        )

    def draw(self, surface):
        """Draw the snake on the surface."""
        for pos in self.body:
            pygame.draw.rect(surface, (0, 255, 0), (pos, (self.SIZE, self.SIZE)))
