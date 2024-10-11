class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        bal = res = 0

        for p in s:
            if p == "(":
                bal += 1
            else:
                bal -= 1
                if bal < 0:
                    res += 1
                    bal = 0

        return res + max(0, bal)
