"""
Snake module for the Snake game.

This module contains the Snake class that represents the snake in the game.
"""

import pygame


class Snake:
    """Class that represents the snake in the game."""

    SIZE = 10

    def __init__(self, pos, surface, width, height):
        """Initialize the snake."""
        self.pos = pos
        self.vel = (0, -self.SIZE)
        self.body = [self.pos]
        self.grow = False
        self.surface = surface
        self.width = width
        self.height = height

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
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False

    def eat(self, apple):
        """Grow the snake when it eats an apple."""
        if self.body[0] == apple.pos:
            self.grow = True
            apple.reposition(self)
            self.draw()

    def collides_with_wall(self):
        """Check if the snake collides with a wall."""
        x, y = self.body[0]
        return x < 0 or x >= self.width or y < 0 or y >= self.height

    def collides_with_self(self):
        """Check if the snake collides with itself."""
        return self.body[0] in self.body[1:]

    def draw(self):
        """Draw the snake on the surface."""
        for pos in self.body:
            pygame.draw.rect(self.surface, (0, 255, 0), (pos, (self.SIZE, self.SIZE)))
        pygame.display.flip()
