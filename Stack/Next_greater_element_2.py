# LeetCode 503 - Next Greater Element II
# Pattern: Monotonic Stack (Next Greater Element)
# TC : O(n) | SC : O(n)


def nextGreaterElements(nums):

    n = len(nums)

    stack = []
    result = [-1] * n

    for i in range(2 * n):

        index = i % n

        while stack and nums[index] > nums[stack[-1]]:

            previous_index = stack.pop()

            result[previous_index] = nums[index]

        if i < n:
            stack.append(index)

    return result
