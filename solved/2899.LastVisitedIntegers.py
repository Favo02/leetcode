from typing import List

class Solution:
  def lastVisitedIntegers(self, words: List[str]) -> List[int]:
    res = []
    
    consecutive = 0
    integers = []
    for i, w in enumerate(words):
      if w == "prev":
        consecutive += 1
        revIntegers = list(reversed(integers))
        if consecutive > len(revIntegers):
          res.append(-1)
        else:
          res.append(revIntegers[consecutive-1])
      else:
        consecutive = 0
        integers.append(int(w))
    
    print(res)
    return res
  
s = Solution()
s.lastVisitedIntegers(["1","2","prev","prev","prev"]) # 2, 1, -1
s.lastVisitedIntegers(["1","prev","2","prev","prev"]) # 1, 2, 1
