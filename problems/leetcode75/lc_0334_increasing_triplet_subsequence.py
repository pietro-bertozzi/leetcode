# Increasing Triplet Subsequence (https://leetcode.com/problems/increasing-triplet-subsequence/)
# Difficulty: Medium
# Tags: Array, Greedy

import math
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = math.inf #float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
    
solution = Solution()

test_cases = [
    ([1,2,3,4,5]),  #True
    ([5,4,3,2,1]),  #False
    ([2,1,5,0,4,6]) #True
]

for nums in test_cases:
    print(solution.increasingTriplet(nums))
