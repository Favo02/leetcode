class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mins = sorted([(arrays[0][0], 0), (arrays[1][0], 1)])
        maxs = sorted([(arrays[0][-1], 0), (arrays[1][-1], 1)], reverse=True)

        for i, arr in enumerate(arrays[2:]):
            if arr[0] < mins[1][0]:
                mins[1] = (arr[0], i+2)
                mins.sort()
            if arr[-1] > maxs[1][0]:
                maxs[1] = (arr[-1], i+2)
                maxs.sort(reverse=True)

        if mins[0][1] != maxs[0][1]:
            return abs(mins[0][0] - maxs[0][0])

        return max(abs(mins[1][0] - maxs[0][0]), abs(mins[0][0] - maxs[1][0]))
