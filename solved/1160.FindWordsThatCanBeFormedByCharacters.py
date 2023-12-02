class Solution:
  def countCharacters(self, words: List[str], chars: str) -> int:
    cc = {}
    for c in chars:
      if c in cc: cc[c] += 1
      else: cc[c] = 1

    res = 0

    for w in words:
      wc = {}
      for c in w:
        if c in wc: wc[c] += 1
        else: wc[c] = 1

      for c,v in wc.items():
        if not (c in cc and v <= cc[c]):
          break
      else:
        res += len(w)

    print(res)
    return res
