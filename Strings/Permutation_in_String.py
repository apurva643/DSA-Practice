# LeetCode #567 - Permutation in String
# Pattern: Fixed Size Sliding Window + HashMap
# TC : O(n) | SC : O(1)

def checkInclusion(s1, s2):

    if len(s1) > len(s2):
        return False

    frequency1 = {}
    frequency2 = {}

    for ch in s1:
        if ch in frequency1:
            frequency1[ch] += 1
        else:
            frequency1[ch] = 1

    for i in range(len(s1)):
        if s2[i] in frequency2:
            frequency2[s2[i]] += 1
        else:
            frequency2[s2[i]] = 1

    if frequency1 == frequency2:
        return True

    left = 0

    for right in range(len(s1), len(s2)):

        # Add new character
        if s2[right] in frequency2:
            frequency2[s2[right]] += 1
        else:
            frequency2[s2[right]] = 1

        # Remove left character
        frequency2[s2[left]] -= 1

        if frequency2[s2[left]] == 0:
            del frequency2[s2[left]]

        left += 1

        if frequency1 == frequency2:
            return True

    return False

