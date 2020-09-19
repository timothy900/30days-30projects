# day something idek anymore i missed too many days at this point
#
# osu!taiko copy
# time taken to make < 1 hour
# how to play: press space when a green circle goes on the white circle

"""
there is a bug where the circles clip out for a fram or two when one gets deleted, 
it's probably just because the code has to loop through
all the circles when drawing, and it's a slow method. idk how to fix right now
"""

import pygame
import random

pygame.init()
pygame.display.set_caption('taiko')
# screen settings
size = width, height = 800, 800
bg_color = 0, 0, 0
white = (220, 220, 220)
green = (0, 100, 0)
screen = pygame.display.set_mode(size)

drum_r = 35

font = pygame.font.Font('freesansbold.ttf', 64) 


class Drum:
	def __init__(self):
		self.x = width # x position
		self.y = height // 2 # y position
		self.onscreen = True # is visible on screen

	def draw(self):
		pygame.draw.circle(screen, green, (int(self.x), self.y), drum_r)

	def is_onscreen(self):
		if self.x + 2*drum_r + 10 < 0:
			return False
		return True


class Taiko:
	def __init__(self):
		self.score = 0 
		self.drums = [] # list of drums on screen
		self.speed = 5 # how many pixels the drums should move each frame
		self.max_interval = 150 # maximum amount of frames to wait for next drum
		self.min_interval = 20
		self.frame = 0 # frame number
		self.x = 170 # x position of target
		self.y = height // 2 # y position of target

	def game_manager(self):
		self.frame += 1
		if self.frame >= random.randint(self.min_interval, self.max_interval):
			self.frame = 0
			new_drum = Drum()
			self.drums.append(new_drum)

	def check_inps(self): # runs when player press spacebar
		# check each drum if close enough to target
		gap = 2 * drum_r * .3
		max_x = self.x + gap # gap is a small margin
		min_x = self.x - gap
		for d in self.drums:
			if min_x <= d.x <= max_x: 		
				self.drums.pop( self.drums.index(d) ) # remove d from list of drums
				del d # delete d
				self.score += 1
				break # no need to check the other drums

	def draw(self):
		# draw target
		pygame.draw.circle(screen, white, (int(self.x), self.y), drum_r)

		# draw each drum
		for d in self.drums:
			# check if drum is onscreen
			if not d.is_onscreen():		
				self.drums.pop( self.drums.index(d) ) # remove d from list of drums
				del d # delete d
				self.score -= 1 # subtract score
				break

			d.x -= self.speed
			d.draw()

		# draw score
		x, y = width//2, 250 # x, y coordinate of score
		score_text = font.render(str(self.score), True, white, bg_color) 
		score_text_rect = score_text.get_rect() 
		score_text_rect.center = (x, y) 

		screen.blit(score_text, score_text_rect) 



game = Taiko()

def main():
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					game.check_inps()

		screen.fill(bg_color)

		game.draw()
		game.game_manager()

		pygame.display.flip()

	pygame.quit()
	quit()

main()
