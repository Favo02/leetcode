from typing import List

class Solution:
  def maximalSquare(self, matrix: List[List[str]]) -> int:

    for i,m in enumerate(matrix):
      for j in range(len(m)):
        matrix[i][j] = int(matrix[i][j])

    Max = 0

    if len(matrix) > 0 and 1 in matrix[0]:
      Max = 1
    for m in matrix:
      if len(m) > 0 and m[0] == 1:
        Max = 1

    for y, m in enumerate(matrix):
      if y == 0: continue
      for x in range(len(m)):
        if x == 0: continue

        if matrix[y][x] == 1:
          matrix[y][x] = min(matrix[y-1][x], matrix[y-1][x-1], matrix[y][x-1])+1
          Max = max(Max, matrix[y][x])

    print(Max*Max)
    return Max*Max

s = Solution()
s.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
s.maximalSquare([["0","1"],["1","0"]])
s.maximalSquare([["0"]])
s.maximalSquare([["1","1"],["1","1"]])
s.maximalSquare([["0","1","0","0"],["0","1","1","1"],["1","1","1","1"],["0","1","1","1"]])
