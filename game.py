"""
Game module for the Snake game.

This module contains the Game class that manages the game logic.
"""

import random
import pygame
from snake import Snake
from apple import Apple


class Game:
    """Class that manages the game logic."""

    def __init__(self):
        """Initialize the game."""
        self.width = 640
        self.height = 480
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.snake = Snake((self.width // 2, self.height // 2))
        self.apple = Apple(self.get_random_pos())

    def run(self):
        """Main game loop."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.snake.handle_keys()
            self.snake.update()

            if self.snake.collides_with(self.apple):
                self.snake.eat(self.apple)
                self.apple = Apple(self.get_random_pos())

            self.screen.fill((0, 0, 0))
            self.snake.draw(self.screen)
            self.apple.draw(self.screen)
            pygame.display.flip()

            self.clock.tick(10)

    def get_random_pos(self):
        """Return a random position on the screen."""
        x = random.randint(0, self.width - Apple.SIZE)
        y = random.randint(0, self.height - Apple.SIZE)
        return x, y
