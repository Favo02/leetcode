class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7

        dp = [0] * forget
        dp[0] = 1

        tot = 0
        res = 1
        for _ in range(n-1):
            tot = (tot + dp[delay-1] - dp[-1]) % MOD
            res = (res + tot - dp[-1]) % MOD
            dp = [tot] + dp[:-1]
        return res

s = Solution()
s.peopleAwareOfSecret(6, 2, 4)
