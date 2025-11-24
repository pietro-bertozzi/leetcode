# Counting Bits (https://leetcode.com/problems/counting-bits/)
# Difficulty: Easy
# Tags: Dynamic Programming, Bit Manipulation

from typing import List

class Solution:
    def countBits(self, n: int) -> list[int]:
        counts = [0] * (n + 1)
        for i in range(1, n + 1):
            counts[i] = counts[i & i - 1] + 1
        return counts
  
solution = Solution()

test_cases = [
    (2), #[0,1,1]
    (5)  #[0,1,1,2,1,2]
]

for n in test_cases:
    print(solution.countBits(n))
