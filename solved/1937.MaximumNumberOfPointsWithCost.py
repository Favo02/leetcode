class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        last_row = [0] * len(points[0])
        for row in points:
            last_row = [lr + r for lr, r in zip(last_row, row)]
            # to right
            maxx = 0
            for i, n in enumerate(last_row):
                maxx = max(maxx, n)
                last_row[i] = maxx
                maxx -= 1
            # to left
            maxx = 0
            for i, n in enumerate(last_row[::-1]):
                maxx = max(maxx, n)
                last_row[-i-1] = maxx
                maxx -= 1

        return max(last_row)
