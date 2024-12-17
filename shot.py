import pygame
from circleshape import CircleShape
from constants import COLOR_WHITE, SHOT_RADIUS


class Shot(CircleShape):
    containers = ()

    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, COLOR_WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
