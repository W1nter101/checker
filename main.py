# Assets: https://techwithtim.net/wp-content/uploads/2020/09/assets.zip
import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, WHITE
from checkers.game import Game
from minimax.algorithm import minimax
import sys
# import thongbao as tb
from checkers.button import *
import menu as s
import importlib
FPS = 60
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont('arialblack',40)
def drawtext(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)
def thongbao(winner):
    run = True
    while run:
        screen.fill((52,78,91))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        game_instant = Game(WIN)
        #winner = game_instant.winner()
        if(winner== "WHITE"):
            MENU_TEXT = get_font(50).render("You Lose!", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(400, 150))
            screen.blit(MENU_TEXT, MENU_RECT)
        if(winner=="RED"):
            MENU_TEXT = get_font(50).render("You Win!", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(400, 150))
            screen.blit(MENU_TEXT, MENU_RECT)
        elif(winner=="DRAW"):
            MENU_TEXT = get_font(50).render("Draw!", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(400, 150))   
            screen.blit(MENU_TEXT, MENU_RECT)   
        RETURN_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 350), 
        text_input="RETURN", font=get_font(30), base_color="#d7fcd4", hovering_color="Green")
        for button in [RETURN_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN_BUTTON.checkForInput(MENU_MOUSE_POS):
                    s.menu()
                # if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                # 	option()
                    
        pygame.display.update()

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 3, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            thongbao(game.winner())
            break
            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()
    sys.exit()

main()
