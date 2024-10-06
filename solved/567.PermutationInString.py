class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = [0]*26
        for c in s1:
            d1[ord(c) - ord('a')] += 1

        d2 = [0]*26
        start = 0
        for end, c in enumerate(s2):
            while (end-start) >= len(s1):
                d2[ord(s2[start]) - ord('a')] -= 1
                start += 1
            d2[ord(c) - ord('a')] += 1

            if d1 == d2:
                return True

        return False
