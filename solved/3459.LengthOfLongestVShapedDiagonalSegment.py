from typing import List
from functools import cache

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        DIRS = ((-1, -1), (+1, -1), (+1, +1), (-1, +1))

        @cache
        def go(x, y, last, dir, turn):
            if not (0 <= x < COLS): return 0
            if not (0 <= y < ROWS): return 0
            if grid[y][x] != ((last + 2) % 4): return 0

            # go straight
            s = 1 + go(x+DIRS[dir][0], y+DIRS[dir][1], grid[y][x], dir, turn)
            if not turn: return s

            # turn
            t = 1 + go(x+DIRS[(dir+1)%4][0], y+DIRS[(dir+1)%4][1], grid[y][x], (dir+1)%4, False)
            return max(s, t)

        res = 0
        for y in range(ROWS):
            for x in range(COLS):
                if grid[y][x] != 1: continue
                for dir, (dx, dy) in enumerate(DIRS):
                    res = max(res, 1 + go(x+dx, y+dy, 0, dir, True))
        return res
