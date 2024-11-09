class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for start in range(len(s)):
            if s[start:] + s[:start] == goal:
                return True
        return False
