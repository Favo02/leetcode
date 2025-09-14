from typing import List
from collections import deque

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        def bfs(start, end):
            queue = deque()
            queue.append((start, 0))
            seen = set()
            seen.add(start)

            while queue:
                cur, d = queue.popleft()
                for ad in graph[cur]:
                    if ad in seen: continue
                    if ad == end: return d+1
                    seen.add(ad)
                    queue.append((ad, d+1))

            assert False

        res = []
        graph = {c: {c+1} for c in range(n) if c < n-1}
        for fr, to in queries:
            graph[fr].add(to)
            res.append(bfs(0, n-1))
        return res
