import sys
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
import pygame
from player import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
bullets = pygame.sprite.Group()

def main():
    pygame.init()
    print("Starting asteroids!")
    clock = pygame.time.Clock()
    dt = 0
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (bullets, updatable, drawable)
    asteroid_field = AsteroidField()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        pygame.Surface.fill(screen, (0,0,0))
        updatable.update(dt)
        for object in asteroids:
            if object.check_collision(player):
                print("Game over!")
                sys.exit(0)
            for bullet in bullets:
                if object.check_collision(bullet):
                    bullet.kill()
                    object.split()


        for image in drawable:
            image.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()
