from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [0] * 9
        cols = [0] * 9
        groups = [0] * 9

        for y in range(9):
            for x in range(9):
                if board[y][x] == ".": continue
                rows[y] |= (1 << int(board[y][x]))
                cols[x] |= (1 << int(board[y][x]))
                groups[(y // 3)*3 + (x // 3)] |= (1 << int(board[y][x]))

        def solve(pos):
            if pos >= 81: return True
            x, y = pos % 9, pos // 9
            g = (y // 3)*3 + (x // 3)

            if board[y][x] != ".": return solve(pos+1)

            for n in range(1, 10):
                if ((1 << n) & rows[y]) != 0: continue
                if ((1 << n) & cols[x]) != 0: continue
                if ((1 << n) & groups[g]) != 0: continue

                rows[y] |= (1 << n)
                cols[x] |= (1 << n)
                groups[g] |= (1 << n)

                if solve(pos+1):
                    board[y][x] = str(n)
                    return True

                rows[y] &= ~(1 << n)
                cols[x] &= ~(1 << n)
                groups[g] &= ~(1 << n)

            return False

        solve(0)
