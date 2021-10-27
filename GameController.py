import pygame
import sys
from Crosshair import Crosshair
from Targets import Target
import random
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

        #crosshair
        crosshair = Crosshair("circle_dot.png")
        crosshair_group = pygame.sprite.Group()
        crosshair_group.add(crosshair)

        #targets
        target_group = pygame.sprite.Group()
        for target in range(20):
            new_target = Target("new_bullet.png", random.randrange(9, self.width), random.randrange(0, self.height))
            target_group.add(new_target)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    crosshair.shoot(crosshair, target_group)
            
            self.screen.fill((0, 0 ,0))
            self.screen.blit(self.background,(0,0))

            target_group.draw(self.screen)
            crosshair_group.draw(self.screen)
            crosshair_group.update()
            pygame.display.flip()
            self.clock.tick(60)
            