"""
Game module for the Snake game.

This module contains the Game class that represents the game.
"""

import pygame
from snake import Snake
from apple import Apple


class Game:
    """Class that represents the game."""

    WIDTH = 640
    HEIGHT = 480
    FPS = 10

    def __init__(self):
        """Initialize the game."""
        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.snake = Snake((self.WIDTH // 2, self.HEIGHT // 2), self.surface, self.WIDTH, self.HEIGHT)
        self.apple = Apple((self.WIDTH // 2, self.HEIGHT // 2))
        self.font = pygame.font.SysFont(None, 50)

    def handle_events(self):
        """Handle events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def check_collision(self):
        """Check if the snake has collided with a wall or itself."""
        if self.snake.collides_with_wall() or self.snake.collides_with_self():
            self.game_over = True

    def run(self):
        """Run the game."""
        self.running = True
        self.game_over = False
        while self.running:
            self.handle_events()

            if self.game_over:
                game_over_text = self.font.render("Game Over", True, (255, 255, 255))
                self.surface.blit(game_over_text, (self.WIDTH // 2 - game_over_text.get_width() // 2,
                                                   self.HEIGHT // 2 - game_over_text.get_height() // 2))
                pygame.display.flip()
                pygame.time.wait(1000)
                self.__init__()
                self.run()
                continue

            self.surface.fill((0, 0, 0))
            self.snake.handle_keys()
            self.snake.update()
            self.snake.draw()
            self.apple.draw(self.surface)
            self.check_collision()
            self.snake.eat(self.apple)
            pygame.display.flip()
            self.clock.tick(self.FPS)

        pygame.quit()
