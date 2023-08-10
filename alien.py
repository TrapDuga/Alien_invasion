import pygame
from pygame.sprite import  Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen

    # Load the alien image and set its rect attribute
        self.default_size = (50,50)
        self.alien_ship = pygame.image.load('images/UFO-icon.bmp')
        self.image = pygame.transform.scale(self.alien_ship, self.default_size)
        self.rect = self.image.get_rect()
    # Start each alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.settings = ai_game.settings
        self.x = float(self.rect.x)
        

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
    
    def _update_aliens(self):
        self.aliens.update()

    def check_edges(self):
        # return true if alien is at the edge of the screen
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
