# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        for updatable_sprite in updatable:
            updatable_sprite.update(dt)

        for updatable_drawable in drawable:
            updatable_drawable.draw(screen)

        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game Over!")
                return
            for shot in shots:
                if shot.collides(asteroid):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        tick = clock.tick(60)
        dt = tick / 1000


if __name__ == "__main__":
    main()
