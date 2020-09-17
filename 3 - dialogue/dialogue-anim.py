# day 4*
# text animation- show the words overtime(like pokemon and other JRPGs)
# i missed 3 days so it should be day 7 now but yea

import time
import pygame

pygame.init()
pygame.display.set_caption('dialogue')
# screen settings
size = width, height = 800, 800
bg_color = 0, 0, 0
white = (220, 220, 220)
red = (220, 0, 0)
screen = pygame.display.set_mode(size)

margin = 30

font = pygame.font.SysFont('tahoma', 32) 


class Dialogue:
	def __init__(self, txt):
		self.interval = 2 # draw the next character every 2 frames
		self.n = 1 # frame number
		self.text = txt
		self.len_txt = len(txt)
		self.char_n = 0 # which character to draw (index if str)
		self.line = 0 # which line in the dialogue
		self.outputs = [""] # text that is outputted

	# draw everything
	def draw(self): 
		x, y = margin, margin
		w, h = width - 2*margin, 20 + 50*len(self.outputs)
		col = (255, 255, 255)

		pygame.draw.rect(screen, col, (x, y, w, h))
		# draw all the lines in the outputs
		for i, line in enumerate(self.outputs):
			out_text = font.render(line, True, bg_color, col) 

			out_text_rect = (x + 30, (y + 20)*(i+1) )

			screen.blit(out_text, out_text_rect) 

		self.update()

	def update(self):
		# deal with changing the letter
		self.char_n = self.n//self.interval
		self.n += 1 if self.char_n <= self.len_txt else 0
		self.outputs[self.line] = self.text[0:self.char_n]

		# deal with new lines (dirtiest code i've ever seen)
		if self.outputs[0]:
			if self.outputs[self.line][-1] == "`": 
				self.outputs[self.line] = self.outputs[self.line][:-1] # remove the ` symbol
				self.n = self.interval  # this prevents the code from going in this if statement more than once
										# (because it checks self.outputs every time. this line only makes it check once)
				self.text = self.text[self.char_n:] # remove the previous text which is already in self.outputs
				self.outputs.append("") # add a new line to the outputs
				self.line += 1 


# use ` to indicate new line
dialogue = Dialogue("There's something so refreshing about `Michelangeli's Chopin. It doesn't have `the same warmth I've become accustomed `to hearing, but it is so clear, and the `ideas are so well articulated and the `phrases so well formed. There is `something very pure and not self-indulgent `in it.")


def main():
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				run = False

		screen.fill(bg_color)

		dialogue.draw()

		pygame.display.flip()

	pygame.quit()
	quit()

main()


