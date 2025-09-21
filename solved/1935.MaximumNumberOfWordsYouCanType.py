class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return len(list(True for w in text.split() if not any(c in brokenLetters for c in w)))
