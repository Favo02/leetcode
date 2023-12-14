class Solution:
  def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
    rows = [sum(r) for r in grid]
    cols = [sum([r[x] for r in grid]) for x in range(len(grid[0]))]

    for y in range(len(grid)):
      for x in range(len(grid[0])):
        grid[y][x] = rows[y]+cols[x] - ((len(cols)-rows[y])+(len(rows)-cols[x]))
    return grid
