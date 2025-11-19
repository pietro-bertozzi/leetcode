# Find Pivot Index (https://leetcode.com/problems/find-pivot-index/)
# Difficulty: Easy
# Tags: Array, Prefix Sum

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        summ = sum(nums)
        left = 0
        for i, n in enumerate(nums):
            if left == summ - left - n:
                return i
            left += n
        return -1


solution = Solution()

test_cases = [
    ([1,7,3,6,5,6]), #3
    ([1,2,3]), #-1
]

for s in test_cases:
    print(solution.pivotIndex(s))