"""
Main module for the Snake game.

This module initializes the game and starts the main loop.
"""

import pygame
from game import Game


def main():
    """Main function that initializes and runs the game."""
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()


if __name__ == "__main__":
    main()
