from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n = 9
    
    #probable values for cell (i, j)
    cand = [[set(list(range(1, 10))) for x in range(n)] for y in range(n)]

    #rows[i] - values used in i-th row, cols[i] - values used in i-th column
    #blocks[i, j] - values used in block (i, j)
    rows = [set() for x in range(n)]
    cols = [set() for x in range(n)]
    blocks = [[set() for x in range(3)] for y in range(3)]
    ans = [[0 for x in range(n)] for y in range(n)]

    #init rows, cols, blocks
    for i in range(n):
        for j in range(n):
            val = grid[i][j]
            if not val:
                continue

            ans[i][j] = val
            rows[i].add(val)
            cols[j].add(val)
            blocks[i//3][j//3].add(val)
    
    def check_row(i, val):
        cnt = 0
        for k in range(n):
            if ans[i][k]:
                continue
            if not (val in cols[k] or val in blocks[i//3][k//3]):
                cnt += 1
        return cnt == 1

    def check_col(i, val):
        cnt = 0
        for k in range(n):
            if ans[k][i]:
                continue
            if not (val in rows[k] or val in blocks[k//3][i//3]):
                cnt += 1
        return cnt == 1

    def check_block(i, j, val):
        cnt = 0
        for ib in range(i - i%3, i - i%3 +3):
            for jb in range(j - j%3, j - j%3 +3):
                if ans[ib][jb]:
                    continue
                if not (val in rows[ib] or val in cols[jb]):
                    cnt += 1
        return cnt == 1

    found = 0

    def go():
        for i in range(n):
            for j in range(n):
                if ans[i][j]:
                    continue

                for val in range(1, 10):
                    if val in rows[i] or val in cols[j] or val in blocks[i//3][j//3]:
                        continue

                    if check_row(i, val) or check_col(j, val) or check_block(i, j, val):
                        # print(check_row(i, val), check_col(j, val), check_block(i, j, val))
                        ans[i][j] = val
                        cols[j].add(val)
                        rows[i].add(val)
                        blocks[i//3][j//3].add(val)
                        nonlocal found
                        found += 1
                        break
    
    for tt in range(20):
        go()

    print(found)

    return ans