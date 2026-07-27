# LeetCode 1209 - Remove All Adjacent Duplicates in String II
# TC : O(n) | SC: O(n)

def removeDuplicates(s, k):

    stack = []

    for ch in s:

        if stack and stack[-1][0] == ch:

            stack[-1][1] += 1

            if stack[-1][1] == k:
                stack.pop()

        else:

            stack.append([ch, 1])

    answer = ""

    for ch, count in stack:

        answer += ch * count

    return answer
