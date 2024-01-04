class Solution:
  def findMatrix(self, nums: List[int]) -> List[List[int]]:
    count = Counter(nums)
    res = []
    while count:
      arr = []
      new_count = {}
      for n, t in count.items():
        arr.append(n)
        if t > 1:
          new_count[n] = t-1
      res.append(arr)
      count = new_count
    print(res)
    return res
