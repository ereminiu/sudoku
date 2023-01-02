import gen
import solver
import checkers
import sys 
import tools

for tt in range(1000):
    grid = gen.GridGenerator().get_grid()
    sol = solver.Solver(grid).get_solution()
    if not checkers.check_valid(sol):
        print('Failed')
        assert False