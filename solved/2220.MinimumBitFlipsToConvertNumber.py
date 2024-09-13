class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a = bin(start)[2:]
        b = bin(goal)[2:]

        res = 0

        if len(a) > len(b):
            res += sum(map(int, a[:len(a)-len(b)]))
        elif len(b) > len(a):
            res += sum(map(int, b[:len(b)-len(a)]))

        for aa, bb in zip(a[::-1], b[::-1]):
            if aa != bb:
                res += 1

        return res
