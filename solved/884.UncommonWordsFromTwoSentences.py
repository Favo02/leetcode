class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return list(map(itemgetter(0), filter(lambda w: w[1] == 1, Counter(s1.split() + s2.split()).items())))
