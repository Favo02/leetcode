class Solution:
  def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
    
    row = 0
    nextRow = [ poured ]

    while row <= query_row:
      lastRow = nextRow
      nextRow = [0 for _ in range(row+2)]
      # print(lastRow, nextRow)

      for index, qty in enumerate(lastRow):

        if qty > 1:
          lastRow[index] = 1
          qty = (qty-1) / 2

          nextRow[index] += qty
          nextRow[index+1] += qty

      row += 1

    print(lastRow[query_glass])
    return lastRow[query_glass]

s = Solution()
s.champagneTower(1, 1, 1) # 0
s.champagneTower(2, 1, 1) # 0.5
s.champagneTower(25, 6, 1) # 0.1875
s.champagneTower(100000009, 33, 17) # 1
s.champagneTower(1000000000, 99, 99) # 0

