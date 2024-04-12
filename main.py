import sys
import pygame
from settings import Settings
from player import Player

class Invasion:
    """This clas manges the behavior of the game"""
    def __init__(self):
        """Initializes the game and creates resources"""
        pygame.init()
        self.settings = Settings()

        pygame.display.set_caption("Mr. Orlando Simulator")
        icon = pygame.image.load("images\icon.png") 
        pygame.display.set_icon(icon)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        
        self.player = Player(self)

        self.bg_color = self.settings.bg_color
    
    def run_game(self):
        """start the main game loop"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        #Watch for keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN: #Checks for keys pressed down
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP: #Checks for keys released
                self._check_keyup_events(event)
            
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.player.jumping  = True
        elif event.key == pygame.K_q:
            sys.exit()  

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False

    def _update_screen(self):
        #redraw the screen
        self.screen.fill(self.bg_color)
        self.player.update()
        self.player.blitme()
        self.clock.tick(60)
        #make the screen visible
        pygame.display.flip()

if __name__ == "__main__":
    #Make our game instance
    ai = Invasion()
    ai.run_game()