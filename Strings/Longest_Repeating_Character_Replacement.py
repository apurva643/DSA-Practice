# LeetCode #424 - Longest Repeating Character Replacement
# TC: O(n) | SC: O(1)

def characterReplacement(s, k):

    frequency = {}

    left = 0
    max_frequency = 0
    max_length = 0

    for right in range(len(s)):

        # Count frequency of current character
        if s[right] in frequency:
            frequency[s[right]] += 1
        else:
            frequency[s[right]] = 1

        # Maximum frequency in current window
        max_frequency = max(max_frequency, frequency[s[right]])

        # Shrink window if more than k replacements are needed
        while (right - left + 1) - max_frequency > k:

            frequency[s[left]] -= 1
            left += 1

        # Update answer
        max_length = max(max_length, right - left + 1)

    return max_length


# ---------------- Driver Code ----------------

s = "ABAB"
k = 2

print("String:", s)
print("k =", k)
print("Longest Length:", characterReplacement(s, k))

print()

s = "AABABBA"
k = 1

print("String:", s)
print("k =", k)
print("Longest Length:", characterReplacement(s, k))

print()

s = "AAAA"
k = 2

print("String:", s)
print("k =", k)
print("Longest Length:", characterReplacement(s, k))

print()

s = "ABCDE"
k = 1

print("String:", s)
print("k =", k)
print("Longest Length:", characterReplacement(s, k))