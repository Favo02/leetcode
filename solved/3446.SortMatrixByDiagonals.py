from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        N = len(grid)
        asc = ((i,0) for i in range(1, N))
        dec = ((0,i) for i in range(0, N))

        for starts, rev in ((asc, False), (dec, True)):
            for sx, sy in starts:
                cur = []
                x, y = sx, sy
                while x < N and y < N:
                    cur.append(grid[y][x])
                    x += 1
                    y += 1
                cur.sort(reverse=rev)
                x, y = sx, sy
                for c in cur:
                    grid[y][x] = c
                    x += 1
                    y += 1

        return grid
