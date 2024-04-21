class Solution:
  def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if source == destination:
      return True

    graph = defaultdict(list)
    for f, t in edges:
      graph[f].append(t)
      graph[t].append(f)

    q = deque([source])
    seen = set()
    while q:
      cur = q.popleft()
      for adj in graph[cur]:
        if adj in seen:
          continue
        if adj == destination:
          return True
        seen.add(adj)
        q.append(adj)
    return False
