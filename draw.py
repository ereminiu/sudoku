import pygame as pg
from tools import cols

class Drawer:
    def __init__(self, screen):
        self.screen = screen
        self.fontsize = 30
        self.sx, self.sy = 150, 30
        self.d, self.N = 30, 9
        self.font = pg.font.Font(None, self.fontsize)
    
    def draw_text(self, text, x=0, y=0, color='red'):
        tx = self.font.render(text, True, cols[color])
        self.screen.blit(tx, (x, y))
        pg.display.flip()
    
    def fx(self, i=0):
        return self.sx + self.d * i
    
    def fy(self, i=0):
        return self.sy + self.d * i 
    
    def draw_tiles(self):
        for i in range(10):
            pg.draw.line(self.screen, cols['black'], (self.fx(i), self.sy), (self.fx(i), self.fy(self.N)), 1 + (i%3 == 0))
            pg.draw.line(self.screen, cols['black'], (self.sx, self.fy(i)), (self.fx(self.N), self.fy(i)), 1 + (i%3 == 0))
        
        pg.display.flip()
    
    def draw_grid(self, grid):
        for i in range(9):
            for j in range(9):
                val = grid[j][i]
                if val:
                    self.draw_text(str(val), self.fx(i) + self.fontsize//3, self.fy(j) + self.fontsize//5)

        pg.display.flip()

    def draw_diff(self, ans, empty):
        for i in range(9):
            for j in range(9):
                if empty[i][j]:
                    self.draw_text(str(ans[j][i]), self.fx(i) + self.fontsize//3, self.fy(j) + self.fontsize//5, color='green')
                
        pg.display.flip()
