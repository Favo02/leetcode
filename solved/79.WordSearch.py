from typing import List
from collections import Counter, defaultdict

class Solution:

  def dfs(self, x, y, target, seen, board, word):

    if target == len(word):
      return True

    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
      nx = x + dx
      ny = y + dy

      if not (0 <= ny < len(board)):
        continue
      if not (0 <= nx < len(board[0])):
        continue
      if (nx, ny) in seen:
        continue

      if word[target] == board[ny][nx]:
        newseen = seen.copy()
        newseen.add((nx, ny))
        if self.dfs(nx, ny, target+1, newseen, board, word):
          return True

    return False

  def exist(self, board: List[List[str]], word: str) -> bool:

    target = Counter(word)
    available = defaultdict(int)

    queue = []

    for y, row in enumerate(board):
      for x, cell in enumerate(row):

        available[cell] += 1

        if cell == word[0]:

          if len(word) == 1:
            print(True)
            return True

          queue.append((x, y, 1, {(x,y)}, board, word))

    for k, v in target.items():
      if available[k] < v:
        print(False)
        return False

    for x, y, t, s, _, _ in queue:
      if self.dfs(x, y, t, s, board, word):
        print(True)
        return True

    print(False)
    return False

s = Solution()
s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE")
s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB")
s.exist([["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]], "AAAAAAAAAAAAAAB")
