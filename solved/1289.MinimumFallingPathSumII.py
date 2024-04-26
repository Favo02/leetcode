from typing import List
from operator import itemgetter

class Solution:
  def minFallingPathSum(self, grid: List[List[int]]) -> int:

    last_row_min = sorted(enumerate(grid[0]), key=itemgetter(1))[:2]

    for y in range(1, len(grid)):
      cur_row_min = []

      for x, num in enumerate(grid[y]):
        non_zero_shift = last_row_min[0][1] if last_row_min[0][0] != x else last_row_min[1][1]
        cur_row_min.append((x, num + non_zero_shift))
        cur_row_min = sorted(cur_row_min, key=itemgetter(1))[:2]

      last_row_min = cur_row_min

    res = last_row_min[0][1]
    print(res)
    return res

s = Solution()
s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]])
s.minFallingPathSum([[7]])
