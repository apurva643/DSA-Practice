# LeetCode #383 - Ransom Note
# TC: O(n + m) | SC: O(n)

def canConstruct(ransomNote, magazine):

    frequency = {}

    # Count frequency of magazine
    for ch in magazine:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    # Use characters for ransomNote
    for ch in ransomNote:

        if ch not in frequency:
            return False

        frequency[ch] -= 1

        if frequency[ch] < 0:
            return False

    return True