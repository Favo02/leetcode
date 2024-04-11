from collections import deque

class Solution:
  def removeKdigits(self, num: str, k: int) -> str:

    if k == len(num):
      return "0"

    rem = deque(num)
    res = deque()

    assert len(num) > 1

    while k > 0:
      while len(rem) >= 2 and rem[0] <= rem[1]:
        res.append(rem.popleft())
      rem.popleft()
      k -= 1
      if res:
        rem.appendleft(res.pop())

    return "".join(res + rem).lstrip("0") or "0"

s = Solution()
print(s.removeKdigits("1432219", 3))
print(s.removeKdigits("10200", 1))
print(s.removeKdigits("10", 2))
print(s.removeKdigits("112", 1))
print(s.removeKdigits("1111111", 3))
print(s.removeKdigits("10001", 4))
