# LeetCode 1172 - Dinner Plate Stacks
# Pattern: Stack Design
# TC : O(log n) per operation | SC : O(n)

import heapq


class DinnerPlates:

    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

        # Min-heap → leftmost stack with available space
        self.available = []

        # Max-heap → rightmost non-empty stack
        self.non_empty = []

    def push(self, val):

        # Remove invalid/full stacks from available
        while self.available and (
            self.available[0] >= len(self.stacks)
            or len(self.stacks[self.available[0]]) >= self.capacity
        ):
            heapq.heappop(self.available)

        # No available stack → create new stack
        if not self.available:
            index = len(self.stacks)

            self.stacks.append([])

            heapq.heappush(self.available, index)

        index = self.available[0]

        self.stacks[index].append(val)

        # Stack is now non-empty
        heapq.heappush(self.non_empty, -index)

        # If stack becomes full, remove from available
        if len(self.stacks[index]) == self.capacity:
            heapq.heappop(self.available)

    def pop(self):

        # Remove invalid/empty stacks
        while self.non_empty and (
            -self.non_empty[0] >= len(self.stacks)
            or not self.stacks[-self.non_empty[0]]
        ):
            heapq.heappop(self.non_empty)

        if not self.non_empty:
            return -1

        index = -heapq.heappop(self.non_empty)

        val = self.stacks[index].pop()

        # Stack now has space
        heapq.heappush(self.available, index)

        # If still non-empty, keep it tracked
        if self.stacks[index]:
            heapq.heappush(self.non_empty, -index)

        return val

    def popAtStack(self, index):

        if index >= len(self.stacks) or not self.stacks[index]:
            return -1

        val = self.stacks[index].pop()

        # Stack now has space
        heapq.heappush(self.available, index)

        # Still has elements
        if self.stacks[index]:
            heapq.heappush(self.non_empty, -index)

        return val


