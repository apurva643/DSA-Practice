# LeetCode #387 - First Unique Character in a String
# TC: O(n) | SC: O(n)

def firstUniqChar(s):

    frequency = {}

    for ch in s:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    for i in range(len(s)):
        if frequency[s[i]] == 1:
            return i

    return -1
