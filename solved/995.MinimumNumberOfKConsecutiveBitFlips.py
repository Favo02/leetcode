class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:

        res = 0
        to_flip = deque()

        for i, n in enumerate(nums):

            if (n + len(to_flip)) % 2 == 0:
                if (i + k) > len(nums):
                    return -1

                res += 1
                to_flip.append(i + k - 1)

            if to_flip and to_flip[0] == i:
                to_flip.popleft()

        return res
