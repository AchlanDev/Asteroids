import pygame
from constants import *
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField

# Asteroids Game
# This is a simple implementation of the classic Asteroids game using Pygame.
def main():

    # Initialize the game
    pygame.init()

    clock = pygame.time.Clock()

    dt = 0

    # Set the screen dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Terminal output
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    # Set player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Set asteroid field
    asteroid_field = AsteroidField()

    # Game Loop
    # Game will run until the user quits
    # The game loop will handle events, update the game state, and render the screen
    while True:

        # Pygame quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Quitting...")
                pygame.quit()
                return

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw the player
        for sprite in drawable:
            sprite.draw(screen)

        # Update the player
        updatable.update(dt)

        # Update the display
        pygame.display.flip()

        # Set the frame rate
        framerate = clock.tick(60)

        dt = framerate / 1000.0
        


if __name__ == "__main__":
    main()