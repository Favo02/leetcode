class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def solve(i, start, formed):
            if i == len(s):
                if start+1 == i:
                    formed.append(s[start:])
                if len(set(formed)) == len(formed):
                    return len(formed)
                return 0

            return max(
                solve(i+1, i+1, formed + [s[start:i+1]]),
                solve(i+1, start, formed)
            )

        return solve(0,0,[])
