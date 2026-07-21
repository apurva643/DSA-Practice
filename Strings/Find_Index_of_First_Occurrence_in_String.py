# ==========================================================
# LeetCode 28 - Find the Index of the First Occurrence in a String
# Pattern: String Matching
#
# Solution 1: Brute Force
# Time Complexity : O(n * m)
# Space Complexity: O(m)
#
# Solution 2: KMP (Knuth-Morris-Pratt)
# Time Complexity : O(n + m)
# Space Complexity: O(m)
# ==========================================================


# ==========================================================
# Solution 1 : Brute Force
# ==========================================================

def strStrBrute(haystack, needle):

    n = len(haystack)
    m = len(needle)

    for i in range(n - m + 1):

        if haystack[i:i + m] == needle:
            return i

    return -1


# ==========================================================
# Solution 2 : KMP Algorithm
# ==========================================================

def buildLPS(pattern):

    lps = [0] * len(pattern)

    length = 0
    i = 1

    while i < len(pattern):

        if pattern[i] == pattern[length]:

            length += 1
            lps[i] = length
            i += 1

        else:

            if length != 0:
                length = lps[length - 1]

            else:
                lps[i] = 0
                i += 1

    return lps


def strStrKMP(haystack, needle):

    if needle == "":
        return 0

    lps = buildLPS(needle)

    i = 0      # Pointer for haystack
    j = 0      # Pointer for needle

    while i < len(haystack):

        if haystack[i] == needle[j]:

            i += 1
            j += 1

            if j == len(needle):
                return i - j

        else:

            if j != 0:
                j = lps[j - 1]

            else:
                i += 1

    return -1

