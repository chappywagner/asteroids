from circleshape import *

from constants import *

import random

class Asteroid(CircleShape):
    
    containers = ()

    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        #print('drawing circle')
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):
        self.position +=  self.velocity * dt
    
    def split(self):
        
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            # split the asteroid up
            split_angle = random.uniform(20,50)
            
            new_velocities = [self.velocity.rotate(split_angle),self.velocity.rotate(-split_angle)]

            new_radius = self.radius - ASTEROID_MIN_RADIUS

            for i in range(0,2):
                asteroid = Asteroid(self.position.x, self.position.y, new_radius)
                asteroid.velocity = new_velocities[i] * 1.2

