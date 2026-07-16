# LeetCode #71 - Simplify Path
# TC: O(n) | SC: O(n)

def simplifyPath(path):

    stack = []

    parts = path.split('/')

    for part in parts:

        if part == "" or part == ".":
            continue

        elif part == "..":

            if stack:
                stack.pop()

        else:
            stack.append(part)

    return "/" + "/".join(stack)
