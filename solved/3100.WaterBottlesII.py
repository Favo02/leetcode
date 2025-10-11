class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        empty = numBottles
        while empty >= numExchange:
            empty = empty - numExchange + 1
            res += 1
            numExchange += 1
        return res
