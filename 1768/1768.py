class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(c for z in zip_longest(word1, word2) for c in z if c)
