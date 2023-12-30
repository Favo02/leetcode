from typing import List
from collections import defaultdict

class Solution:
  def makeEqual(self, words: List[str]) -> bool:
    count = defaultdict(int)
    for w in words:
      for c in w:
        count[c] += 1

    for times in count.values():
      if times % len(words) != 0:
        print(False)
        return False
    print(True)
    return True

s = Solution()
s.makeEqual(["abc","aabc","bc"])
s.makeEqual(["ab","a"])
