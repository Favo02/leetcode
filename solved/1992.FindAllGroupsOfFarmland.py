from typing import List

class Solution:
  def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

    res = []
    ongoing = {}

    for y, row in enumerate(land):
      sx = -1

      for x, cell in enumerate(row):
        if cell and sx == -1:
          sx = x
        if not cell and sx != -1:
          if (sx, x-1) in ongoing:
            ongoing[(sx, x-1)][1] = y
          else:
            ongoing[(sx, x-1)] = [y, y]
          sx = -1

      if sx != -1:
        if (sx, x) in ongoing:
            ongoing[(sx, x)][1] = y
        else:
          ongoing[(sx, x)] = [y, y]

      res += [(sy, sx, ey, ex) for (sx, ex), (sy, ey) in ongoing.items() if ey != y or y == len(land) -1]
      ongoing = {(sx, ex): [sy, ey] for (sx, ex), (sy, ey) in ongoing.items() if ey == y}

    print(res)
    return res

s = Solution()
s.findFarmland([[1,0,0],[0,1,1],[0,1,1]])
s.findFarmland([[1,1],[0,0]])
s.findFarmland([[1,1,0,0,0,1],[1,1,0,0,0,0]])