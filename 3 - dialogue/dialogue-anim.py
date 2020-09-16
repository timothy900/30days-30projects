# day 4*
# text animation- show the words overtime(like pokemon and other JRPGs)
# i missed 2 days so it should be day 6 now but yea

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
		self.interval = 4 # draw the next letter every 4 frames
		self.n = 1 # frame number
		self.text = txt
		self.len_txt = len(txt)
		self.char_n = 0 # which character to draw (index if str)
		self.line = 0 # which line in the dialogue
		self.outputs = [""] # text that is outputted

	def draw(self): 
		x, y = margin, margin
		w, h = width - 2*margin, 115
		col = (255, 255, 255)

		out_text = font.render(self.output, True, bg_color, col) 
		out_text_rect = out_text.get_rect() 
		out_text_rect = (x + 30, y + 20) 

		pygame.draw.rect(screen, col, (x, y, w, h))
		screen.blit(out_text, out_text_rect) 

		# deal with changing the letter
		self.char_n = self.n//self.interval
		self.n += 1 if self.char_n <= self.len_txt else 0
		self.output = self.text[0:self.char_n]
		if self.output[-1] == "`": pass # new line


# use ` to indicate new line
dialogue = Dialogue("There's something so refreshing about `Michelangeli's Chopin.")


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


