from typing import List
from collections import deque

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    def bfs(start, seen):
      q = deque([start])
      while q:
        x, y = q.popleft()
        for dx, dy in [(0,1), (0, -1), (1,0), (-1, 0)]:
          if not (0 <= x + dx < len(grid[0])): continue
          if not (0 <= y + dy < len(grid)): continue
          if grid[y+dy][x+dx] == "0": continue
          next = (x+dx, y+dy)
          if next in seen: continue
          seen.add(next) 
          q.append(next)
      return seen
    
    seen = set()
    res = 0
    for y, row in enumerate(grid):
      for x, c in enumerate(row):
        if c == "1" and (x,y) not in seen:
          res += 1
          seen.add((x, y)) 
          seen = bfs((x,y), seen)
    return res

s = Solution()
s.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
])    