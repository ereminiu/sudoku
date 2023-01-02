import pygame as pg
from tools import cols
import tools
import draw
import gen
import checkers
import solver

pg.init()

screen = pg.display.set_mode((600, 400))
screen.fill(cols['white'])

#create drawer 
drawer = draw.Drawer(screen)

#draw game field
drawer.draw_tiles()

#write Aboba
drawer.draw_text('Press Space to show solution')

import sys

# sys.stdout = open('output.txt', 'w')

#generate random sudoku grid
grid = gen.GridGenerator().get_grid()

#find the empty cells
empty = [[not grid[i][j] for i in range(9)] for j in range(9)]

print(empty)

# print(grid)

#draw the game grid
drawer.draw_grid(grid)

#solve this puzzle!
sol = solver.Solver(grid).get_solution()

# print(sol)

#check grid is valid
if not checkers.check_valid(grid):
    print('generated not valid grid!!!')
    draw.draw_text(screen, 'generated not valid grid!!!', color='black')
    assert 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                drawer.draw_diff(sol, empty)