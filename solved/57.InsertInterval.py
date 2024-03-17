from typing import List

class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if not intervals:
      return [newInterval]

    start = None
    end = None
    for i, (s,e) in enumerate(intervals):
      if start is None and e >= newInterval[0]:
        start = i
      if end is None and s > newInterval[1]:
        end = i-1
        break

    if start is None: start = len(intervals)
    if end is None: end = len(intervals)-1

    if start > end:
      return intervals[:start] + [newInterval] + intervals[start:]
    else:
      return intervals[:start] + [[min(newInterval[0], intervals[start][0]), max(newInterval[1], intervals[end][1])]] + intervals[end+1:]

s = Solution()
print(s.insert(intervals = [[0,1],[6,9]], newInterval = [2,5]))
print(s.insert(intervals = [[0,2],[6,9]], newInterval = [2,5]))
print(s.insert(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))
print(s.insert(intervals = [], newInterval = [4,8]))
print(s.insert(intervals = [[1,5]], newInterval = [2,3]))
