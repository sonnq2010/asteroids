import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):
    containers = ()

    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self._shoot_cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, COLOR_WHITE, self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        vector_move = pygame.Vector2(0, 1)
        vector_move = vector_move.rotate(self.rotation)
        vector_move *= PLAYER_SPEED * dt
        self.position += vector_move

    def shoot(self):
        if self._shoot_cooldown > 0:
            return

        self._shoot_cooldown = PLAYER_SHOOT_COOLDOWN
        velocity = pygame.Vector2(0, 1).rotate(self.rotation)
        velocity *= PLAYER_SHOT_SPEED
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = velocity

    def update(self, dt):
        self._shoot_cooldown -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        elif keys[pygame.K_d]:
            self.rotate(dt)
        elif keys[pygame.K_w]:
            self.move(dt)
        elif keys[pygame.K_s]:
            self.move(-dt)
        elif keys[pygame.K_SPACE]:
            self.shoot()
