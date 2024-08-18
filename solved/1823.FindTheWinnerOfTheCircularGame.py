class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        assert k <= n

        # 0 indexed winner
        def solve(n):
            if n == 2:
                return k % 2
            elim = k % n
            subwinner = solve(n-1)
            return (subwinner + elim) % n

        if n == 1:
            return 1
        return solve(n) + 1

s = Solution()
print(s.findTheWinner(5,2)) # 3
print(s.findTheWinner(5,4)) # 1
print(s.findTheWinner(6,3)) # 1
print(s.findTheWinner(12,3)) # 10
