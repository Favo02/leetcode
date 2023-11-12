from typing import List

def bfs(routes, connections, start, endBuses):
  queue = [start]
  dist = [None for _ in range(len(routes)+1)]
  dist[start] = 0

  while queue:
    cur = queue.pop(0)
    if cur in endBuses:
      return dist[cur]

    for adj in connections[cur]:
      if dist[adj] == None:
        dist[adj] = dist[cur]+1
        queue.append(adj)

  return -1

class Solution:
  def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
    if source == target:
      print(0)
      return 0

    connections = [set() for _ in routes]
    graph = {}
    for i, bus in enumerate(routes):
      for stop in bus:
        if stop in graph:
          graph[stop].append(i)
        else:
          graph[stop] = [i]

    for _, buses in graph.items():
      if len(buses) > 1:
        for b1 in buses:
          for b2 in buses:
            if b1 != b2:
              connections[b1].add(b2)

    startBuses = graph[source]
    try:
      endBuses = graph[target]
    except:
      print(-1)
      return -1

    N = len(routes)
    connections.append(startBuses)

    r = bfs(routes, connections, N, endBuses)
    print(r)
    return r

s = Solution()
s.numBusesToDestination(routes = [[1,2,7],[3,6,7]], source = 1, target = 6)
s.numBusesToDestination(routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12)
