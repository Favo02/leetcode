from typing import List

class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    lastRow = [1]
    for _ in range(rowIndex):
      for j in range(len(lastRow)-1):
        lastRow[j] += lastRow[j+1]
      lastRow.insert(0, 1)
    print(lastRow)
    return lastRow

s = Solution()
s.getRow(10)
# s.getRow(10_000)
