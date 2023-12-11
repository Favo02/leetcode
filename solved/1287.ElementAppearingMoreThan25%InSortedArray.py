class Solution:
  def findSpecialInteger(self, arr: List[int]) -> int:
    count = 0
    last = -1
    for n in arr:
      if n == last:
        count += 1
      else:
        count = 1
      last = n
      if count > (len(arr)/4):
        print(n)
        return n
