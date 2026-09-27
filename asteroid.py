from circleshape import CircleShape
import pygame
from constants import *
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    
    def draw(self, screen) -> None:
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)
    
    def update(self, dt) -> None:
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            rand_angle = random.uniform(20,50)
            radius = self.radius - ASTEROID_MIN_RADIUS
            pos_vel = self.velocity.rotate(rand_angle)
            neg_vel = self.velocity.rotate(-1*rand_angle)
            asteroid1 = Asteroid(self.position.x, self.position.y, radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, radius)
            asteroid1.velocity = pos_vel * 1.2
            asteroid2.velocity = neg_vel * 1.2

