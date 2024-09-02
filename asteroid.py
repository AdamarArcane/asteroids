from circleshape import *
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        self.velocity = pygame.Vector2(0,1)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255),(self.position.x,self.position.y),self.radius,2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self, dt):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            new_vect_1 = self.velocity.rotate(random_angle)
            new_vect_2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid_1.velocity = new_vect_1 * 1.2
            new_asteroid_2.velocity = new_vect_2 * 1.2
