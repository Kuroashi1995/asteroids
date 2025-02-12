from constants import *
import pygame

def main():
    pygame.init()
    print(pygame.get_init())
    print("Starting asteroids!")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        print(f"Game running in {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        pygame.Surface.fill(screen, (0,0,0))
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        print(dt)

if __name__ == "__main__":
    main()
