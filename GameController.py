import pygame
import sys
from Crosshair import Crosshair
class GameController:
    """Game Controller Constructor"""
    def __init__(self):
        pygame.init()
        self.width = 850
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
    
    def run(self):
        """Run method that runs the game """
        crosshair = Crosshair(50, 50, 100, 100, (255, 255, 255))

        crosshair_group = pygame.sprite.Group()
        crosshair_group.add(crosshair)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            
            pygame.display.flip()
            crosshair_group.draw(self.screen)
            self.clock.tick(60)