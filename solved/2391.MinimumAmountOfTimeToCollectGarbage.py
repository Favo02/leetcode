from typing import List

class Solution:
  def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
    travel.insert(0,0)

    m,p,g = 0,0,0
    tm,tp,tg = 0,0,0

    for i, gar in enumerate (garbage):
      tm+=travel[i]
      tp+=travel[i]
      tg+=travel[i]

      gm = gar.count("M")
      gp = gar.count("P")
      gg = gar.count("G")

      if gm > 0:
        m += gm
        m += tm
        tm = 0

      if gp > 0:
        p += gp
        p += tp
        tp = 0

      if gg > 0:
        g += gg
        g += tg
        tg = 0

    print(m+p+g)
    return m+p+g

s = Solution()
s.garbageCollection(garbage = ["G","P","GP","GG"], travel = [2,4,3]) # 21
s.garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10]) # 37
