# graph: weight matrix
def floydWarshall(graph):
  INF = 1_000_000_000
  N = len(graph)
  dist = [[INF for _ in range(N)] for _ in range(N)]

  for i in range(N):
    for adj in graph[i]:
      dist[i][adj] = 1

  for i in range(N):
    for j in range(N):
      if i == j:
        dist[i][j] = 0
        continue
      for k in range(N):
        newD = dist[i][k] + dist[k][j]
        if newD < dist[i][j]:
          dist[i][j] = newD

  return dist
