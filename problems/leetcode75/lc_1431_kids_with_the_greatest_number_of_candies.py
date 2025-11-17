# Kids With the Greatest Number of Candies (https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/)
# Difficulty: Easy
# Tags: Array

from typing import List

class Solution1:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        enough = []
        threshold = max(candies) - extraCandies
        for i in range(len(candies)):
            enough.append(candies[i] >= threshold)
        return enough
    
class Solution2:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        threshold = max(candies) - extraCandies
        return [candy >= threshold for candy in candies]
        
solution1 = Solution1()
solution2 = Solution2()

test_cases = [
    ([2,3,5,1,3], 3), #[true,true,true,false,true]
    ([4,2,1,1,2], 1), #[true,false,false,false,false]
    ([12,1,12], 10)   #[true,false,true]
]

for candies, extraCandies in test_cases:
    print(solution1.kidsWithCandies(candies, extraCandies))
for candies, extraCandies in test_cases:
    print(solution2.kidsWithCandies(candies, extraCandies))