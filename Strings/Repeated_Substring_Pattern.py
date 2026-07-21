# ==========================================================
# LeetCode 459 - Repeated Substring Pattern
# Pattern: KMP (String Matching)
#
# Solution 1 : Brute Force
# Time Complexity : O(n²)
# Space Complexity: O(n)
#
# Solution 2 : KMP Algorithm
# Time Complexity : O(n)
# Space Complexity: O(n)
# ==========================================================


# ==========================================================
# Solution 1 : Brute Force
# ==========================================================

def repeatedSubstringPatternBrute(s):

    n = len(s)

    for length in range(1, n // 2 + 1):

        if n % length == 0:

            substring = s[:length]

            if substring * (n // length) == s:
                return True

    return False

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

def repeatedSubstringPatternKMP(s):

    lps = buildLPS(s)

    last = lps[-1]

    return last > 0 and len(s) % (len(s) - last) == 0
