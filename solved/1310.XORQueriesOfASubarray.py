class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

        prefix = []
        suffix = []

        bits = [0] * 30
        for n in arr:
            ns = bin(n)[2:]
            for i, bit in enumerate(ns[::-1]):
                if bit == "1":
                    bits[i] += 1
            prefix.append(tuple(bits))

        def bitsToInt(bits):
            res = 0
            for i, b in enumerate(bits):
                if b % 2 == 1:
                    res += (1 << i)
            return res

        res = []
        for s, e in queries:
            if s == 0:
                res.append(bitsToInt(prefix[e]))
            else:
                res.append(bitsToInt(
                    [ee-ss for ss, ee in zip(prefix[s-1], prefix[e])]))

        return res
