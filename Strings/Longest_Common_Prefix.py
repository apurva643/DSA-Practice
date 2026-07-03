# LeetCode #14 - Longest Common Prefix
# Time Complexity: O(n × m)
# Space Complexity: O(1)

def longestCommonPrefix(strs):

    first = strs[0]

    for i in range(len(first)):

        for word in strs[1:]:

            if i >= len(word) or word[i] != first[i]:
                return first[:i]

    return first