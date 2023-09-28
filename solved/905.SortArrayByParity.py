from typing import List

class Solution:
  def sortArrayByParity(self, nums: List[int]) -> List[int]:
    res = [-1 for _ in range(len(nums))]
    i = 0
    j = len(nums)-1
    for n in nums:
      if n%2 == 0:
        res[i] = n
        i += 1
      else:
        res[j] = n
        j -= 1
    print(res)
    return res

s = Solution()
s.sortArrayByParity([3,1,2,4])
s.sortArrayByParity([0])
s.sortArrayByParity([3,1,2,5,4])
s.sortArrayByParity([1,3])
s.sortArrayByParity([0,1,2])
s.sortArrayByParity([3,0,1])
