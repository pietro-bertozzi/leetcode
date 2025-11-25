# Single Number (https://leetcode.com/problems/single-number/)
# Difficulty: Easy
# Tags: Array, Bit Manipulation

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        for n in nums:
            single ^= n
        return single
        
solution = Solution()

test_cases = [
    ([2,2,1]),     #1
    ([4,1,2,1,2]), #4
    ([1])          #1
]

for nums in test_cases:
    print(solution.singleNumber(nums))
