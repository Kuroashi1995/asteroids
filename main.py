from constants import *
import pygame

def main():
    pygame.init()
    print(pygame.get_init())
    print("Starting asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        print(f"Game running in {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()
if __name__ == "__main__":
    main()
