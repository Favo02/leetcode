class Solution:
  def findTheDifference(self, s: str, t: str) -> str:
    qty = {}
    for char in s:
      if char in qty:
        qty[char] += 1
      else:
        qty[char] = 1

    for char in t:
      if char not in qty or qty[char] == 0:
        return char
      qty[char] -= 1
