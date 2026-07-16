# LeetCode #451 - Sort Characters By Frequency
# Time Complexity: O(n log n)
# Space Complexity: O(n)

def frequencySort(s):

    frequency = {}

    for ch in s:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

    sorted_frequency = sorted(
        frequency.items(),
        key=lambda x: x[1],
        reverse=True
    )

    result = ""

    # Build final string
    for ch, count in sorted_frequency:
        result += ch * count

    return result
