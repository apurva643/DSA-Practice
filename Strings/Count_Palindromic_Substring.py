# LeetCode #647 - Count Palindromic Substrings
# Time Complexity: O(n²)
# Space Complexity: O(1)

def countSubstrings(s):

    count = 0

    def expand(left, right):
        nonlocal count

        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1

    for i in range(len(s)):

        # Odd length palindrome
        expand(i, i)

        # Even length palindrome
        expand(i, i + 1)

    return count
