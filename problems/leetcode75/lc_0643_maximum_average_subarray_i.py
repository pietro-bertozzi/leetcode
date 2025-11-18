# Maximum Average Subarray I (https://leetcode.com/problems/maximum-average-subarray-i/)
# Difficulty: Easy
# Tags: Array, Sliding Window

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        best = candidate = sum(nums[:k])
        for i in range(k, len(nums)):
            candidate += nums[i] - nums[i - k]
            if candidate > best:
                best = candidate
        return best / k
    
solution = Solution()

test_cases = [
    ([1,12,-5,-6,50,3], 4), #12.75000
    ([5], 1),               #5.00000
]

for s, t in test_cases:
    print(solution.findMaxAverage(s, t))