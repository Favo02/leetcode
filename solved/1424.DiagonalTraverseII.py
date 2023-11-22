from typing import List

class Solution:
  def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:

    dict = {}
    for i,nn in enumerate(nums):
      for j,n in enumerate(nn):
        if i + j in dict:
          dict[i+j].append(n)
        else:
          dict[i+j] = [n]

    res = []
    for kk in dict.keys():
      res += list(reversed(dict[kk]))

    print(res)
    return res

s = Solution()
s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]) # [1,4,2,7,5,3,8,6,9]
s.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]) # [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
s.findDiagonalOrder([[1,2,3,4,5,6]]) # [1,2,3,4,5,6]
