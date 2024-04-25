from typing import List
from collections import defaultdict, deque

class Solution:
  def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    if n <= 2:
      return range(n)

    graph = defaultdict(list)
    for s, e in edges:
      graph[s].append(e)
      graph[e].append(s)

    leafs = set()
    for node, edges in graph.items():
      if len(edges) == 1:
        leafs.add(node)

    def dfs(node, prec):
      if (node, prec) in mem:
        return mem[(node, prec)]
      res = 0
      for adj in graph[node]:
        if adj == prec:
          continue
        res = max(res, 1 + dfs(adj, node))
      mem[(node, prec)] = res
      return res

    mem = {}
    res = []
    minn = float("inf")
    for root in range(n):
      if root in leafs:
        continue
      h = dfs(root, -1)
      if h < minn:
        minn = h
        res = [ root ]
      elif h == minn:
        res.append(root)

    print(res)
    return res

s = Solution()
s.findMinHeightTrees(4, [[1,0],[1,2],[1,3]])
s.findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]])
s.findMinHeightTrees(7, [[0,1],[1,2],[1,3],[2,4],[3,5],[4,6]])
