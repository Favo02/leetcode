def group_size(count):
  if not count:
    return 0
  if count == 1:
    return 1
  return 1 + len(str(count))

def solve(string, index, last_char, last_count, to_remove, mem) -> int:
  if (index, last_char, last_count, to_remove) in mem:
    return mem[(index, last_char, last_count, to_remove)]

  if index == len(string):
    mem[(index, last_char, last_count, to_remove)] = group_size(last_count)
    return group_size(last_count)

  keep = float("inf")
  remove = float("inf")

  # keep: there are enough characters to be removed past this index
  if to_remove <= len(string) - (index+1):

    # contigous group
    if last_char == string[index]:
      keep = solve(string, index+1, last_char, last_count+1, to_remove, mem)
    # different character: new group
    else:
      keep = group_size(last_count) + solve(string, index+1, string[index], 1, to_remove, mem)

  # remove: there are enough "remove token" left
  if to_remove > 0:
    remove = solve(string, index+1, last_char, last_count, to_remove-1)

  mem[(index, last_char, last_count, to_remove)] = min(keep, remove)
  return min(keep, remove)

class Solution:
  def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
    res = solve(s, 0, None, None, k, {})
    print(res)
    return res

s = Solution()
s.getLengthOfOptimalCompression("aabbaa", 2) # 2
s.getLengthOfOptimalCompression("aaabcccd", 2) # 4
s.getLengthOfOptimalCompression("aaaaaaaaaaa", 0) # 3
s.getLengthOfOptimalCompression("aaaaabaaaaafffwfff", 2) # 5
s.getLengthOfOptimalCompression("abcdefghijklmnopqrstu", 10) # 11
s.getLengthOfOptimalCompression("abcdefghijklmnopqrstuvwxyz", 16) # 10
s.getLengthOfOptimalCompression("cbbabbcebddcbeeddecebffbccdfbbfaaddcdbccbefacdadbebafeecacbdddeedbbedfdecdbdbc", 55)
s.getLengthOfOptimalCompression("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuv", 10)
s.getLengthOfOptimalCompression("rdpiocpgffhammefahhqshgprrbsigdqckacbpiaqasbnnrnmmppsslbdpmsdnskrihcbpappifbiqjmjigfemlelkfabcsclnn", 85)
s.getLengthOfOptimalCompression("a", 1)
