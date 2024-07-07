from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        N = len(board)

        jumps = {}
        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c != -1:
                    row = N-i
                    col = j if row % 2 == 1 else (N-j-1)
                    col += N*(row-1)
                    jumps[col] = c-1

        queue = deque([0])

        dp = [float("inf")] * N**2
        dp[0] = 0

        while queue:
            cell = queue.popleft()
            if cell == N**2 - 1:
                return dp[cell]

            for i in range(1,7):
                nextt = jumps.get(cell+i, cell+i)
                if nextt > N**2 - 1:
                    continue
                if dp[cell]+1 < dp[nextt]:
                    dp[nextt] = dp[cell]+1
                    queue.append(nextt)

        return -1


s = Solution()
s.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]])
