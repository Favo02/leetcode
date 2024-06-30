class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        starts = set(range(n))
        graph = {i: [] for i in range(n)}
        for f, t in edges:
            graph[f].append(t)
            starts.discard(t)

        ancestors = {i: set() for i in range(n)}

        def bfs(start):
            queue = deque(graph[start])
            seen = set()
            while queue:
                cur = queue.popleft()
                if cur in seen:
                    continue
                seen.add(cur)
                ancestors[cur].add(start)
                queue += graph[cur]

        for i in range(n):
            bfs(i)

        return list(map(sorted, ancestors.values()))
