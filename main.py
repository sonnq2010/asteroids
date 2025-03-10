# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    drawable_group = pygame.sprite.Group()
    updatable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Shot.containers = (shot_group, updatable_group, drawable_group)
    Asteroid.containers = (drawable_group, updatable_group, asteroid_group)

    AsteroidField.containers = (updatable_group)
    asteroid_field = AsteroidField()

    Player.containers = (drawable_group, updatable_group)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for object in updatable_group:
            object.update(dt)

        for asteroid in asteroid_group:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()

            for shot in shot_group:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()

        screen.fill(COLOR_BLACK)

        for object in drawable_group:
            object.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
