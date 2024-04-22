from typing import List
from collections import deque

class Solution:
  def openLock(self, deadends: List[str], target: str) -> int:
    def adjs(cur):
      cur = list(cur)
      for i, digit in enumerate(cur):
        cur[i] = (digit + 1) % 10
        yield tuple(cur)
        cur[i] = (digit - 1) % 10
        yield tuple(cur)
        cur[i] = digit

    deadends = {tuple([int(digit) for digit in state]) for state in deadends}
    target = tuple([int(digit) for digit in target])

    if target == (0,0,0,0):
      return 0
    if (0,0,0,0) in deadends:
      return -1

    seen = set()
    q = deque([ ((0,0,0,0), 0) ])

    while q:
      cur, dist = q.popleft()
      for adj in adjs(cur):
        if adj == target:
          return dist+1
        if adj in deadends or adj in seen:
          continue
        q.append((adj, dist+1))
        seen.add(adj)

    return -1

s = Solution()
print(s.openLock(["0201","0101","0102","1212","2002"], target = "0202"))

