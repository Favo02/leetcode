from typing import List
from math import ceil

class Solution:
  def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:

    health = [ceil(h / power) for h in health]


    ratio = [(h / d, h, d) for h, d in zip(health, damage)]
    ratio.sort()
    # print(ratio)

    dmg = sum(damage)
    res = 0

    for r, h, d in ratio:
      res += dmg*h
      dmg -= d

    print(res)
    return res

s = Solution()
s.minDamage(power = 4, damage = [1,2,3,4], health = [4,5,6,8])
s.minDamage(power = 1, damage = [1,1,1,1], health = [1,2,3,4])
s.minDamage(power = 8, damage = [40], health = [59])
