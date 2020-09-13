# sept 13, 2020
# day 2 of my 30-day challenge to make one project daily

# move a box in a grid using the arrow keys

import pygame

pygame.init()
pygame.display.set_caption('move2d')
# screen settings
size = width, height = 800, 800
bg_color = 0, 0, 0
white = (220, 220, 220)
red = (220, 0, 0)
screen = pygame.display.set_mode(size)

margin = 10

class Grid:
	def __init__(self):
		self.size = (11, 11) # (width, height)
		self.cell_size = (width - 2*margin) // self.size[0] - 10

		self.cells = [["." for i in range(self.size[0])] 
							for j in range(self.size[1])]
		self.player_pos = [self.size[0]//2 + 1, self.size[0]//2 + 1]


	def move(self, d):
		self.player_pos[0] += d[0]
		self.player_pos[1] += d[1] 
		# don't allow player to leave grid
		if self.player_pos[0] > self.size[0]: self.player_pos[0] -= 1
		if self.player_pos[1] > self.size[1]: self.player_pos[1] -= 1
		if self.player_pos[0] < 1: self.player_pos[0] += 1
		if self.player_pos[1] < 1: self.player_pos[1] += 1


	def draw(self):
		c_size = self.cell_size

		x_size = self.size[0]
		y_size = self.size[1]

		# player
		pos = self.player_pos
		px, py = c_size*(pos[0]), c_size*(pos[1])
		p_width = self.cell_size 
		p_rect = ((px, py), (p_width, p_width))
		pygame.draw.rect(screen, red, p_rect)

		# vertical lines
		for i in range(self.size[0] + 1):
			c = c_size * (i+1)
			pygame.draw.line(screen, white, (c, c_size), \
				(c , c_size*(y_size+1)), 1)
		# horizontal lines
		for j in range(self.size[1] + 1):
			c = c_size * (j+1)
			pygame.draw.line(screen, white, (c_size, c), \
				(c_size*(x_size+1), c), 1)


grid = Grid()

def main():
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				run = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					grid.move((0, -1))
				if event.key == pygame.K_DOWN:
					grid.move((0, 1))
				if event.key == pygame.K_LEFT:
					grid.move((-1, 0))
				if event.key == pygame.K_RIGHT:
					grid.move((1, 0))

		screen.fill(bg_color)

		grid.draw()

		pygame.display.flip()

	pygame.quit()
	quit()

main()

