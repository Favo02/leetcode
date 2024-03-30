from typing import List

class Solution:
  def minimumLevels(self, possible: List[int]) -> int:
    enemy = []
    post = 0
    for n in reversed(possible):
      post += 1 if n == 1 else -1
      enemy.append(post)
    enemy = list(reversed(enemy))

    pre = 0
    for i, n in enumerate(possible[:-1]):
      pre += 1 if n == 1 else -1
      if pre > enemy[i+1]:
        print(i+1)
        return i+1

    print(-1)
    return -1

s = Solution()
s.minimumLevels([1,0,1,0])
s.minimumLevels([1,1,1,1,1])
s.minimumLevels([0,0])
