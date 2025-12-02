# Max Number of K-Sum Pairs (https://leetcode.com/problems/max-number-of-k-sum-pairs/)
# Difficulty: Medium
# Tags: Array, Hash Table, Two Pointers, Sorting

import collections

class Solution1:
    def maxOperations(self, nums: list[int], k: int) -> int:
        count = {}
        operations = 0
        for num in nums:
            complement = k - num
            if count.get(complement, 0) > 0:
                operations += 1
                count[complement] -= 1
            else:
                count[num] = count.get(num, 0) + 1
        return operations

class Solution2:
  def maxOperations(self, nums: list[int], k: int) -> int:
    count = collections.Counter(nums)
    return sum(min(count[num], count[k - num]) for num in count) // 2
    
solution1 = Solution1()
solution2 = Solution2()

test_cases = [
    ([1,2,3,4], 5),  #2
    ([3,1,3,4,3], 6) #1
]

for nums, k in test_cases:
    print(solution1.maxOperations(nums, k))
for nums, k in test_cases:
    print(solution2.maxOperations(nums, k))