from typing import List
from collections import deque

class Solution:
  def shortestPathLength(self, graph: List[List[int]]) -> int:
    if len(graph) == 1:
      return 0

    queue = deque()
    seen = set()

    for start in range(len(graph)):
      queue.append((start, 1 << start, 0))

    while queue:
      cur, reached, dist = queue.popleft()

      if (cur, reached) in seen:
        continue
      seen.add((cur, reached))

      for adj in graph[cur]:
        newreached = reached | (1 << adj)
        queue.append((adj, newreached, dist+1))
        if newreached == ((1 << len(graph)) - 1):
          print(dist + 1)
          return dist + 1

    print(-1)
    return -1

s = Solution()
s.shortestPathLength([[1,2,3],[0],[0],[0]]) # 4
s.shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]) # 4
s.shortestPathLength([[1],[0,2,4],[1,3],[2],[1,5],[4]]) # 6
s.shortestPathLength([[1,2,3,4],[0,3],[0],[0,1],[0]]) # 5
s.shortestPathLength([[1,5],[0,3],[3,5],[1,2,5],[7],[0,7,6,2,3],[5],[5,4,8],[7]]) # 10
s.shortestPathLength([[7],[3],[3,9],[1,2,4,5,7,11],[3],[3],[9],[3,10,8,0],[7],[11,6,2],[7],[3,9]]) # 17
s.shortestPathLength([[1,2,3,4,5,6,7,8,9],[0,2,3,4,5,6,7,8,9],[0,1,3,4,5,6,7,8,9],[0,1,2,4,5,6,7,8,9],[0,1,2,3,5,6,7,8,9],[0,1,2,3,4,6,7,8,9],[0,1,2,3,4,5,7,8,9],[0,1,2,3,4,5,6,8,9],[0,1,2,3,4,5,6,7,9,10],[0,1,2,3,4,5,6,7,8,11],[8],[9]])
