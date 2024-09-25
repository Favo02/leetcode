class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        if len(timePoints) == 1:
            return 0

        mins = []

        for time in timePoints:
            h, m = map(int, time.split(":"))
            mins.append(h * 60 + m)

        mins.sort()

        res = float("inf")

        for a, b in zip(mins, mins[1:]):
            res = min(res, abs(a-b))

        return min(res, 1440 - mins[-1] + mins[0])
