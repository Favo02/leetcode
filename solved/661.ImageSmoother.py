from typing import List

class Solution:
  def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
    W, H = len(img[0]), len(img)
    newimg = [[0 for _ in range(W)] for _ in range(H)]
    for y in range(H):
      for x in range(W):
        cur = 0
        num = 0

        for dy in [-1, 0, +1]:
          for dx in [-1, 0, +1]:
            nx, ny = x+dx, y+dy
            if (0 <= nx < W) and (0 <= ny < H):
              cur += img[ny][nx]
              num += 1
        newimg[y][x] = cur // num
    return newimg

s = Solution()
s.imageSmoother([[100,200,100],[200,50,200],[100,200,100]])
