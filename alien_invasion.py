import sys
import pygame
from settings import Settings

class AlienInvasion:
    #""Class to manage the game assets and behavior""
    
    def __init__(self):
        #""Initilize game and create resouces""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        #Set the backround color
        self.bg_color = (230,230,230)
        
    def run_game(self):
    #""Start main loop for the game""
        while True:
        #Watch for keyboard and mouse input
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        
        #Redraw screen during each pass through the loop detecing input
        self.screen.fill(self.settings.bg_color)
        
        #Make recent screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
    

                