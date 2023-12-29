from typing import List

def solve(jobs, ji, cur_day_max, days_left, mem) -> int:
  if (ji, cur_day_max, days_left) in mem:
    return mem[(ji, cur_day_max, days_left)]

  result = float("inf")

  if ji == len(jobs) and days_left == 0:
    result = cur_day_max
  elif ji >= len(jobs):
    result = float("inf")
  else:
    # place job this day (only if there are enough jobs for the remaining days)
    if (len(jobs) - ji) >= days_left:
      result = min(result, solve(jobs, ji+1, max(jobs[ji], cur_day_max), days_left, mem))

    # place job next day (only if there are some days left)
    if days_left > 0:
      result = min(result, cur_day_max + solve(jobs, ji+1, jobs[ji], days_left-1, mem))

  mem[(ji, cur_day_max, days_left)] = result
  return result

class Solution:
  def minDifficulty(self, jobDifficulty: List[int], days: int) -> int:
    global jobs
    jobs = jobDifficulty

    if len(jobs) < days:
      print(-1)
      return -1

    res = solve(jobs, 0, 0, days, {})
    print(res)
    return res

s = Solution()
s.minDifficulty([6,5,4,3,2,1], 2)
s.minDifficulty([9,9,9], 4)
s.minDifficulty([1,1,1], 3)
