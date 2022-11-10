# final project for 2022 Spring Randomness and Computation
# Joanne Lee & Matt Ma
# slide_puzzle_interface.py written by Joanne Lee

import pygame
pygame.init()
from math import pi
from puzzle import *

# define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
WHEAT = (245, 222, 179)
TAN =   (210, 180, 140) # darker, between tiles
BROWN = (242,233,222) # tile
DIRT =  (155, 118,  83) # even darker, text color
BLANCHELALMOND = (255,235,205) # looks too flesh-colored
LINEN = (250,240,230) # same problem as above

# define color schemes
brown_color_scheme = {'background': BROWN, 'font': DIRT, 'tile': WHEAT, 'border': TAN, 'button':(235, 212, 169)}
red_color_scheme = {'background':(255,0,0),'font':(178,34,34),'tile':(250,128,114),'border':(255,0,0)}
orange_color_scheme = {'background':(255,140,0),'font':(255,225,60),'tile':(255,165,0),'border':(255,127,80)}
yellow_color_scheme = {'background':(255,255,153),'font':(51,51,0),'tile':(255,255,224),'border':(255,255,153)}
green_color_scheme = {'background':(107,142,35),'font':(0,100,0),'tile':(153,178,133),'border':(85,107,47)}
blue_color_scheme = {'background':(135,206,250),'font':WHITE,'tile':(65,105,225),'border':(0,191,255)}
purple_color_scheme = {'background':(147,112,219),'font':(75,0,130),'tile':(216,191,216),'border':(138,43,226)}

color_scheme = blue_color_scheme
background_col = color_scheme['background']
font_color = color_scheme['font']
tile_color = color_scheme['tile']
border_color = color_scheme['border']

# set the dimensions of buttons and tiles and interface
cell_size = 153

button_width = int(cell_size * 2)
button_height = int(cell_size * 0.6)
border_width = int(cell_size / 15)

font_size = int(cell_size / 3)
font = pygame.font.Font(None, font_size)

size = [cell_size * 4, cell_size * 5]
screen = pygame.display.set_mode(size)

# initialize puzzle and scramble it
puzzle = Number_Slide_Puzzle()
number_of_scrambles = int(32/0.6)
puzzle.scramble(number_of_scrambles)

# translating mouse click positions to interface positions
def pos2cell(pos):
    (row, col) = pos
    return (row // cell_size, col // cell_size)

def cell2pos(cell_coordinates):
    (cell_row, cell_col) = cell_coordinates
    return (cell_row * cell_size, cell_col * cell_size)

def pressedNewGameButton(pos):
    (row, col) = pos
    return (row > 4 * cell_size + (cell_size - button_height)/2 \
    and row < 5 * cell_size - (cell_size - button_height)/2 \
    and col > cell_size + (cell_size - button_width)/2 \
    and col < 3 * cell_size -  (cell_size - button_width)/2)



# loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

num_scrambles = 0
while not done:

    # limits the while loop to a max of num_loops times per second.
    # leave this out and we will use all CPU we can.
    num_loops = 30
    clock.tick(num_loops)

    if not num_scrambles == 0:
        puzzle.scramble(1)
        num_scrambles -= 1

    for event in pygame.event.get(): # user did something
        if event.type == pygame.QUIT: # if user clicked close
            done=True # flag that we are done so we exit this loop

        if event.type == pygame.MOUSEBUTTONDOWN:
            (mouse_col, mouse_row) = pygame.mouse.get_pos()
            pos = (mouse_row, mouse_col)
            if pressedNewGameButton(pos):
                num_scrambles = number_of_scrambles
            elif not puzzle.is_solved():
                cell_pos = pos2cell(pos)
                puzzle.slide(cell_pos)

    # clear the screen and set the screen background
    screen.fill(background_col)
    pygame.draw.rect(screen, border_color, [0, 0, cell_size * 4, cell_size * 4])

    # draw the board
    for i in range(4):
        for j in range(4):
            number = puzzle.board[i][j]
            if number != 0:
                top = int(cell_size * i + border_width / 2)
                left = int(cell_size * j + border_width / 2)
                box_size = cell_size - border_width
                pygame.draw.rect(screen, tile_color, [left, top, box_size, box_size], border_radius=10)
                text_image = font.render(str(number), True, font_color)
                col_adjustment = cell_size/17
                if number >= 10:
                    col_adjustment = 0
                text_row = top + cell_size/2 - font_size/2
                text_col = left + cell_size/2 - font_size/2 + col_adjustment
                screen.blit(text_image, (text_col, text_row))

    # draw 'Scramble Board' button
    button_left = cell_size + cell_size - button_width/2
    button_top = 4 * cell_size + (cell_size - button_height)/2
    pygame.draw.rect(screen, tile_color, [button_left, button_top, button_width, button_height], border_radius=10)

    button_txt = font.render("Scramble Board", True, font_color)
    text_row = button_top + button_height/2 - font_size/2 + 10
    text_col = button_left + 16

    screen.blit(button_txt, (text_col, text_row))

    # set name of interface window
    if puzzle.is_solved():
        pygame.display.set_caption("Puzzle Solved!!!")
    else:
        pygame.display.set_caption("4x4 Slide Puzzle")

    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
