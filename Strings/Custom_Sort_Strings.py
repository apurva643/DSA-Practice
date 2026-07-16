class Solution:
    def customSortString(self, order: str, s: str) -> str:

        frequency = {}

        for ch in s:
            if ch in frequency:
                frequency[ch] += 1
            else:
                frequency[ch] = 1

        result = ""

        for ch in order:

            if ch in frequency:
                result += ch * frequency[ch]
                del frequency[ch]

        for ch, count in frequency.items():
            result += ch * count

        return result