class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        pref = defaultdict(int)
        for w in words:
            for i in range(1, len(w)+1):
                pref[w[:i]] += 1

        res = []
        for w in words:
            c = 0
            for i in range(1, len(w)+1):
                c += pref[w[:i]]
            res.append(c)

        return res
