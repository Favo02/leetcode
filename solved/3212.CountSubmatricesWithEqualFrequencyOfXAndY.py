from typing import List

class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:

        last_row = [(0, 0)] * len(grid[0])
        res = 0

        for row in grid:
            count = {"X": 0, "Y": 0, ".": 0}
            for x, cell in enumerate(row):
                count[cell] += 1
                cx, cy = last_row[x][0] + count["X"], last_row[x][1] + count["Y"]

                if cx > 0 and cx == cy:
                    res += 1

                last_row[x] = (cx, cy)

        print(res)
        return res

s = Solution()
s.numberOfSubmatrices([["X","Y","."],["Y",".","."]])
