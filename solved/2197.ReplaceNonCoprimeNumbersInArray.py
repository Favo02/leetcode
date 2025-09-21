from typing import List
from collections import deque
# from math import gcd, lcm

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        def gcd(a, b):
            return b == 0 and a or gcd(b, a % b)

        def lcm(a, b):
            return a * b // gcd(a, b)

        stack = deque()
        for n in nums:
            stack.append(n)
            while len(stack) > 1 and gcd(stack[-1], stack[-2]) > 1:
                stack.append(lcm(stack.pop(), stack.pop()))
        return list(stack)
