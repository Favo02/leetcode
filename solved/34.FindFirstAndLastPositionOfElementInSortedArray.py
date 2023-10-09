from typing import List

def startBinSearch(arr, x):
  low = 0
  high = len(arr) - 1
  mid = 0
  while low <= high:
    mid = (high + low) // 2
    if arr[mid] < x:
      low = mid + 1
    elif arr[mid] > x:
      high = mid - 1
    else:
      if mid != 0 and arr[mid-1] == x:
        high = mid-1
      else:
        return mid
  return -1

def endBinSearch(arr, x):
  low = 0
  high = len(arr) - 1
  mid = 0
  while low <= high:
    mid = (high + low) // 2
    if arr[mid] < x:
      low = mid + 1
    elif arr[mid] > x:
      high = mid - 1
    else:
      if mid != len(arr)-1 and arr[mid+1] == x:
        low = mid+1
      else:
        return mid
  return -1

class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    start = startBinSearch(nums, target)
    if start == -1:
      print(-1,-1)
      return [-1,-1]
    end = endBinSearch(nums, target)
    print(start, end)
    return [start, end]

s = Solution()
s.searchRange([5,7,7,8,8,10], 8)
s.searchRange([5,7,7,8,8,8,8,8,8,8,8,8,10], 8)
s.searchRange([5,7,7,8,10], 8)
s.searchRange([5,7,7,8,8,10], 6)
s.searchRange([], 0)
