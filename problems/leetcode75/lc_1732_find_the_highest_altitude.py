# Find the Highest Altitude (https://leetcode.com/problems/find-the-highest-altitude/)
# Difficulty: Easy
# Tags: Array, Prefix Sum

from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
            candidate = best = 0
            for g in gain:
                 candidate += g
                 if candidate > best:
                      best = candidate
            return best

solution = Solution()

test_cases = [
    ([-5,1,5,0,-7]), #1
    ([-4,-3,-2,-1,4,3,2]), #0
]

for gain in test_cases:
    print(solution.largestAltitude(gain))