import circleshape
import pygame
from constants import *
import random

class Asteroid(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        # create 2 new asteroids
        velocity1 = self.velocity.rotate(random.uniform(20, 50))
        velocity2 = self.velocity.rotate(random.uniform(20, 50)*-1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = velocity2 * 1.2
        
        

