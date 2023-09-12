def countFreq(str):
  freq = {}
  for s in str:
    if s in freq:
      freq[s] += 1
    else:
      freq[s] = 1
  return freq

def isOver(freq):
  for f1 in freq:
    for f2 in freq:
      if f1 == f2:
        continue
      if freq[f1] == freq[f2]:
        return f1
  return True
 
def solve(s):
  count = 0
  freq = countFreq(s)

  while True:
    over = isOver(freq)
    if over == True: # explicit check for True, over can be True or a characted (always true-ish value)
      return count

    count+=1
    index = s.index(over)
    s = s[0:index] + s[index+1:]
    freq[over] -= 1
    if freq[over] == 0:
      del freq[over]

class Solution(object):
  def minDeletions(self, s):
    """
    :type s: str
    :rtype: int
    """
    res = solve(s)
    print(res)
    return res
    


Solution.minDeletions(0, "aab")
Solution.minDeletions(0, "aaabbbcc")
Solution.minDeletions(0, "ceabaacb")
