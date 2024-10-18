class Solution:
    def minimumSteps(self, s: str) -> int:
        place = 0
        res = 0
        for i, b in enumerate(s):
            if b == "0":
                res += (i - place)
                place += 1
        return res
