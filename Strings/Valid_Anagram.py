# LeetCode #242 - Valid Anagram
# TC: O(n) | SC: O(n)

def isAnagram(s, t):

    if len(s) != len(t):
        return False

    frequency = {}

    for ch in s:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    for ch in t:

        if ch not in frequency:
            return False

        frequency[ch] -= 1

        if frequency[ch] < 0:
            return False

    return True
