class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0
        for w in words:
            if all(ww in allowed for ww in w):
                res += 1
        return res
