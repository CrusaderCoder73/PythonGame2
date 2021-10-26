import pygame
import sys
class GameController():
    """Game Controller Constructor"""
    def __init__(self):
        pygame.init()
        self.width = 400
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()