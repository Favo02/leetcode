from typing import List

class Solution:
  def sortByBits(self, arr: List[int]) -> List[int]:
    countOnes = lambda a: len(list(filter(lambda x: x == '1', bin(a)[2:])))
    arr.sort(key=lambda x: [countOnes(x), x])
    print(arr)
    return arr

s = Solution()
s.sortByBits([0,1,2,3,4,5,6,7,8])
s.sortByBits([1024,512,256,128,64,32,16,8,4,2,1])
