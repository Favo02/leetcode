class Solution:
    def compressedString(self, word: str) -> str:
        count = 0
        last = None
        res = []
        for w in word:
            if last and (last != w or count == 9):
                res.append(str(count) + last)
                count = 1
            else:
                count += 1
            last = w
        res.append(str(count) + last)
        return "".join(res)
