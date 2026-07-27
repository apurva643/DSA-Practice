# LeetCode 844 - Backspace String Compare
# TC : O(n + m) | SC: O(n + m)

def process(string):

    stack = []

    for ch in string:

        if ch != "#":
            stack.append(ch)

        else:

            if stack:
                stack.pop()

    return "".join(stack)


def backspaceCompare(s, t):

    return process(s) == process(t)
