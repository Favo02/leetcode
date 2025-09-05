class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x, y = abs(x-z), abs(y-z)
        return x < y and 1 or y < x and 2 or 0
