# LeetCode #151 - Reverse Words in a String
# TC: O(n) | # SC: O(n)

from typing import List

class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()

        words.reverse()

        return " ".join(words)