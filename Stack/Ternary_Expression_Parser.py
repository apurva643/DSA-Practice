# LeetCode 439 - Ternary Expression Parser
# TC : O(n) | SC: O(n)

def parseTernary(expression):

    stack = []

    i = len(expression) - 1

    while i >= 0:

        if stack and stack[-1] == "?":

            stack.pop()

            true_value = stack.pop()

            stack.pop()

            false_value = stack.pop()

            if expression[i] == "T":
                stack.append(true_value)
            else:
                stack.append(false_value)

        else:

            stack.append(expression[i])

        i -= 1

    return stack[-1]


