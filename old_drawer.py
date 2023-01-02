import pygame as pg
from tools import cols

fontsize = 30
sx, sy = 150, 30
d, N = 30, 9

def draw_text(screen, text, x=0, y=0, color='red'):
    font = pg.font.Font(None, fontsize)
    tx = font.render(text, True, cols[color])
    screen.blit(tx, (x, y))
    pg.display.flip()

def draw_tiles(screen):
    for i in range(10):
        pg.draw.line(screen, cols['black'], (sx + d*i, sy), (sx + d*i, sy + N*d), 1 + (i%3 == 0))
        pg.draw.line(screen, cols['black'], (sx, sy + d*i), (sx + N*d, sy + d*i), 1 + (i%3 == 0))
    
    pg.display.flip()

def draw_grid(screen, grid):
    for i in range(9):
        for j in range(9):
            val = grid[j][i]
            if val:
                draw_text(screen, str(val), sx + d*i + fontsize//3, sy + d*j + fontsize//5)

    pg.display.flip()

def draw_diff(screen, grid, ans):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == ans[i][j]:
                draw_text(screen, str(ans[i][j]), sx + d*i + fontsize//3, sy + d*j + fontsize//5)
            else:
                draw_text(screen, str(ans[i][j]), sx + d*i + fontsize//3, sy + d*j + fontsize//5, color='green')
    
    pg.display.flip()