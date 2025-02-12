from constants import *
import pygame
from player import *

def main():
    pygame.init()
    print(pygame.get_init())
    print("Starting asteroids!")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        print(f"Game running in {SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        dt = clock.tick(60) / 1000
        pygame.Surface.fill(screen, (0,0,0))
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        print(dt)

if __name__ == "__main__":
    main()
