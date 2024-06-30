class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        incoming = {c:0 for c in range(n)}
        for a, b in roads:
            incoming[a] += 1
            incoming[b] += 1

        cities = dict(
            map(lambda a: (a[1], a[0]),
            enumerate(
            map(itemgetter(0), sorted(incoming.items(), key=itemgetter(1))))))

        res = 0
        for a, b in roads:
            res += cities[a]+1 + cities[b]+1
        return res
