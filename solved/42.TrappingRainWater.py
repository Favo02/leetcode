from typing import List

class Solution:
  def trap(self, height: List[int]) -> int:

    rightmax = []
    rm = -1
    for h in height[::-1]:
      rightmax.append(rm)
      rm = max(rm, h)

    water = 0

    lm = 0
    for h, rm in zip(height, rightmax[::-1]):
      if lm > h and rm > h:
        water += min(lm, rm) - h
      lm = max(lm, h)

    print(water)
    return water

s = Solution()
s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) # 6
s.trap([4,2,0,3,2,5]) # 9
s.trap([0,1,2,0,3,0,1,2,0,0,4]) # 14
s.trap([0,1,2,0,3,0,1,2,0,0,4,2,1,2,5,0,1,2,0,2]) # 26
