# elevator

"""
how it works:
the elevator could be moving or stationary
we have a queue
whenever a button is pressed, it gets added to the queue(if it's not already there),
then the elevator goes through the queue 
example:
- queue = [5,3,6,1], meaning 5 was added first, an 1 was added last
- so the elevator goes to floor 5, then floor 3, and so on, until it reaches floor 1
- if, while on the way to its current destination, the elvator passes through 
	a floor which is already in the queue, it stops at that floor, removes it from the queue,
	then continues

"""	

import pygame
import math

pygame.init()
pygame.display.set_caption('elevator')
# screen settings
size = width, height = 1280, 720
bg_color = 0, 0, 0
white =  (240, 240, 240)
green = (0, 100, 0)
screen = pygame.display.set_mode(size)

font = pygame.font.Font('freesansbold.ttf', 64) 


button_r = 60 # button radius
bl_width = 300 # building width
bl_width //= 2
mid = width//2 # middle of the screen

y = 50 # y coordinate of roof
floor_h = (height - y) // 6 # height of each floor


def draw_building(): # draw a 6-floor building
	ww = 3 # width of walls
	# draw the roof
	pygame.draw.line(screen, white, (mid-bl_width, y), (mid+bl_width , y), ww)
	# draw the two walls on the sides (left and right)
	pygame.draw.line(screen, white, (mid-bl_width, y), (mid-bl_width , height), ww)
	pygame.draw.line(screen, white, (mid+bl_width, y), (mid+bl_width , height), ww)

	# draw the floors (1-6)
	for i in range(6):
		fy = height - i * floor_h - ww # y coordinate of this floor
		pygame.draw.line(screen, white, (mid+bl_width, fy), \
						(mid-bl_width , fy), ww)	


class Button:
	def __init__(self, x, y, n):
		self.x, self.y = x, y
		self.n = n

	def is_on(self): # return True if mouse is over button
		mouse_pos = pygame.mouse.get_pos()
		mx = abs(mouse_pos[0] - self.x) # distance of mouse to self.x
		my = abs(mouse_pos[1] - self.y)
		if (mx**2 + my**2)**.5 <= button_r: # radius formula
			return True
		return False

	def draw(self): 
		if self.is_on():
			b_color = (200, 200, 200) # darken the button if mouse is on it 
		else: b_color = white # button color
		# circle shape
		pygame.draw.circle(screen, b_color, (self.x, self.y), button_r)
		# text
		x, y = self.x, self.y
		text = font.render(str(self.n), True, bg_color, b_color) 
		text_rect = text.get_rect() 
		text_rect.center = (x, y) 

		screen.blit(text, text_rect)

class Elevator: # six-floor elevator
	def __init__(self):
		# elevator shaft info
		self.floor = 0 # which floor the elevator shaft is on
		self.queue = [4, 6, 3, 1] # queue of floors
		self.dir = 0 # 1: shaft moving down, -1: moving up, 0: not moving
		self.prev = self.floor # previous floor that the elevator was on (prevents animation from breaking)

		self.x = mid # elevator shaft's x coordinate
		self.y = height - floor_h - 2 # elevator shaft's y coordinate
		self.col = (150, 150, 150) # shaft color
		self.w = 100 # shaft width
		self.speed = 2 # move speed

		# elevator buttons
		bx = button_r + 25 # button x
		by = 230 # y coordinate of topmost row
		bg = 2 * button_r + 10 # button gap
		left_col =  [Button(bx,    by+i*bg, 5 - 2*i) for i in range(3)] # list of buttons on the left column
		right_col = [Button(bx+bg, by+i*bg, 6 - 2*i) for i in range(3)] # list of buttons on the right column
		self.buttons = left_col + right_col

	def which_floor(self): # which floor the shaft is closest to
		bldg_h = height - y
		curr_floor = 6 - (self.y - y) // floor_h
		return curr_floor

	def stop(self, floor_n): 
		# stops the shaft when it reaches it's destination
		# this prevents the animation from looking wierd when 
		# the shaft goes up to a certain floor
		req_h = height - (floor_h)*floor_n
		if  req_h - 10 <= self.y <= req_h + 10:
			self.y = req_h
			self.floor = floor_n
			self.dir = 0

	def goto(self, floor_n): # start moving to floor n
		if self.floor < floor_n: self.dir = -1 # go up
		elif self.floor > floor_n: self.dir = 1 # go down
		else:
			# destination reached 
			self.stop(floor_n) # stops
			self.dir = 0
			self.queue.pop(0)

	def manager(self):
		self.floor = self.which_floor()
		if len(self.queue) > 0: 
			self.goto(self.queue[0])
		self.draw()

	def clicked(self):
		for b in self.buttons:
			if b.is_on(): 
				# b.pressed()
				self.queue.append(b.n)

	def draw_buttons(self):
		for b in self.buttons:
			b.draw()

	def draw(self):
		# draw buttons
		self.draw_buttons()
		# draw elevator shaft
		self.y += self.speed * self.dir
		pygame.draw.rect(screen, self.col, (self.x-self.w//2, self.y, self.w, floor_h))
		# draw building
		draw_building()


elevator = Elevator()


def main():
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				run = False
			if event.type == pygame.MOUSEBUTTONUP:
				elevator.clicked() 


		screen.fill(bg_color)

		elevator.manager()

		pygame.display.flip()

	pygame.quit()
	quit()

main()
