# Can Place Flowers (https://leetcode.com/problems/can-place-flowers/)
# Difficulty: Easy
# Tags: Array, Greedy

from typing import List

class Solution1:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:  
        for i, flower in enumerate(flowerbed):
            if flower == 0 and (
                    i == 0 or flowerbed[i - 1] == 0) and (
                    i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False
    
class Solution2:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed):
            nextfree = i + 1 >= len(flowerbed) or flowerbed[i+1] == 0
            if flowerbed[i] == 0 and nextfree:
                n -= 1
            i += 2 if nextfree else 3
        return n <= 0 

solution1 = Solution1()
solution2 = Solution2()

test_cases = [
    ([1,0,0,0,1], 1), #True
    ([1,0,0,0,1], 2), #False
    ([1,0,0,0,0,1], 2) #False
]

for flowerbed, n in test_cases:
    print(solution1.canPlaceFlowers(flowerbed, n))
for flowerbed, n in test_cases:
    print(solution2.canPlaceFlowers(flowerbed, n))