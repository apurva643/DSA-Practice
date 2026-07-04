# LeetCode #205 - Isomorphic Strings
# Time Complexity: O(n) | Space Complexity: O(n)

def isIsomorphic(s, t):

    if len(s) != len(t):
        return False

    mapST = {}
    mapTS = {}

    for i in range(len(s)):

        if s[i] in mapST:

            if mapST[s[i]] != t[i]:
                return False

        else:
            mapST[s[i]] = t[i]

        if t[i] in mapTS:

            if mapTS[t[i]] != s[i]:
                return False

        else:
            mapTS[t[i]] = s[i]

    return True


