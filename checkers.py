from typing import List

def check_valid(board: List[List[int]]) -> bool:
    n = 9
    blocks = [[set() for x in range(3)] for y in range(3)]
    rows = [set() for x in range(n)]
    cols = [set() for x in range(n)]
    for i in range(n):
        for j in range(n):
            bi, bj = i//3, j//3
            val = board[i][j]
            if not val:
                continue
            if val in blocks[bi][bj] or val in rows[i] or val in cols[j]:
                print(f'blocks = {blocks}')
                print(f'rows = {rows}')
                print(f'cols = {cols}')
                print(f'break at {i}, {j}')
                return False
            blocks[bi][bj].add(val)
            rows[i].add(val)
            cols[j].add(val)
    return True