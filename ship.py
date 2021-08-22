import pygame

class Ship:
    # A class to manage the ship

    def __init__(self,ai_game):
        # Initialize ship and starting pos.
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start new ships at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)
        # self.y = float(self.rect.y)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        # self.moving_up = False

    def update(self):
        # Update the ships position based on the movement flag, update the ship x value
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # if self.moving_up :
        #     self.y -= self.settings.ship_speed
        # Update rect object from self.x
        self.rect.x = self.x
        # self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image,self.rect)