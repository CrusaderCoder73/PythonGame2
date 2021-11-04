import pygame
import sys
from Crosshair import Crosshair
from Targets import Target
import random
class GameController:
    """GameController class that runs and manages the game"""
    def __init__(self):
        """Game Controller Constructor"""
        pygame.init()
        self.width = 850
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("Stars.png")
        pygame.mouse.set_visible(False)
    
    def run(self):
        """Run method that runs the game """

        #creates a new crosshair object
        crosshair = Crosshair("circle_dot.png")
        #creates a crosshair sprite group and adds a crosshair object to the group
        crosshair_group = pygame.sprite.Group()
        crosshair_group.add(crosshair)

        #creates a new target sprite group
        target_group = pygame.sprite.Group()
        #A for loop to iterate through the sprite group to create and add a new target in a random position to the screen
        for target in range(20):
            new_target = Target("new_bullet.png", random.randrange(9, self.width), random.randrange(0, self.height))
            target_group.add(new_target)
        
        #Game Loop
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    crosshair.shoot(crosshair, target_group)
            #allows the screen to update so images that move don't trail
            self.screen.fill((0, 0 ,0))
            #puts background image on the screen
            self.screen.blit(self.background,(0,0))

            #draws the targets and the crosshair to the screen
            target_group.draw(self.screen)
            crosshair_group.draw(self.screen)
            crosshair_group.update()
            
            #updates the display
            pygame.display.flip()
            #framerate
            self.clock.tick(60)
            