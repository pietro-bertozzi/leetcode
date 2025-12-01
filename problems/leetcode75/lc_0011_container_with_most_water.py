# Container With Most Water (https://leetcode.com/problems/container-with-most-water/)
# Difficulty: Medium
# Tags: Array, Two Pointers, Greedy

from typing import List

class Solution1:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        left, right = 0, len(height) - 1
        while left < right:
            candidate = min(height[left], height[right]) * (right - left)
            if candidate > best:
                best = candidate
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                best = max(best, height[left] * (right - left))
                left += 1
            else:
                best = max(best, height[right] * (right - left))
                right -= 1
        return best
    
solution1 = Solution1()
solution2 = Solution2()

test_cases = [
    ([1,8,6,2,5,4,8,3,7]), #49
    ([1,1]),               #1
]

for height in test_cases:
    print(solution1.maxArea(height))
for height in test_cases:
    print(solution2.maxArea(height))
