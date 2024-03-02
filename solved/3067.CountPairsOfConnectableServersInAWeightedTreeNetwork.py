from typing import List
from collections import defaultdict

class Solution:
  def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
    N = len(edges) + 1

    graph = defaultdict(list)
    for f, t, w in edges:
      graph[f].append((t, w))
      graph[t].append((f, w))

    res = []
    for c in range(N):
      count = 0
      if len(graph[c]) == 0:
        continue

      lists = []
      for ed, w in graph[c]:
        q = [(ed, w)]
        curlist = []
        seen = set()
        seen.add(c)

        while q:
          cur, curw = q.pop(0)
          if curw % signalSpeed == 0:
            curlist.append((cur, curw))
          seen.add(cur)

          for adj, adjw in graph[cur]:
            if adj in seen: continue
            q.append((adj, curw + adjw))

        if curlist:
          lists.append(len(curlist))

      # print()
      # print("==:", c)
      # print(lists)
      count = 0
      for i, a in enumerate(lists):
        for b in lists[i+1:]:
          # print(a,b)
          count += a*b

      res.append(count)
    print(res)
    return res


s = Solution()
s.countPairsOfConnectableServers([[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]], signalSpeed = 1)
s.countPairsOfConnectableServers(edges = [[0,6,3],[6,5,3],[0,3,1],[3,2,7],[3,1,6],[3,4,2]], signalSpeed = 3)
s.countPairsOfConnectableServers([[1,0,2],[2,1,4],[3,2,4],[4,0,3],[5,1,4],[6,2,2],[7,6,4],[8,1,2],[9,8,3]], 1)
