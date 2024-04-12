class Settings:
    """A class to keep track of all the settings in the game"""

    def __init__(self):
        """Initialize the game settings"""
        #Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #Ship Settings
        self.player_speed = 0.75