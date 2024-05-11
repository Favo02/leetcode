from typing import List

class Solution:
  def satisfiesConditions(self, grid: List[List[int]]) -> bool:

    for r1, r2 in zip(grid, grid[1:]):
      if r1 != r2:
        return False

    for c1, c2 in zip(grid[0], grid[0][1:]):
      if c1 == c2:
        return False

    return True

s = Solution()
print(s.satisfiesConditions([[1,0,2],[1,0,2]]))
print(s.satisfiesConditions([[1,1,1],[0,0,0]]))
print(s.satisfiesConditions([[1],[2],[3]]))
