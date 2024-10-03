import pygame
from constants import * 
from player import *
from asteroid import *
from asteroidfield import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")



	# create clock variable
	clock = pygame.time.Clock()

	# create delta variable
	dt = 0

	# create some groups
	group_updatable = pygame.sprite.Group()

	group_drawable = pygame.sprite.Group()

	group_asteroids = pygame.sprite.Group()

	group_shots = pygame.sprite.Group()

	# add the Player class to these groups
	Player.containers = (group_updatable,group_drawable)

	Asteroid.containers = (group_asteroids, group_updatable, group_drawable)

	AsteroidField.containers = (group_updatable)
	
	# make the shots basically small asteroids, so they are 
	Shot.containers = (group_shots, group_updatable,group_drawable)

	# instantiate the player
	player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
	
	field = AsteroidField()

	while 1:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			
		screen.fill(color="black")

		# update everything in the updateable group
		for g in group_updatable:
			g.update(dt)

		# update the drawable group items
		for g in group_drawable:
			g.draw(screen)

		for asteroid in group_asteroids:

			
			if asteroid.is_colliding(player):
				print('Game over!')
				exit()

			for shot in group_shots:
				if asteroid.is_colliding(shot):
					asteroid.split()
					shot.kill()


		dt = clock.tick(60)/1000
		
		pygame.display.flip()



	

if __name__ == "__main__":
	main()

