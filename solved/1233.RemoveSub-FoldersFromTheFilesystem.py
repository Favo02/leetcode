class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        folder.sort(key=len)
        seen = set()
        res = []

        for f in folder:
            t = tuple(filter(lambda a: a, f.split("/")))
            for i in range(1, len(t)+1):
                sub = t[:i]
                if sub in seen:
                    break
            else:
                res.append(f)
            seen.add(t)

        return res
