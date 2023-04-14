"""
Apple module for the Snake game.

This module contains the Apple class that represents the apple in the game.
"""

import pygame
import random


class Apple:
    """Class that represents the apple in the game."""

    SIZE = 10

    def __init__(self, pos):
        """Initialize the apple."""
        self.pos = pos

    def reposition(self, snake):
        """Reposition the apple."""
        while self.pos in snake.body:
            x = random.randrange(0, snake.width - self.SIZE, self.SIZE)
            y = random.randrange(0, snake.height - self.SIZE, self.SIZE)
            self.pos = (x, y)

    def draw(self, surface):
        """Draw the apple on the surface."""
        pygame.draw.rect(surface, (255, 0, 0), (self.pos, (self.SIZE, self.SIZE)))
