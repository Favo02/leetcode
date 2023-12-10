from typing import List

class Solution:
  def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
    return [[r[i] for r in matrix] for i in range(len(matrix[0]))]

s = Solution()
print(s.transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(s.transpose([[1,2,3],[4,5,6]]))
