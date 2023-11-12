from typing import List
from collections import deque
from collections import defaultdict

class Solution:
  def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:

    SIZE = len(adjacentPairs) + 1

    res = deque(adjacentPairs[0])

    couples = defaultdict(list)
    for a,b in adjacentPairs:
      couples[a].append(b)
      couples[b].append(a)
    a,b = adjacentPairs[0]
    couples[a].remove(b)
    couples[b].remove(a)

    while len(res) < SIZE:
      next = couples[res[-1]]
      prev = couples[res[0]]

      if next:
        couples[res[-1]] = next[1:]
        couples[next[0]].remove(res[-1])
        res.append(next[0])
      else:
        couples[res[0]] = prev[1:]
        couples[prev[0]].remove(res[0])
        res.appendleft(prev[0])

    print(res)
    return res

s = Solution()
s.restoreArray([[2,1],[3,4],[3,2]])
s.restoreArray([[4,-2],[1,4],[-3,1]])
s.restoreArray([[100000,-100000]])
s.restoreArray([[-3,-9],[-5,3],[2,-9],[6,-3],[6,1],[5,3],[8,5],[-5,1],[7,2]])
