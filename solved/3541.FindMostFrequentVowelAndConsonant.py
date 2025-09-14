from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        return max((v for k, v in Counter(s).items() if k in "aeiou"), default=0) + max((v for k, v in Counter(s).items() if k not in "aeiou"), default=0)
