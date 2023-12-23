class Solution:
  def isPathCrossing(self, path: str) -> bool:
    DIRS = {"N": (0,-1), "S": (0,+1), "E": (+1,0), "W": (-1,0)}

    cur = (0, 0)
    seen = set([ cur ])
    for dir in path:
      dx, dy = DIRS[dir]
      cur = cur[0]+dx, cur[1]+dy
      if cur in seen:
        return True
      seen.add(cur)
    return False

