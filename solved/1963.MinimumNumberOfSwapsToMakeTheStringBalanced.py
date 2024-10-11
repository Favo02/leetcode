class Solution:
    def minSwaps(self, s: str) -> int:

        res = 0
        openn = 0

        for b in s:
            if b == "[":
                openn += 1
            else:
                if openn <= 0:
                    res += 1
                    openn += 1
                else:
                    openn -= 1

        return res
