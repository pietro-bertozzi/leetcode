# Move Zeroes (https://leetcode.com/problems/move-zeroes/)
# Difficulty: Easy
# Tags: Array, Two Pointers

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        i = 0
        for n in nums:
            if n != 0:
                nums[i] = n
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0
        print(nums)
 
solution = Solution()

test_cases = [
    ([0,1,0,3,12]), #[1,3,12,0,0]
    ([0]),          #[0]
]

for nums in test_cases:
    solution.moveZeroes(nums)