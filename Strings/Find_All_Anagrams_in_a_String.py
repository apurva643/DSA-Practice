# LeetCode #438 - Find All Anagrams in a String
# Pattern: Fixed Size Sliding Window + HashMap
# Time Complexity: O(n + m)
# Space Complexity: O(1)

def findAnagrams(s, p):

    if len(p) > len(s):
        return []

    frequencyP = {}
    frequencyWindow = {}

    for ch in p:
        if ch in frequencyP:
            frequencyP[ch] += 1
        else:
            frequencyP[ch] = 1

    for i in range(len(p)):
        if s[i] in frequencyWindow:
            frequencyWindow[s[i]] += 1
        else:
            frequencyWindow[s[i]] = 1

    result = []

    if frequencyP == frequencyWindow:
        result.append(0)

    left = 0

    for right in range(len(p), len(s)):

        if s[right] in frequencyWindow:
            frequencyWindow[s[right]] += 1
        else:
            frequencyWindow[s[right]] = 1

        frequencyWindow[s[left]] -= 1

        if frequencyWindow[s[left]] == 0:
            del frequencyWindow[s[left]]

        left += 1

        if frequencyP == frequencyWindow:
            result.append(left)

    return result
