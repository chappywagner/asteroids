import pygame
from constants import *
from circleshape import *
from shot import *
class Player(CircleShape):

    containers = ()
    shot_timer = 0
    PLAYER_SHOT_COOLDOWN = .3
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
      
    def draw(self, screen):
        #print("drawing player")
        pygame.draw.polygon(screen,"white",self.triangle(),2)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def shoot(self):
        
        if self.shot_timer <=0:
            self.shot_timer = .3
            shot = Shot(self.position.x,self.position.y,SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED


    def update(self, dt):
        keys = pygame.key.get_pressed()

        # update the shot timer
        self.shot_timer -=dt

        if keys[pygame.K_a]:
            dt_inv = dt * -1
            self.rotate(dt_inv)
      
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_w]:
            #dt += 10
            self.move(dt)

        if keys[pygame.K_s]:
            #dt -=10
            self.move(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt