# LeetCode 735 - Asteroid Collision
# TC : O(n) | SC: O(n)

def asteroidCollision(asteroids):

    stack = []

    for asteroid in asteroids:

        while stack and asteroid < 0 and stack[-1] > 0:

            if stack[-1] < -asteroid:

                stack.pop()

            elif stack[-1] == -asteroid:

                stack.pop()
                break

            else:

                break

        else:

            stack.append(asteroid)

    return stack
