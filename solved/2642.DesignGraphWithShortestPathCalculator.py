from typing import List

class Graph:

  def __init__(self, n: int, edges: List[List[int]]):
    self.graph = {}
    for nn in range(n):
      self.graph[nn] = []

    for edge in edges:
      a = edge[0]
      b = edge[1]
      cost = edge[2]
      self.graph[a].append((b, cost))

  def addEdge(self, edge: List[int]) -> None:
    a = edge[0]
    b = edge[1]
    cost = edge[2]
    self.graph[a].append((b, cost))

  def shortestPath(self, node1: int, node2: int) -> int:
    dist = {node1: 0}
    queue = [node1]

    while queue:
      cur = queue.pop(0)
      curD = dist[cur]
      for adj, cost in self.graph[cur]:
        newD = curD + cost
        if adj not in dist or newD < dist[adj]:
          dist[adj] = newD
          queue.append(adj)

    return dist[node2] if node2 in dist else -1

g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
