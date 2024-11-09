class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        return words[0][0] == words[-1][-1] and all(w1[-1] == w2[0] for w1, w2 in zip(words, words[1:]))
