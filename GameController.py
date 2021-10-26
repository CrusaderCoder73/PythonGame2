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
        self.background = pygame.image.load("Stars.png")
        pygame.mouse.set_visible(False)
    
    def run(self):
        """Run method that runs the game """

        crosshair = Crosshair("circle_dot.png")
        crosshair_group = pygame.sprite.Group()
        crosshair_group.add(crosshair)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            
            pygame.display.flip()
            self.screen.blit(self.background,(0,0))
            crosshair_group.draw(self.screen)
            crosshair_group.update()
            self.clock.tick(60)