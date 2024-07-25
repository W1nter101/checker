from checkers.constants import *
from checkers.button import *
import main as m
import pygame, sys

pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont('arialblack',40)



def drawtext(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x,y))

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    pass

def option():
    pass

def menu():
	run = True
	pygame.display.set_caption("Main Menu")
	while run:
		screen.fill((52,78,91))
		MENU_MOUSE_POS = pygame.mouse.get_pos()
  
		MENU_TEXT = get_font(50).render("CHECKERS GAME", True, "#b68f40")

		MENU_RECT = MENU_TEXT.get_rect(center=(400, 150))
		PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 350), 
                    text_input="PLAY", font=get_font(30), base_color="#d7fcd4", hovering_color="Green")
		# OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(400, 400), 
        #                     text_input="OPTIONS", font=get_font(30), base_color="#d7fcd4", hovering_color="Green")
		QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(400, 550), 
                            text_input="QUIT", font=get_font(30), base_color="#d7fcd4", hovering_color="Green")
		screen.blit(MENU_TEXT, MENU_RECT)
		
		for button in [PLAY_BUTTON, QUIT_BUTTON]:
			button.changeColor(MENU_MOUSE_POS)
			button.update(screen)
            
            
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
					m.main()
				# if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
				# 	option()
				if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
					pygame.quit()
					sys.exit()	
		pygame.display.update()
	pygame.quit()
	sys.exit()

menu()