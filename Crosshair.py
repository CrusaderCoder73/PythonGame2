import pygame, sys
class Crosshair(pygame.sprite.Sprite):
    """Crosshair class that creates an image that follows the players mouse
    if the player shoots a target the target gets deleted or removed"""

    def __init__(self, picture_path):
        """Crosshair constructor"""
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.gunshot = pygame.mixer.Sound("laser2.wav")
    def shoot(self, crosshair_group, target_group):
        """A shoot method that deletes a target sprite and plays a sound effect"""
        self.gunshot.play()
        pygame.sprite.spritecollide(crosshair_group, target_group, True)

    def update(self):
        """Overriden Pygame Update method that makes the crosshair follow the mouse"""
        self.rect.center = pygame.mouse.get_pos()