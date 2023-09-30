from typing import List

def compress(nums):
  newNums = [nums[0]]
  for n in nums:
    if n != newNums[-1]:
      newNums.append(n)
  return newNums

def check(arr, pos, n):
  for a in arr[:pos]:
    if a[0] == n: continue
    for b in arr[pos:]:
      if b[0] == n: continue
      if b[1] > a[1]:
        return True
  return False

class Solution:
  def find132pattern(self, nums: List[int]) -> bool:
    nums = compress(nums)

    if (max(nums) - min(nums)) < 2:
      return False

    stack = [ (nums[0], -1) ]
    for i, n in enumerate(nums[1:]):
      if n >= stack[-1][0]:
        stack.append((n, i))
      else:
        ins = 0
        while stack[ins][0] < n:
          ins += 1
        
        if ins == 0:
          stack.insert(0, (n, i))
        else:
          # check that exists a tuple after ins position with index greather than a tuple before ins position
          if check(stack, ins, n):
            return True
          else:
            stack.insert(ins, (n, i))
            
    return False

s = Solution()
print(s.find132pattern([3,1,2,2])) # false
print(s.find132pattern([-2,1,1])) # false
print(s.find132pattern([3,4,5,1,2,6,5,7,9])) # true
print(s.find132pattern([1,2,3,4])) # false
print(s.find132pattern([3,1,4,2])) # true
print(s.find132pattern([-1,3,2,0])) # true
print(s.find132pattern([3,5,0,3,4])) # true
print(s.find132pattern([1,0,1,-4,-3])) # false
