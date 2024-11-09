class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for l in s:
            if len(res) >= 2 and res[-1] == res[-2] == l: continue
            res.append(l)
        return "".join(res)
