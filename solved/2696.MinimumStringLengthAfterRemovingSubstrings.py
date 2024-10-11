class Solution:
    def minLength(self, s: str) -> int:
        return len(s) \
            if ("AB" not in s and "CD" not in s) else \
            self.minLength( s.replace("AB", "").replace("CD", ""))
