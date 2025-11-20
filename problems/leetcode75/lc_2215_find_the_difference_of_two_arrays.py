# Find the Difference of Two Arrays (https://leetcode.com/problems/find-the-difference-of-two-arrays/)
# Difficulty: Easy
# Tags: Array, Hash Table


from typing import List

class Solution1:
  def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
    set1 = set(nums1)
    set2 = set(nums2)
    return [list(set1 - set2), list(set2 - set1)]
  
class Solution2:
  def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
    return [list(set(nums1)-set(nums2)), list(set(nums2)-set(nums1))]

solution1 = Solution1()
solution2 = Solution2()

test_cases = [
    ([1,2,3], [2,4,6]), #[[1,3],[4,6]]
    ([1,2,3,3], [1,1,2,2]), #[[3],[]]
]

for nums1, nums2 in test_cases:
    print(solution1.findDifference(nums1, nums2))
for nums1, nums2 in test_cases:
    print(solution2.findDifference(nums1, nums2))