from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:

        colors.insert(0, colors[-1])
        colors.append(colors[1])


        res = 0
        for a, b, c in zip(colors, colors[1:], colors[2:]):
            if a == c and a != b:
                res += 1

        print(res)
        return res


s = Solution()
s.numberOfAlternatingGroups([1,1,1])
s.numberOfAlternatingGroups([0,1,0,0,1])
