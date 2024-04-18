class Solution:
  def islandPerimeter(self, grid: List[List[int]]) -> int:
    res = 0
    for y, row in enumerate(grid):
      for x, c in enumerate(row):
        if not c:
          continue
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
          if not (0 <= x+dx < len(row)) or\
            not (0 <= y+dy < len(grid)) or\
            not grid[y+dy][x+dx]:
              res += 1 
    return res