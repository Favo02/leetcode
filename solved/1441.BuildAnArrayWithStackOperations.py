from typing import List

class Solution:
  def buildArray(self, target: List[int], n: int) -> List[str]:
    res = []

    stream = 1
    for t in target:
      while stream != t:
        res.append("Push")
        res.append("Pop")
        stream += 1
      res.append("Push")
      stream += 1
    print(res)
    return res

s = Solution()
s.buildArray(target = [1,3], n = 3)
s.buildArray(target = [1,2,3], n = 3)
s.buildArray(target = [1,2], n = 4)
