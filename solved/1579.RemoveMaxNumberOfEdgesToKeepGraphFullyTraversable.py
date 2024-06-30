class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        graph = {i:[] for i in range(1, n+1)}
        for ty, fr, to in edges:
            graph[fr].append((ty, to))
            graph[to].append((ty, fr))

        def bfs(who, start):
            remove = []
            remove_both = []

            queue = deque([(start, None)])
            queue_both = deque([])
            seen = set()

            while queue or queue_both:
                if queue_both:
                    ty = 3
                    cur, prev = queue_both.popleft()
                else:
                    ty = who
                    cur, prev = queue.popleft()

                if cur in seen:
                    if ty == 3:
                        remove_both.append((cur, prev))
                    elif ty == who:
                        remove.append((cur, prev))
                    continue
                seen.add(cur)
                for t, adj in graph[cur]:
                    if adj == prev:
                        continue
                    if t == who:
                        queue.append((adj, cur))
                    if t == 3:
                        queue_both.append((adj, cur))

            return len(seen) == n, remove, remove_both

        valid_a, rem_a, rem_both_a = bfs(1, 1)
        if not valid_a:
            return -1
        valid_b, rem_b, rem_both_b = bfs(2, 1)
        if not valid_b:
            return -1

        rem_a = set(map(lambda t: frozenset(t), rem_a))
        rem_b = set(map(lambda t: frozenset(t), rem_b))

        rem_both_a = set(map(lambda t: frozenset(t), rem_both_a))
        rem_both_b = set(map(lambda t: frozenset(t), rem_both_b))

        return len(rem_a) + len(rem_b) + len(rem_both_a & rem_both_b)
