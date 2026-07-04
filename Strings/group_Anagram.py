# LeetCode #49 - Group Anagrams
# Time Complexity: O(n × k log k)
# Space Complexity: O(n × k)

def groupAnagrams(strs):

    groups = {}

    for word in strs:

        key = "".join(sorted(word))

        if key in groups:
            groups[key].append(word)
        else:
            groups[key] = [word]

    return list(groups.values())