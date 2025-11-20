# Unique Number of Occurrences (https://leetcode.com/problems/unique-number-of-occurrences/)
# Difficulty: Easy
# Tags: Array, Hash Table

from typing import Counter, List

class Solution1:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = {}
        for a in arr:
            if a in occurrences:
                occurrences[a] += 1
            else:
                occurrences[a] = 1
        seen = set()
        for o in occurrences.values():
            if o in seen:
                return False
            seen.add(o)
        return True
    
class Solution2:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        occ = list(count.values())
        return len(occ) == len(set(occ))
    
solution1 = Solution1()
solution2 = Solution2()

test_cases = [
    ([1,2,2,1,1,3]),             #True
    ([1,2]),                     #False
    ([-3,0,1,-3,1,1,1,-3,10,0])  #True
]

for arr in test_cases:
    print(solution1.uniqueOccurrences(arr))
for arr in test_cases:
    print(solution2.uniqueOccurrences(arr))