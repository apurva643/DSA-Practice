# LeetCode 496 - Next Greater Element I
# Pattern: Monotonic Stack (Next Greater Element)
# TC : O(n) | SC : O(n)

def nextGreaterElement(nums1, nums2):

    stack = []
    greater = {}

    for num in nums2:

        while stack and num > stack[-1]:
            smaller = stack.pop()
            greater[smaller] = num

        stack.append(num)

    for num in stack:
        greater[num] = -1

    result = []

    for num in nums1:
        result.append(greater[num])

    return result


# Driver Code

nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]

print(nextGreaterElement(nums1, nums2))