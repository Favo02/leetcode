def hasAll(string, sub):
  for s in sub:
    if s not in string:
      return False
  return True

class Solution:
  def removeDuplicateLetters(self, s: str) -> str:

    queue = []
    for char in s:
      if char not in queue:
        queue.append(char)
    queue.sort()

    target = len(queue)

    res = []
    curIndex = 0
    buffer = []
    placed = False

    while len(res) < target:
      if placed and len(buffer) > 0:
        queue = buffer + queue
        buffer = []
    
      curChar = queue.pop(0)
      placed = False

      # find leftmost curChar with all other chars to the left
      for i in range(curIndex, len(s)):
        if s[i] == curChar:
          if hasAll(s[i:], queue):
            curIndex = i
            res.append(curChar)
            placed = True
            break
      else:
        buffer.append(curChar)

    res = "".join(res)
    print(res)
    return res

s = Solution()
s.removeDuplicateLetters("bcabc") # abc
s.removeDuplicateLetters("cbacdcbc") # acdb
s.removeDuplicateLetters("cdadabcc") # adbc
