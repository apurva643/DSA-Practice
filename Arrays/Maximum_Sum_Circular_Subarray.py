# LeetCode #918 - Maximum Sum Circular Subarray
# Time Complexity: O(n)
# Space Complexity: O(1)

def Maximum_subarray(nums):

    current_sum = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(current_sum + nums[i], nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


def Minimum_subarray(nums):

    current_sum = nums[0]
    min_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = min(current_sum + nums[i], nums[i])
        min_sum = min(min_sum, current_sum)

    return min_sum


def Maximum_Circular_Subarray(nums):

    total_sum = sum(nums)

    max_subarray = Maximum_subarray(nums)

    if max_subarray < 0:
        return max_subarray

    min_subarray = Minimum_subarray(nums)

    circular_sum = total_sum - min_subarray

    return max(max_subarray, circular_sum)


