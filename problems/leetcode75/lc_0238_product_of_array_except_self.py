# Product of Array Except Self (https://leetcode.com/problems/product-of-array-except-self/)
# Difficulty: Medium
# Tags: Array, Prefix Sum

from typing import List
import math

class Solution1:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in reversed(range(n - 1)):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        return [prefix[i] * suffix[i] for i in range(n)]
    
class Solution2:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result

solution1 = Solution1()
solution2 = Solution2()

test_cases = [
    ([1,2,3,4]),    #[24,12,8,6]
    ([-1,1,0,-3,3]) #[0,0,9,0,0]
]

for nums in test_cases:
    print(solution1.productExceptSelf(nums))
for nums in test_cases:
    print(solution2.productExceptSelf(nums))