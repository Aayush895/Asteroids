import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

def main():
    start_game = pygame.init() # Initialize all imported pygame modules
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while(True):
        log_state()
        for event in pygame.event.get():
            # Handle window close event (QUIT) by iterating over the pygame event queue
            if event.type == pygame.QUIT:
                return
        screen.fill("black") # Will fill the screen surface with black color

        for item in drawable:
            item.draw(screen) # Draw the player onto the screen surface
        updatable.update(dt)
        pygame.display.flip() # Update the full display surface to reflect all drawing operations
        dt = clock.tick(60) / 1000 # Limit the game loop to 60 FPS and compute delta time (seconds since last frame)

if __name__ == "__main__":
    main()
