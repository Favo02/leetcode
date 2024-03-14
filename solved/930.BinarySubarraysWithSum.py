from typing import List

class Solution:
  def compact_zeros(self, nums):
    def first_n_integers(qty):
      return (qty * (qty+1)) // 2

    res = []
    zeros = 0
    zero_goal = 0
    for n in nums:
      if n == 1:
        if zeros > 0:
          res.append((0, zeros))
          zero_goal += first_n_integers(zeros)
          zeros = 0
        res.append((1, 1))
      else:
        zeros += 1

    if zeros > 0:
      res.append((0, zeros))
      zero_goal += first_n_integers(zeros)
    return res, zero_goal

  def positive_goal(self, nums, goal):
    def num_subarrays(prec, post):
      prec = prec[1] if prec[0] == 0 else 0
      post = post[1] if post[0] == 0 else 0
      return 1 + prec + post + prec*post

    summ = 0
    start = end = 0

    res = 0
    while True:

      # start
      for i in range(start, len(nums)):
        if nums[i][0] == 1:
          start = i
          break

      # end
      for i in range(end, len(nums)):
        if nums[i][0] == 1:
          summ += 1
        if summ == goal:
          end = i
          break
      else:
        break

      res += num_subarrays(
        nums[(start-1)] if start > 0 else (1,0),
        nums[(end+1)] if end < len(nums)-1 else (1,0))

      summ -= 1
      start += 1
      end += 1
    return res

  def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    nums, res = self.compact_zeros(nums)

    if goal != 0:
      res = self.positive_goal(nums, goal)

    print(res)
    return res

s = Solution()
s.numSubarraysWithSum([0,0,1,0,0,0,0,1,0], goal = 2)
s.numSubarraysWithSum([1,0,1,0,1], goal = 2)
s.numSubarraysWithSum([0,0,0,0,0], goal = 0)
