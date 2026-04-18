import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    start_game = pygame.init() # Initialize all imported pygame modules
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    asteroid_field = AsteroidField()
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

        for asteroid in asteroids:
            if (player.collides_with(asteroid) == True):
                log_event("player_hit")
                print(f"Game Over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots:
                if (shot.collides_with(asteroid) == True):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.kill()

        pygame.display.flip() # Update the full display surface to reflect all drawing operations
        dt = clock.tick(60) / 1000 # Limit the game loop to 60 FPS and compute delta time (seconds since last frame)

if __name__ == "__main__":
    main()
