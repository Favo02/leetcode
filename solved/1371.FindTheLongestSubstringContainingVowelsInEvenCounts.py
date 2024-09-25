class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        vow = [True] * 5
        first_seen = {}
        last_seen = {}

        for i, c in enumerate(s):
            key = tuple(vow)
            if key in first_seen:
                last_seen[key] = i
            else:
                first_seen[key] = i

            pos = "aeiou".find(c)
            if pos != -1:
                vow[pos] = not vow[pos]

        key = tuple(vow)
        if key in first_seen:
            last_seen[key] = len(s)
        else:
            first_seen[key] = len(s)

        res = 0
        for k, f in first_seen.items():
            if k in last_seen:
                res = max(res, last_seen[k] - f)

        return res
