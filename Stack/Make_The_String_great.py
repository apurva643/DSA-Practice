# LeetCode 1544 - Make The String Great
# TC : O(n) | SC: O(n)

def makeGood(s):

    stack = []

    for ch in s:

        if stack and abs(ord(stack[-1]) - ord(ch)) == 32:
            stack.pop()

        else:
            stack.append(ch)

    return "".join(stack)
