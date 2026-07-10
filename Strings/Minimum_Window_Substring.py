# LeetCode #76 - Minimum Window Substring
# Pattern: Variable Sliding Window + HashMap
# Time Complexity: O(n)
# Space Complexity: O(m)

from collections import Counter


def minWindow(s, t):

    if len(t) > len(s):
        return ""

    target = Counter(t)
    window = {}

    required = len(target)
    formed = 0

    left = 0

    min_length = float("inf")
    start = 0

    for right in range(len(s)):

        char = s[right]

        # Add current character
        if char in window:
            window[char] += 1
        else:
            window[char] = 1

        # Check if this character requirement is satisfied
        if char in target and window[char] == target[char]:
            formed += 1

        # Shrink window while it is valid
        while formed == required:

            # Update minimum window
            if right - left + 1 < min_length:
                min_length = right - left + 1
                start = left

            left_char = s[left]

            # Remove left character
            window[left_char] -= 1

            # Window is no longer valid
            if left_char in target and window[left_char] < target[left_char]:
                formed -= 1

            left += 1

    if min_length == float("inf"):
        return ""

    return s[start:start + min_length]

