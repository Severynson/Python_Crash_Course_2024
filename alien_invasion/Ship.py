import pygame

UA_SPACESHIP_SIZE = (220, 240)
UPA_SPACESHIP_SIZE = (150, 240)
DEFEATED_SPACESHIP_SIZE = (220, 200)
GRAVE_SIZE = (200, 200)

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Load the ship image and get its rect.
        self.update_skin()
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)
        # Movement flags, start with a ship that is not moving.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update_skin(self, ships_left=3):
            "Updates the ship's skin depending on how many ships left."
            if ships_left >= 3:
                self.image = pygame.image.load("alien_invasion/images/ua_spaceship.bmp")
                self.image = pygame.transform.scale(self.image, UA_SPACESHIP_SIZE)
            elif ships_left == 2:
                self.image = pygame.image.load("alien_invasion/images/upa_spaceship.bmp")
                self.image = pygame.transform.scale(self.image, UPA_SPACESHIP_SIZE)
            elif ships_left == 1:
                self.image = pygame.image.load("alien_invasion/images/defeated_spaceship.bmp")
                self.image = pygame.transform.scale(self.image, DEFEATED_SPACESHIP_SIZE)
            else:
                self.image = pygame.image.load("alien_invasion/images/grave.bmp")
                self.image = pygame.transform.scale(self.image, GRAVE_SIZE)
            
            # Update the rect attribute to match the new size of the image
            self.rect = self.image.get_rect()
            
            # Calculate the center position based on the screen size
            screen_rect = self.screen.get_rect()
            self.rect.center = screen_rect.center