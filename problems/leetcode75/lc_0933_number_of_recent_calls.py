# Number of Recent Calls (https://leetcode.com/problems/number-of-recent-calls/)
# Difficulty: Easy
# Tags: Design, Queue, Data Stream

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

import collections

class RecentCounter:
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

tests = [
    {
        "commands": ["RecentCounter", "ping", "ping", "ping", "ping"],
        "arguments": [[], [1], [100], [3001], [3002]]
    },
]

for t in tests:
    obj = None
    outputs = []
    for cmd, arg in zip(t["commands"], t["arguments"]):
        if cmd == "RecentCounter":
            obj = RecentCounter()
            outputs.append(None)
        elif cmd == "ping":
            result = obj.ping(arg[0])
            outputs.append(result)
        else:
            raise ValueError("Comando sconosciuto:", cmd)
    print(outputs)
