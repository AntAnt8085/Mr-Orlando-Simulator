import pygame

class Player():
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the image
        self.image = pygame.image.load("images/player.jpeg")
        self.rect = self.image.get_rect()

        #start the ship in the bottom middle of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #Moving Flag
        self.moving_right = False
        self.moving_left = False

        self.jumping = False

        self.y_gravity = .5
        self.jump_height = 20
        self.y_velocity = self.jump_height

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Updates the ship position based off of the moving flag"""
        if self.moving_right and self.rect.right <= self.screen_rect.right:
            self.x += self.settings.player_speed
        if self.moving_left and self.rect.left >= self.screen_rect.left:
            self.x -= self.settings.player_speed
        
        if self.jumping:
            self.y -= self.y_velocity
            self.y_velocity -= self.y_gravity
            if self.y_velocity < -self.jump_height:
                self.jumping = False
                self.y_velocity = self.jump_height
        else:
            pass
        
        #Update rect object from self x
        self.rect.x = self.x
        self.rect.y = self.y