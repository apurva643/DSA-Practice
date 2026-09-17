# LeetCode 895 - Maximum Frequency Stack
# Pattern: Stack Design
# TC : O(1) for push/pop | SC : O(n)


class FreqStack:

    def __init__(self):
        self.frequency = {}
        self.groups = {}
        self.max_frequency = 0

    def push(self, val):
        self.frequency[val] = self.frequency.get(val, 0) + 1

        freq = self.frequency[val]

        if freq > self.max_frequency:
            self.max_frequency = freq

        if freq not in self.groups:
            self.groups[freq] = []

        self.groups[freq].append(val)

    def pop(self):
        val = self.groups[self.max_frequency].pop()

        self.frequency[val] -= 1

        if not self.groups[self.max_frequency]:
            self.max_frequency -= 1

        return val


