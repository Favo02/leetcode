class Solution:
  def minimumRecolors(self, blocks: str, k: int) -> int:
    white = 0
    res = float("inf")

    for i in range(len(blocks)):
      if blocks[i] == "W":
        white += 1

      if i+1 > k and blocks[i-k] == "W":
          white -= 1

      if i+1 >= k:
        res = min(res, white)

    return res
