from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        languages = list(map(set, languages))
        friendships = list(map(lambda a: (a[0]-1, a[1]-1), friendships))

        LANS = [set() for _ in range(n)]
        for a, b in friendships:
            if (languages[a] & languages[b]):
                continue
            for lan in range(1, n+1):
                if lan in languages[a]:
                    LANS[lan-1].add(b)
                elif lan in languages[b]:
                    LANS[lan-1].add(a)
                else:
                    LANS[lan-1].add(a)
                    LANS[lan-1].add(b)

        res = min(map(len, LANS))
        print(res)
        return res
