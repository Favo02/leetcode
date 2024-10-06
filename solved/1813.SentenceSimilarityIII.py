class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()

        short = s1 if len(s1) < len(s2) else s2
        longg = s2 if len(s1) < len(s2) else s1

        gap = abs(len(s1) - len(s2))

        for i in range(len(short)+1):
            if (short[:i] == longg[:i]) and (short[i:] == longg[i+gap:]):
                return True
        return False
