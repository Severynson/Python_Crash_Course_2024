class Settings:
    "A class to store all settings for Alien Invasion."

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings:
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.is_fullsceen = True
        # Ship settings:
        self.ship_speed = 1.5
        self.ship_limit = 3
        # Bullet settings:
        self.bullet_width = 12
        self.bullet_height = 32
        self.bullet_color = (255, 165, 0)
        self.bullets_allowed = 5
        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        # Ship settings:
        self.ship_speed = 1.5
        # Bullet settings:
        self.bullet_speed = 3
        # Alien settings
        self.fleet_drop_speed = 50
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.fleet_drop_speed *= self.speedup_scale
