# calculator with pygame
# features:
# adding
# subtracting
# multiplying
# dividing
# floating point numbers


import pygame

pygame.init()
pygame.display.set_caption('calculator')
# screen settings
size = width, height = 600, 800
bg_color = 0, 0, 0
white = (220, 220, 220)
screen = pygame.display.set_mode(size)

font = pygame.font.Font('freesansbold.ttf', 64) 


class Button:
	def __init__(self, pos, size, text):
		self.pos = pos
		self.size = size 
		self.text = text

	# return true if mouse is over the button
	def isOn(self):
		m_pos = pygame.mouse.get_pos()
		x, y = m_pos[0], m_pos[1]

		if self.pos[0] <= x <= self.pos[0] + self.size[0]:
			if self.pos[1] <=  y <= self.pos[1] + self.size[1]:
				return True
		return False

	# draw the button
	def draw(self, canvas):
		# header
		x, y = self.pos[0], self.pos[1]
		w, h = self.size[0], self.size[1]
		
		# reset button
		if self.isOn(): col = (200, 200, 200)
		else: col = (255, 255, 255)

		button_text = font.render(self.text, True, bg_color, col) 
		button_text_rect = button_text.get_rect() 
		button_text_rect.center = (x + (w // 2), y + (h // 2)) 

		pygame.draw.rect(screen, col, (x, y, w, h))
		screen.blit(button_text, button_text_rect) 


	def pressed(self, calc):
		if self.isOn():
			# if last op was not a number and an op(e.g. +, -) wasnt pressed yet
			if self.text not in "0123456789":
				if len(calc.ops) != 2:
					# clear output and put operators in the list 
					calc.ops.append(calc.output)
					calc.ops.append(self.text)
			calc.output += self.text
			# if equals was pressed
			if self.text == "=" and len(calc.ops) == 2:
				# evaluate the expression
				calc.ops.append(calc.output[1+len(calc.ops[0]):-1])
				calc.eval()
			print(calc.ops)
			print(calc.output)


class Calculator:
	def __init__(self):
		# self.ans = None
		self.ops = []
		self.nums = []
		# the 3x3 num pad
		for i in range(3):
			self.nums.append([
				Button((30+120*i, 200+120*j), (115, 115), str(i+1 + (3*j))) 
				for j in range(3)])
		# the zero button at the bottom
		self.nums.append([Button((30+120*i, 560), (115, 115), "0")])
		# the 4 operations (add, subtract, multiply, divide)
		self.op_buttons = [
			Button((30+360, 200), (115, 115), "+"),
			Button((30+360, 200+120*1), (115, 115), "-"),
			Button((30+360, 200+120*2), (115, 115), "x"),
			Button((30+360, 200+120*3), (115, 115), "/"),
			Button((30, 200+120*3), (235, 115), "=")
			]
		# the output space
		self.output = ""

	def eval(self):
		n1, n2 = float(self.ops[0]), float(self.ops[2])
		operator = self.ops[1]
		if operator == "+": result = n1 + n2
		elif operator == "-": result = n1 - n2
		elif operator == "*": result = n1 * n2
		elif operator == "/": result = n1 / n2
		# self.ans = result 
		self.output = str(result)
		self.ops = [] # reset list of operations

	def c(self):
		self.ans = None

	def inps(self):
		for row in self.nums:
			for b in row:
				b.pressed(self)
		for b in self.op_buttons:
			b.pressed(self)

	def draw(self):
		# output
		self.draw_output()
		# buttons (nums)
		for row in self.nums:
			for b in row: 
				b.draw(screen)
		# buttoms (operators)
		for b in self.op_buttons: b.draw(screen)

	def draw_output(self):
		x, y = 20, 20
		w, h = 500, 115
		col = (255, 255, 255)

		out_text = font.render(self.output, True, bg_color, col) 
		out_text_rect = out_text.get_rect() 
		out_text_rect = (x + 30, y + 30) 

		pygame.draw.rect(screen, col, (x, y, w, h))
		screen.blit(out_text, out_text_rect) 


calc = Calculator()


def main():
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				run = False
			if event.type == pygame.MOUSEBUTTONUP:
				calc.inps()

		screen.fill(bg_color)

		calc.draw()
		pygame.display.flip()

	pygame.quit()
	quit()

main()
