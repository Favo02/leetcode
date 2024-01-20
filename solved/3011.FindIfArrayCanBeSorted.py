from typing import List

class Solution:
  def canSortArray(self, nums: List[int]) -> bool:
    sorted_ = sorted(nums)

    target_index = [sorted_.index(n) for n in nums]
    bits = [sum([1 for c in bin(n)[2:] if c == '1']) for n in nums]

    for i, ti in zip(range(len(nums)), target_index):
      if i == ti:
        continue

      path = bits[min(i, ti) : max(i, ti)+1]
      if any(b != bits[i] for b in path):
        print("False")
        return False

    print("True")
    return True

s = Solution()

print(s.canSortArray([8,4,2,30,15])) # true
print(s.canSortArray([1, 2, 3, 4, 5])) # true
print(s.canSortArray([3,16,8,4,2])) # false
