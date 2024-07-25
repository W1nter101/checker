import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax
from checkers.button import *
import menu
import sys
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(None,40)
def drawtext(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x,y))
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)
def ketqua(winner):
    run = True
    while run:
        screen.fill((52,78,91))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(50).render("chiến thắng", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 150))
        RETURN_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 350), 
                    text_input="RETURN", font=get_font(30), base_color="#d7fcd4", hovering_color="Green")
        screen.blit(MENU_TEXT, MENU_RECT)
        for button in [RETURN_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if RETURN_BUTTON.checkForInput(MENU_MOUSE_POS):
                        menu.menu()
				# if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
				# 	option()
				
        pygame.display.update()
