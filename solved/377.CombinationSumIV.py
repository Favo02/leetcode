memoization = {}

def recursion(nums, target):
  if target in memoization:
    return memoization[target]

  if target == 0:
    memoization[target] = 1
    return 1
  
  count = 0
  for n in nums:
    if n <= target: 
      count += recursion(nums, target - n)
  
  memoization[target] = count
  return count

class Solution(object):
  def combinationSum4(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    memoization.clear()
    res = recursion(nums, target)
    print(res)
    return res

Solution.combinationSum4(0, [1,2,3], 4)
Solution.combinationSum4(0, [9], 3)
Solution.combinationSum4(0, [1,2,3], 32)
