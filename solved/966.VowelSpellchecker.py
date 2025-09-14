from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def VOW(w):
            return w.lower().replace('a','*').replace('e','*').replace('i','*').replace('o','*').replace('u','*')

        res = []

        set_wordlist = set(wordlist)
        insensitive = dict(reversed({w.lower(): w for w in reversed(wordlist)}.items()))
        vowels = dict(reversed({VOW(w): w for w in reversed(wordlist)}.items()))

        for q in queries:
            if q in set_wordlist:
                res.append(q)
            elif q.lower() in insensitive:
                res.append(insensitive[q.lower()])
            elif VOW(q) in vowels:
                res.append(vowels[VOW(q)])
            else:
                res.append("")

        return res
