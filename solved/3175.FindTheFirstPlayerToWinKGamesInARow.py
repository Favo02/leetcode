from typing import List
from collections import deque

class Solution:
  def findWinningPlayer(self, skills: List[int], k: int) -> int:
    skills = deque(enumerate(skills))

    a = skills.popleft()
    won = 0

    while skills and won < k:
      b = skills.popleft()
      if a[1] > b[1]:
        won += 1
      else:
        won = 1
        a = b

    print(a[0])
    return a[0]


s = Solution()
s.findWinningPlayer(skills = [4,2,6,3,9], k = 2)
s.findWinningPlayer(skills = [2,5,4], k = 3)
s.findWinningPlayer([16,4,7,17], 562084119)
