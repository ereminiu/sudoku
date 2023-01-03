import random
import solver

class GridGenerator:
    def __init__(self):
        self.n = 9
        self.grid = [[0 for x in range(self.n)] for y in range(self.n)]
        self.init_grid()
        self.shuffle()
        #68 - for hard, 61 - medium, >= 46 - easy
        self.remove_cells(68) 
    
    def init_grid(self):
        self.grid = [[(3*i + i//3 + j) % 9 + 1 for i in range(self.n)] for j in range(self.n)]
    
    def transpos(self):
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    break
                self.grid[i][j], self.grid[j][i] = self.grid[j][i], self.grid[i][j]
    
    def swap_rows(self):
        d = random.randint(0, 2)
        x, y = 3*d + random.randint(0, 2), 3*d + random.randint(0, 2)

        while x == y:
            y = 3*d + random.randint(0, 2)
        
        self.grid[x], self.grid[y] = self.grid[y], self.grid[x]
    
    def swap_cols(self):
        self.transpos()
        self.swap_rows()
        self.transpos()
    
    def swap_box_h(self):
        x, y = 3*random.randint(0, 2), 3*random.randint(0, 2)

        while x == y:
            y = 3*random.randint(0, 2)
        
        for i in range(3):
            self.grid[x + i], self.grid[y + i] = self.grid[y + i], self.grid[x + i]

    def swap_box_v(self):
        self.transpos()
        self.swap_box_h()
        self.transpos()

    def shuffle(self):
        self.transpos()
        for it in range(40):
            idx = random.randint(0, 3)
            for rep in range(4):
                if idx == 0:
                    self.swap_rows()
                elif idx == 1:
                    self.swap_rows()
                elif idx == 2:
                    self.swap_box_h()
                else:
                    self.swap_box_v()
        for it in range(6):
            self.swap_rows()

    def remove_cells(self, emptycnt=60):

        def copy():
            table = [[0 for x in range(9)] for j in range(9)]
            for i in range(9):
                for j in range(9):
                    table[i][j] = self.grid[i][j]
            return table

        removed = 0
        while removed < emptycnt:
            i, j = random.randint(0, 8), random.randint(0, 8)
            val = self.grid[i][j]
            self.grid[i][j] = 0

            table = copy()

            if not solver.Solver(table).solve():
                self.grid[i][j] = val
            else:
                removed += 1
    
    def get_grid(self):
        return self.grid