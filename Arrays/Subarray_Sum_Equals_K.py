# LeetCode #560 - Subarray Sum Equals K
# Time Complexity: O(n)
# Space Complexity: O(n)

def subarraySum(nums, k):

    prefix = {0: 1}

    running_sum = 0
    count = 0

    for num in nums:

        running_sum += num

        need = running_sum - k

        if need in prefix:
            count += prefix[need]

        if running_sum in prefix:
            prefix[running_sum] += 1
        else:
            prefix[running_sum] = 1

    return count
