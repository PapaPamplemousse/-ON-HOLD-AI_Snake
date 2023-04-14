"""
Apple module for the Snake game.

This module contains the Apple class that represents the apple in the game.
"""

import pygame


class Apple:
    """Class that represents the apple in the game."""

    SIZE = 10

    def __init__(self, pos):
        """Initialize the apple."""
        self.pos = pos

    def draw(self, surface):
        """Draw the apple on the surface."""
        pygame.draw.rect(surface, (255, 0, 0), (self.pos, (self.SIZE, self.SIZE)))
