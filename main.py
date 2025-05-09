import pygame
from constants import *

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

        # Update the display
        pygame.display.flip()

        # Set the frame rate
        framerate = clock.tick(60)

        dt = framerate / 1000.0
        


if __name__ == "__main__":
    main()