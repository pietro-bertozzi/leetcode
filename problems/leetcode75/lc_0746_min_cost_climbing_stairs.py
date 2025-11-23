# Min Cost Climbing Stairs (https://leetcode.com/problems/min-cost-climbing-stairs/)
# Difficulty: Easy
# Tags: Array, Dynamic Programming

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return cost[-1]
  
solution = Solution()

test_cases = [
    ([10,15,20]),                 #15
    ([1,100,1,1,1,100,1,1,100,1]) #6
]

for cost in test_cases:
    print(solution.minCostClimbingStairs(cost))
