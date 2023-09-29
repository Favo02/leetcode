def genBlocks(s):
  sizes = []
  indexes = []
  letters = []
  count = 0
  for i, c in enumerate(s):
    if c.isdigit() or i == len(s)-1:
      size = count + ((int(c)-1) * (sum(sizes) + count) if c.isdigit() else 1)
      sizes.append(size)
      indexes.append(i)
      letters.append(count if c.isdigit() else count+1)
      count = 0
    else:
      count += 1

  return sizes, indexes, letters

class Solution:
  def decodeAtIndex(self, s: str, k: int) -> str:
  
    sizes, indexes, letters = genBlocks(s)
    # print(sizes)
    # print(indexes)
    # print(letters)
    
    cursorInd = -1
    blockInd = 0
    while True:
      if k <= letters[blockInd]:
        return s[cursorInd + k]

      if k > sizes[blockInd]:
        k -= sizes[blockInd]
        cursorInd = indexes[blockInd]
        blockInd += 1
        continue
  
      k -= letters[blockInd]
      cursorInd = -1
      blockInd = 0

s = Solution()
print(s.decodeAtIndex("abc", 1)) # a
print(s.decodeAtIndex("abc", 3)) # c

print(s.decodeAtIndex("leet2code3", 10)) # o
print(s.decodeAtIndex("leet2code3", 11)) # d
print(s.decodeAtIndex("leet2code3", 12)) # e
print(s.decodeAtIndex("leet2code3", 13)) # l
print(s.decodeAtIndex("leet2code3", 14)) # e
print(s.decodeAtIndex("leet2code3", 15)) # e

print(s.decodeAtIndex("leet2code3", 10)) # o
print(s.decodeAtIndex("ha22", 5)) # h
print(s.decodeAtIndex("a2345678999999999999999", 1)) # a
print(s.decodeAtIndex("a23", 6)) # a
print(s.decodeAtIndex("a2b3c4d5e6f7g8h9", 9)) # b
print(s.decodeAtIndex("a2b3c4d5e6f7g8h9", 10)) # c
print(s.decodeAtIndex("a2b3c4d5e6f7g8h9", 30)) # c
print(s.decodeAtIndex("y959q969u3hb22odq595", 222280369))
